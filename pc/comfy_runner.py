#!/usr/bin/env python3
"""Run on the ComfyUI PC. Usage: comfy_runner.py

Fetches the repo, finds art jobs (art/<slug>/job.json on main) that have no
drop yet, renders every prompt through the local ComfyUI API, then:
  - copies the images to DRIVE_DIR/<slug>/ (your Google Drive folder), and
  - commits them to the art-drop branch as drops/<slug>/*.png plus DONE, and pushes.
The weekly cloud run picks drops up from art-drop, checks, packages and publishes.

Settings come from pc/runner.ini next to this file (see SETUP.md). Standard
library only, so it runs with any Python 3.9+ on Windows, macOS or Linux.
"""
import configparser, json, pathlib, random, shutil, subprocess, sys, time, urllib.parse, urllib.request, uuid

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent
CFG = configparser.ConfigParser()
CFG.read(HERE / "runner.ini")
S = CFG["runner"] if CFG.has_section("runner") else {}
COMFY = S.get("comfy_url", "http://127.0.0.1:8188").rstrip("/")
CKPT = S.get("checkpoint", "sd_xl_base_1.0.safetensors")
WORKFLOW = HERE / S.get("workflow", "workflow_sdxl_api.json")
DRIVE_DIR = pathlib.Path(S["drive_dir"]) if S.get("drive_dir") else None
DROP = REPO / ".art-drop"  # separate worktree for the art-drop branch


def git(*args, cwd=REPO, check=True):
    return subprocess.run(["git", *args], cwd=cwd, check=check, capture_output=True, text=True).stdout


def comfy(path, body=None):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(COMFY + path, data=data, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read() if path.startswith("/view") else json.load(r)


def fill(node, values):
    """Replace %PROMPT%-style placeholders anywhere in the workflow."""
    if isinstance(node, dict):
        return {k: fill(v, values) for k, v in node.items()}
    if isinstance(node, list):
        return [fill(v, values) for v in node]
    if isinstance(node, str) and node in values:
        return values[node]
    return node


def render(job, item):
    values = {"%PROMPT%": item["prompt"], "%NEGATIVE%": job.get("negative", ""),
              "%SEED%": random.randint(1, 2**31), "%CKPT%": CKPT,
              "%WIDTH%": job.get("width", 1024), "%HEIGHT%": job.get("height", 1024)}
    wf = fill(json.loads(WORKFLOW.read_text(encoding="utf-8")), values)
    pid = comfy("/prompt", {"prompt": wf, "client_id": str(uuid.uuid4())})["prompt_id"]
    for _ in range(600):  # up to 20 minutes per image
        hist = comfy(f"/history/{pid}").get(pid)
        if hist and hist.get("outputs"):
            for out in hist["outputs"].values():
                for img in out.get("images", []):
                    q = urllib.parse.urlencode({k: img[k] for k in ("filename", "subfolder", "type")})
                    return comfy("/view?" + q)
        if hist and hist.get("status", {}).get("status_str") == "error":
            raise RuntimeError(f"ComfyUI error on {item['name']}")
        time.sleep(2)
    raise TimeoutError(item["name"])


def prepare_drop():
    """Fresh worktree of art-drop; an orphan branch when the cloud run has deleted it."""
    git("pull", "-q", "--ff-only", "origin", "main", check=False)  # keep this script current
    remote = git("ls-remote", "--heads", "origin", "art-drop").strip()
    if DROP.exists():
        git("worktree", "remove", "--force", str(DROP))
    git("worktree", "prune")
    git("branch", "-D", "art-drop", check=False)
    if remote:
        git("fetch", "-q", "origin", "art-drop")
        git("worktree", "add", "-q", "-B", "art-drop", str(DROP), "origin/art-drop")
    else:
        git("worktree", "add", "-q", "--detach", str(DROP))
        git("checkout", "-q", "--orphan", "art-drop", cwd=DROP)
        git("rm", "-rfq", ".", cwd=DROP, check=False)


def pending_jobs():
    names = git("ls-tree", "-r", "--name-only", "origin/main", "art").splitlines()
    for path in sorted(n for n in names if n.endswith("/job.json")):
        slug = path.split("/")[1]
        if not (DROP / "drops" / slug / "DONE").exists():
            yield slug, json.loads(git("show", f"origin/main:{path}"))


def kits():
    """After a bundle is live, build the Etsy, Adobe Stock and Dreamstime kits into the Drive folder."""
    if not DRIVE_DIR:
        return
    catalog = git("show", "origin/main:pipeline/catalog.md")
    live = {row.split("|")[2].strip() for row in catalog.splitlines()
            if row.count("|") > 3 and " live " in row}
    for slug in sorted(live):
        src = DRIVE_DIR / slug
        if not (src / "DONE").exists() or (src / "kits" / "DONE").exists():
            continue
        for script in ("art_package.py", "art_kits.py"):
            subprocess.run([sys.executable, f"pipeline/{script}", slug, str(src)], cwd=REPO, check=True)
        for kind in ("etsy", "adobe", "dreamstime"):
            shutil.copytree(REPO / "dist" / f"{slug}-{kind}", src / "kits" / kind, dirs_exist_ok=True)
        (src / "kits" / "DONE").write_text(time.strftime("%Y-%m-%d %H:%M\n"), encoding="utf-8")
        print("kits", slug, flush=True)


def run_once():
    prepare_drop()
    for slug, job in pending_jobs():
        out = DROP / "drops" / slug
        out.mkdir(parents=True, exist_ok=True)
        for item in job["prompts"]:
            for n in range(job.get("per_prompt", 1)):
                path = out / f"{item['name']}-{n + 1}.png"
                if not path.exists():
                    print("render", path.name, flush=True)
                    path.write_bytes(render(job, item))
        (out / "DONE").write_text(time.strftime("%Y-%m-%d %H:%M") + f" {CKPT}\n", encoding="utf-8")
        if DRIVE_DIR:
            shutil.copytree(out, DRIVE_DIR / slug, dirs_exist_ok=True)
        git("add", "-A", cwd=DROP)
        git("commit", "-q", "-m", f"Drop {slug}", cwd=DROP)
        git("push", "-q", "origin", "HEAD:art-drop", cwd=DROP)
        print("pushed", slug, flush=True)
    kits()


if __name__ == "__main__":
    lock = HERE / "runner.lock"
    if lock.exists() and time.time() - lock.stat().st_mtime < 6 * 3600:
        sys.exit("another run is in progress")
    try:
        queue = comfy("/queue")
    except Exception as e:
        sys.exit(f"ComfyUI not reachable at {COMFY}: {e}")
    if queue.get("queue_running") or queue.get("queue_pending"):
        sys.exit("ComfyUI is busy with another job; trying again next hour")  # one GPU, one job
    lock.touch()
    try:
        run_once()
    finally:
        lock.unlink(missing_ok=True)

# Setting up the ComfyUI PC (once)

This is for the local AI PC (DESKTOP-FOHQGAD, RX 9070 XT, ComfyUI in `E:\AI`).

The weekly cloud run writes image jobs into this repo. `comfy_runner.py` on your
ComfyUI PC picks them up, renders them, copies the images to your Google Drive
folder, and pushes them to the `art-drop` branch so the cloud run can publish.
Nothing on your PC is opened to the internet; the PC only talks to GitHub.

1. Install **Git for Windows** if it isn't there yet. Python is already in `E:\AI\venv`.
2. Open Command Prompt and clone the repo. The first time, a browser window asks
   you to sign in to GitHub; that login is remembered.
   ```
   git clone https://github.com/jintaanunkulpakhin-droid/skill-factory.git E:\skill-factory
   ```
3. Copy `E:\skill-factory\pc\runner.ini.example` to `runner.ini` in the same folder
   and edit it:
   - `checkpoint`: the model file name exactly as ComfyUI lists it.
   - `drive_dir`: leave it as `E:\AI\outputs\thai-art`. That folder already syncs to
     Google Drive > Computers > My Computer > outputs, so images and upload kits show up there.
4. Start ComfyUI (desktop icon "CATOPIA ComfyUI (LAN)"), then test:
   ```
   E:\AI\venv\Scripts\python.exe E:\skill-factory\pc\comfy_runner.py
   ```
   It prints `render ...` for each image and `pushed <slug>` at the end of a job.
5. Run it every hour automatically:
   ```
   schtasks /create /sc hourly /tn SkillFactoryArt /tr "E:\AI\venv\Scripts\python.exe E:\skill-factory\pc\comfy_runner.py"
   ```
   When there's nothing to do, ComfyUI isn't running, or ComfyUI is busy with another job
   (one GPU, one job), it exits in a few seconds and tries again next hour. After a bundle
   is live it also builds the Etsy and Adobe Stock kits (see art/CHANNELS.md).

## Using your own ComfyUI workflow
The default `workflow_sdxl_api.json` is a plain SDXL text-to-image graph. To use
your own: in ComfyUI turn on dev mode options, use **Save (API Format)**, put the
file in `pc\`, and set `workflow =` in runner.ini. In that file replace the
values with these exact placeholders: `%PROMPT%`, `%NEGATIVE%`, `%SEED%`,
`%CKPT%`, `%WIDTH%`, `%HEIGHT%` (any you don't use can be left out). The graph
must end in a SaveImage node.

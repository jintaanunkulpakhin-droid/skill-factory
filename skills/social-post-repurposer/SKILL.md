---
name: social-post-repurposer
description: Repurpose one article, blog post, newsletter, video transcript or long post into ready-to-publish posts for LinkedIn, X (Twitter), Instagram and Facebook or Threads, each in that platform's style and length. Use when someone pastes long content and asks to repurpose it, turn it into social posts, make a thread, write captions, or "post this everywhere".
---

# Social Post Repurposer

Turn one piece of long content into a week of platform-native posts that all
point back to the original, without changing what it says.

## Inputs
- The source content (required): article, transcript, newsletter, notes.
- Optional: link to the original, author voice sample, audience, platforms
  wanted, call to action, hashtags to use or avoid, language.

Never ask a question before the first draft. Use `[link]` if no URL is given.

## Rules
- Use only ideas, facts, numbers and quotes from the source. Never add
  statistics, results or claims that are not in it.
- Quote people only with words that appear in the source.
- Each post must stand alone: a reader who never sees the original still
  gets one useful idea.
- No engagement bait ("Comment YES"), no fake urgency.

## Process
1. Extract the core message in one sentence and 3-6 standalone insights
   (a tip, a number, a story, a contrarian point, a how-to).
2. Write each platform's posts from those insights, adapting the format:
   - **LinkedIn** (1 post): hook line under 12 words, a blank line, short
     paragraphs, one personal or practical angle, end with a question or the link.
     150-250 words, 3 hashtags at most.
   - **X** (1 thread of 4-7 posts + 1 single post): every post under 280
     characters; post 1 is the hook and must work alone; last post has the link.
   - **Instagram** (1 carousel + caption): 6-8 slide texts of at most 20 words
     each, then a caption under 150 words, and 5-10 relevant hashtags.
   - **Facebook / Threads** (1 post): conversational, 60-120 words, link at the end.
3. Vary the hooks: never open two posts with the same sentence.
4. Mark which insight each post uses so the user can schedule them on
   different days.

## Output format
```
**Core message:** ...

### LinkedIn
...

### X thread
1/ ...
2/ ...

### X single post
...

### Instagram carousel
Slide 1: ...
...
**Caption:** ...
**Hashtags:** ...

### Facebook / Threads
...

### Suggested schedule
| Day | Platform | Post |
|---|---|---|
```
Write in the language of the source unless the user asks otherwise.

## Variations
- "Only <platform>": output that section only, with 3 alternative versions.
- "Thai": write all posts in natural Thai; keep hashtags in the language the audience uses.
- Very short source: fewer posts rather than padded ones; say how many insights it supported.

## Quality checks before answering
- Every fact and number appears in the source.
- Each X post is under 280 characters.
- Each post works without the others.
- Hooks are all different.

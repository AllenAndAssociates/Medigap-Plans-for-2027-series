# HANDOFF: "Best Medigap Plans for 2027" video series (Allen & Associates)

Owner: Arric Allen, Allen & Associates Insurance Agency (Medicare / Medigap, Memphis TN).
Last updated: 2026-10-12. Written for Claude Code running in the cloud.

## 1. What this project is
A short-form (9:16, ~60s) video series on Facebook Reels, each with a **comment "GUIDE" to get a free guide** funnel:
comment -> automatic Messenger DM -> opt-in page -> thank-you page + emailed PDF -> tagged lead.

| Part | Topic | Status |
|---|---|---|
| 1 | Plan G explained | Posted. Funnel live. |
| 2 | Plan G vs Plan N (the 2 differences) | Approved and posted 2026-10-09. Comment-to-DM workflow live (untested by Arric as of this handoff). |
| 3 | High-deductible Plan G (planned) | Not started. |

## 2. Repo layout
- `.claude/skills/` all skills used (see section 3). Cloud Claude Code auto-loads project skills from here.
- `part1/video/` HyperFrames project for Part 1: `build.py` generates `index.html`; `measure.py`; `.work/` timings. Pipeline: `python3 measure.py` then `python3 build.py`, then `npx hyperframes@0.8.73 render`.
- `part1/guide/` the lead-magnet PDF source (`guide.html`) and the built PDF `Medigap-Plan-Comparison-Guide-2027-Edition.pdf`.
- `part1/funnel-pages/` HTML copy of the GHL opt-in and thank-you pages. `part1/funnel-comment-guide-to-dm.md` is the full funnel spec (DM copy, page copy, email, workflow spec).
- `part1/heygen/` HeyGen request/response JSON for the Part 1 avatar scenes.
- `part2/final/index.html` full 60s Part 2 composition (reference). `part2/final-a` (0-30s) and `part2/final-b` (30-60s) are the two halves actually rendered (see gotcha 1).
- `part2/covers/` the two earlier full-screen cover compositions (cover-a no longer used; cover-b superseded by the inline cover in `final-b`).
- `part2/thumbnail/thumb.html` thumbnail source. `part2/Facebook-caption-Part2.md` the posted caption.
- `scripts/part-2-plan-n-vs-plan-g.md` the Part 2 script and prompts (written in an earlier session).

**Not in git (too large or secret):** all `.mp4` renders, the original Google Omni clips, `media/` folders, `video/.env`. These exist only on Arric's Mac under
`~/Documents/A/Allen and Associates/Best Medigap Plans for 2027- Part 1 — Medicare Plan G Explained/` (Part 2 inputs in `Part 2/`, final video `Part 2/Part2-Final.mp4`, thumbnail `Part 2/Part2-Thumbnail.png`).
To rebuild Part 2 in the cloud, Arric must upload the 7 original clips again.

## 3. Skills (in `.claude/skills/`)
- `allen-associates-video-style` client style guide and HyperFrames pitfalls (9:16, no music by default, ~0.5-0.75s pauses, brand kit, safe zones, HeyGen/ElevenLabs workflows). **Read first for any video work.**
- `allen-associates-content` captions/ideas in Arric's voice; saves a markdown file.
- HyperFrames family: `hyperframes`, `hyperframes-core`, `-animation`, `-audio`, `-cli`, `-creative`, `-keyframes`, `-registry`, `-studio`, `general-video`, `motion-graphics`, `media-use`, `embedded-captions`, `talking-head-recut`, `music-to-video`, `product-launch-video`, `remotion-to-hyperframes`. If any are stale: `npx hyperframes skills update`.
- `video-use` was a local symlink and is NOT included.

## 4. Brand kit
Blue `#0092d8` (text `#005f96`), green `#5cb128` (text `#3f8a1c`), navy `#0b1622`, paper `#fbfcfa`, red `#e5484d`, gold `#f2b632`. Font Montserrat (variable woff2 at `part1/video/assets/fonts/`). Phone 800-324-9986. Logo `part1/video/assets/images/logo.png`. Keep graphics out of the bottom ~200px (platform UI).

## 5. Accounts, IDs, services (no secrets here)
- **GoHighLevel** location `rum7HnaCy6I4F6pZ2fOu`; domain `medicare.arricallen.com`. Facebook Page: "Allen and Associates Insurance Agency".
  - Funnel steps: opt-in `/get-the-guide` (page slug `/free-medigap-guide`), thank-you `/guide-sent` (page slug `/download-guide`). Old `watch-free-now-7474` and `watch-the-webinar-page-9059` are 404.
  - Workflow **Medigap Guide - Comment to DM (Part 1 Reel)** id `0f2630d3-76fc-44bb-853a-b521aabb6b1c`: trigger = FB comment containing "guide", Page = agency, Post type = published post, Post = the Part 1 post (07-Oct-2026). Action = Facebook interactive messenger DM linking to `/get-the-guide`.
  - Workflow **... (Part 2 Reel)** id `76350448-4609-45c4-ae08-7239937c4329`: duplicate of the above, Post = "Plan G or Plan N? On paper, they look almost ident..." (09-Oct-2026). Published.
  - Workflow **Medigap Guide - Form Submitted** id `e1609a09-6212-4eb3-a752-0014627221ca`: sends the PDF email and tag `medigap-guide-lead`.
  - Each post needs its own duplicated workflow with the Post filter changed (Part 3 will need one too).
- **ElevenLabs**: Arric's cloned voice "Arric Allen", voice_id `3glBps71Sq7dUQi9biZa`. It lives on the account whose key is in the **local** `video/.env`. The key in Arric's shell env is a different account without that voice. Verify with `GET /v2/voices` before use.
  - Re-voicing recipe (keeps lip-sync): `POST /v1/speech-to-speech/{voice_id}` with `model_id=eleven_multilingual_sts_v2`, `voice_settings {"stability":0.6,"similarity_boost":0.9}` on the clip's own audio. Output timing matches input within ~40ms.
  - To fix a bad phrase, generate it with `POST /v1/text-to-speech/{voice_id}` (`eleven_multilingual_v2`, `previous_text` for context) and splice at the right offset with a 40ms crossfade, level-matched.
- **HeyGen**: avatar "Arric Holding a Mic" `f637fbaa33e846dbbe1935b00e4a48a1`; voice `6f09cad7796d4aa0b1458c35a597023f` (details in the video-style skill, pitfall 7).
- **Google Omni**: produced the Part 2 talking-head clips (10s each, 1080x1920, voice generated by Omni, re-voiced with ElevenLabs).
- **Speech recognition used locally**: whisper.cpp (`whisper-cli`) with `ggml-base.en.bin` in `~/whisper-models/`. Use `-ojf` for per-token confidence.

## 6. How Part 2 was built (so it can be repeated for Part 3)
1. Seven 10s Omni clips -> normalized (`libx264 crf18, 30fps, aac 48k stereo`, keyframe every 15 frames).
2. Host stays on screen. AI-garbled text baked into the clips is **covered** with clean HyperFrames cards (white plan cards, navy badges, a navy header card), not regenerated.
3. Scenes at 0/10/20/30/40/50s. Short dip through navy (0.1s in, 0.12s out) at hard cuts (40s and 50s).
4. Last scene (50-60s) is the clean "Commenting_guide" clip covered full-screen by a motion graphic: "Comment GUIDE", guide name, pulsing button, agency disclaimer.
5. All six host clips re-voiced to Arric's voice via ElevenLabs STS; the audio track is assembled separately and muxed onto the rendered video with `ffmpeg -c:v copy`.
6. Render halves separately and join with `ffmpeg -f concat -c copy` (see gotcha 1).

Part 2 spoken lines (transcribed from the originals): 1) "Plan G or Plan N. On paper, they look almost identical. But there are two differences and they decide which one fits you better." 2) "Quick recap from part one, Plan G covers the gaps. Original Medicare leaves, except the Part B deductible. Pay that once a year, and G picks up the rest." 3) "Plan N usually has a lower monthly premium. The trade-off, you still pay the Part B deductible, plus up to $20 at some office visits and up to $50 at the ER." 4) "Difference number two, excess charges. Some doctors can bill up to 15% above Medicare's rate. Plan G covers that. Plan N does not." 5) "Rarely see the doctor and want a lower premium? Plan N may fit. Want predictable costs with no surprise bills? Plan G may fit." 6/7) "Comment 'Guide' and I'll send you my free 2027 side-by-side comparison guide."

## 7. Gotchas that cost real time
1. **HyperFrames render stalls at ~frame 1239** on this 8GB Mac (screenshot capture hangs, deterministic; `--low-memory-mode`, longer protocol timeout, and keyframe re-encode did not fix it). Workaround: split the composition into two 30s halves, render each, concat. Snapshots at the stall time work fine, so it is session length, not content.
2. Clean up after renders: `work-*` folders and `$TMPDIR/hyperframes-extract-cache-501` are large. Disk was nearly full earlier (<1 GB free).
3. In zsh, an unmatched glob in `rm` aborts the whole command; use `find ... -exec rm` or `setopt nonomatch`.
4. Do not trust a tile contact sheet alone to verify segment order; hash-compare frames.
5. GHL builder: the Pages panel -> page "..." -> Edit holds the **URL Path/Slug**. A slug duplicating a funnel step path gets a numeric suffix. Duplicate a workflow from the list view row menu (scroll the table right).
6. When trimming a host clip for a visual cut, trim the audio separately; cutting audio with the picture dropped the last words once.
7. The Omni clips contain AI-garbled on-screen text and a garbled disclaimer in clips 2 and 6. These are in the originals, not caused by editing.

## 8. Decisions already made by Arric (do not re-ask)
- Host stays on screen with floating cards for Plan G and Plan N (not full-screen takeovers).
- Last scene: **no host**, full-screen HyperFrames motion graphic, voice continues underneath.
- Voice: Arric's ElevenLabs clone on all clips.
- An outside editor's notes were pasted several times; Arric's own instructions override them (e.g., the "Plan C covers" note was a misreading: the card says "Plan G covers").

## 9. Open items
1. **Clip 3 script accuracy:** the line "The trade-off, you still pay the Part B deductible" reads like a Plan N downside, but Plan G also leaves the Part B deductible for the enrollee. Arric should review; fixing it means regenerating that audio.
2. **"Currently we represent 9 organizations"** in the disclaimer came from an AEP ad; confirm for Medigap.
3. **Guide naming:** host and slide say "Side-by-Side Comparison Guide"; the PDF and DM say "Medigap Plan Comparison Guide (2027 Edition)". Pick one and align the PDF, DM and pages.
4. **Part 2 DM workflow untested.** Test by commenting "guide" from a second Facebook account, check Messenger and Message requests, then look at the workflow's Execution logs.
5. **Lead attribution:** all leads get tag `medigap-guide-lead`; add a per-video tag (e.g. `medigap-part2`) to see which video converts.
6. **SMS consent wording** on the opt-in form is a draft and needs agency compliance sign-off. Disclaimer text (TPMO) is Arric's: "Allen & Associates Insurance Agency is a non-government entity. We do not offer every plan available in your area. Currently we represent 9 organizations in your area. Please contact Medicare.gov, 1-800-MEDICARE, or your local State Health Insurance Program (SHIP) to get information on all of your options. Not all plans offer all benefits."
7. **Security:** the ElevenLabs key sits in plain text in the local `video/.env` and appeared in a process listing. Rotate it and delete the file. Never commit keys; `.gitignore` excludes `.env`.
8. The Part 1 source now carries the agency disclaimer on its end card, but the Part 1 video was never re-rendered, so check that the posted Part 1 Reel shows the correct end-card line.
9. **Part 3** (high-deductible Plan G): write script in the same 10s-scene format (see `scripts/`), generate clips, reuse this pipeline, duplicate a new DM workflow, add a per-video tag.

## 10. Working agreements
- Arric reviews by watching: always render and send the actual video file after edits.
- Be honest about what cannot be verified (audio cannot be heard; transcripts and confidence scores only).
- Ask before sending messages, publishing outward-facing content, or downloading files. Publishing GHL workflows was explicitly requested by Arric each time.
- Use the video-style skill defaults without being asked again.

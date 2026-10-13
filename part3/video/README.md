# Part 3: High-Deductible Plan G (HyperFrames)

57.95s, 1080x1920, 30fps. Part 2 look: host on screen with white plan cards and navy badges, full-screen Comment GUIDE cover at the end.

## Clips -> scenes
| Scene | Start | Clip (`../clips/`, sorted order) | Trim |
|---|---|---|---|
| 1 Hook | 0.00 | 1 `Man_discussing_high-deductible_P…192046` | 0.15-9.50 |
| 2 What it is | 9.35 | 6 `Man_explaining_insurance_deductible…194346` | 0.30-10.00 |
| 3 After the deductible | 19.05 | 3 `Man_explaining_health_insurance_…192314` | 1.00-9.40 |
| 4 Premium | 27.45 | 2 `Man_discussing_monthly_insurance…192810` | 1.20-7.40 |
| 5 The catch | 33.65 | 4 `Man_explaining_health_insurance_…192935` | 0.15-9.55 |
| 6 Who it fits | 43.05 | 5 `Man_explaining_health_insurance_…193041` | 0.05-7.95 |
| 7 CTA (no host) | 50.95 | 7 `Man_offering_free_comparison_guide…194447` | audio only: 0-2.95 + 4.40-7.42 (drops the stuttered "2027, 2027" and the outro music sting) |

## Build
1. Re-voice each clip with ElevenLabs speech-to-speech (voice "Arric Allen" `3glBps71Sq7dUQi9biZa`, `eleven_multilingual_sts_v2`, stability 0.6, similarity 0.9) into `<sts>/out1..7.mp3` (clip sorted order).
2. `python3 prep.py <sts>` writes `media/s1..s6.mp4` (video only) and `media/voice.wav` (-16 LUFS).
3. `HYPERFRAMES_BROWSER_PATH=/opt/pw-browsers/chromium-1194/chrome-linux/chrome npx hyperframes@0.8.73 render . -o renders/part3-raw.mp4`
4. Mux the voice: `ffmpeg -i renders/part3-raw.mp4 -i media/voice.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -shortest renders/Part3-Final.mp4`

GSAP is vendored in `assets/vendor/` because the render browser here can't reach the CDN.
Graphic cue times in `index.html` are taken from word timestamps of `media/voice.wav` (ElevenLabs Scribe).

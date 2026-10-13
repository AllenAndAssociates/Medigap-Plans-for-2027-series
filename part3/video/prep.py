#!/usr/bin/env python3
"""Part 3 media prep: trim the 7 Omni clips into scene segments and build the voice track.

Inputs:
  ../clips/*.mp4            original Omni clips (in git)
  <sts>/out1..7.mp3         ElevenLabs speech-to-speech re-voice of each clip (Arric Allen voice),
                            numbered in sorted-filename order of ../clips
Outputs (gitignored):
  media/s1..s6.mp4          video-only scene segments, 1080x1920 30fps
  media/voice.wav           full 58.15s voice track, -16 LUFS

Usage: python3 prep.py <sts-dir>
"""
import glob, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CLIPS = sorted(glob.glob(os.path.join(HERE, "..", "clips", "*.mp4")))
STS = sys.argv[1]
MEDIA = os.path.join(HERE, "media")
os.makedirs(MEDIA, exist_ok=True)

# scene -> (clip index in sorted order, in, out). Cuts leave ~0.4-0.65s after the last word.
SCENES = [
    (1, 0.15, 9.50),   # S1 hook: "Everybody talks about Plan G ... High Deductible Plan G."
    (6, 0.30, 10.00),  # S2 what it is: "... two thousand nine hundred and fifty dollars"
    (3, 1.00, 9.40),   # S3 after the deductible: "Once you've paid that deductible ..."
    (2, 1.20, 7.40),   # S4 premium: "The upside? ..."
    (4, 0.15, 9.55),   # S5 the catch
    (5, 0.05, 7.95),   # S6 who it fits
]
# S7 (host off screen): drop the stuttered first "2027," and the outro music sting.
S7_PARTS = [(7, 0.00, 2.95), (7, 4.40, 7.42)]
S7_LEN = 7.0
TARGET_LUFS = -16.0


def run(cmd):
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def lufs(path):
    out = subprocess.run(["ffmpeg", "-i", path, "-af", "ebur128", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    return float(re.findall(r"I:\s+(-?[\d.]+) LUFS", out)[-1])


segs = []
for n, (c, a, b) in enumerate(SCENES, 1):
    run(["ffmpeg", "-y", "-ss", str(a), "-to", str(b), "-i", CLIPS[c - 1], "-an",
         "-vf", "fps=30", "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p",
         "-g", "15", os.path.join(MEDIA, f"s{n}.mp4")])
    segs.append((c, a, b))
segs += S7_PARTS

parts = []
for k, (c, a, b) in enumerate(segs):
    raw = os.path.join(MEDIA, f"_seg{k}.wav")
    run(["ffmpeg", "-y", "-ss", str(a), "-to", str(b), "-i", os.path.join(STS, f"out{c}.mp3"),
         "-af", f"afade=t=in:d=0.015,afade=t=out:st={b - a - 0.04:.3f}:d=0.04",
         "-ac", "2", "-ar", "48000", raw])
    gain = TARGET_LUFS - lufs(raw)
    seg = os.path.join(MEDIA, f"seg{k}.wav")
    run(["ffmpeg", "-y", "-i", raw, "-af", f"volume={gain:.2f}dB", seg])
    os.remove(raw)
    parts.append(seg)

total = sum(b - a for _, a, b in SCENES) + S7_LEN
lst = os.path.join(MEDIA, "parts.txt")
with open(lst, "w") as f:
    f.writelines(f"file '{p}'\n" for p in parts)
run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", lst,
     "-af", f"alimiter=limit=0.89,apad=whole_dur={total:.3f}", "-ar", "48000",
     os.path.join(MEDIA, "voice.wav")])
for p in parts:
    os.remove(p)
os.remove(lst)

t = 0.0
for n, (_, a, b) in enumerate(SCENES, 1):
    print(f"S{n} start {t:.2f} dur {b - a:.2f}")
    t += b - a
print(f"S7 start {t:.2f} dur {S7_LEN:.2f}  total {total:.2f}")

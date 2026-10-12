#!/usr/bin/env python3
"""Measures speech onset/end per HeyGen scene (ffmpeg silencedetect -35dB) and
writes .work/cuts.json. Word timings come from .work/sN.json (hyperframes transcribe).
Run after replacing any media/sceneN.mp4:  python3 measure.py
"""
import json, os, re, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
out = {}
for n in range(1, 7):
    src = os.path.join(HERE, "media", f"scene{n}.mp4")
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", src],
                               capture_output=True, text=True).stdout.strip())
    log = subprocess.run(["ffmpeg", "-i", src, "-af", "silencedetect=noise=-35dB:d=0.05", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    starts = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", log)]
    ends = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", log)]
    onset = ends[0] if starts and starts[0] < 0.02 and ends else 0.0
    end = dur
    if starts and starts[-1] > onset and (len(ends) < len(starts) or ends[-1] >= dur - 0.05):
        end = starts[-1]
    out[n] = {"onset": round(onset, 3), "end": round(end, 3), "dur": round(dur, 3)}
    print(f"scene{n}: onset={onset:.2f} end={end:.2f} dur={dur:.2f}")
with open(os.path.join(HERE, ".work", "cuts.json"), "w") as fh:
    json.dump(out, fh, indent=1)

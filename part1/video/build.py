#!/usr/bin/env python3
"""Builds index.html for "Best Medigap Plans for 2027 - Part 1: Medicare Plan G Explained" (9:16).

Cue times are tied to each HeyGen clip's own word timings:
W(3, "part") = global time the word "deductible" starts in scene 3.
Pipeline:  python3 measure.py  ->  python3 build.py
"""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
WORK = os.path.join(HERE, ".work")
CUTS = {int(k): v for k, v in json.load(open(os.path.join(WORK, "cuts.json"))).items()}

# ---------------------------------------------------------------------------
# Cut list. Series pacing: ~0.5-0.75s breathing pause after each clip's last
# word. Starting each clip at onset-LEAD drops the avatar's settle-in frames.
# ---------------------------------------------------------------------------
LEAD = 0.12
PAUSE = {1: 0.45, 2: 0.65, 3: 0.70, 4: 0.65, 5: 0.65, 6: 0.70}
END_CARD = 4.2

# HeyGen clips end ~0.3s after the last word, so any pause the footage can't
# cover becomes a freeze-hold on the clip's settled last frame (media/holdN.jpg).
starts, ins, durs, holds = {}, {}, {}, {}
t = 0.0
for n in range(1, 7):
    c = CUTS[n]
    m_in = max(0.0, c["onset"] - LEAD)
    want = c["end"] + PAUSE[n]
    m_out = min(c["dur"] - 0.04, want)
    starts[n], ins[n], durs[n] = t, m_in, m_out - m_in
    holds[n] = round(max(0.0, want - m_out), 3) if n < 6 else 0.0
    t += m_out - m_in + holds[n]
MAIN_END = t
TOTAL = MAIN_END + END_CARD


# ---------------------------------------------------------------------------
# Word timings
# ---------------------------------------------------------------------------
def _norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


WORDS = {}
for n in range(1, 7):
    d = json.load(open(os.path.join(WORK, f"s{n}.json")))
    WORDS[n] = [(_norm(w["text"]), w["start"]) for w in d if _norm(w["text"])]


def W(n, word, k=1):
    """Global start time of the k-th occurrence of `word` in scene n."""
    key = _norm(word)
    hits = [s for w, s in WORDS[n] if w == key or w.startswith(key)]
    if len(hits) < k:
        raise SystemExit(f"scene {n}: word {word!r} not found in {[w for w, _ in WORDS[n]]}")
    return round(starts[n] + (hits[k - 1] - ins[n]), 3)


def S(n):
    return round(starts[n], 3)


def E(n):
    """End of scene n's window, including any freeze-hold."""
    return round(starts[n] + durs[n] + holds[n], 3)


def f(x):
    return f"{x:.3f}"


# ---------------------------------------------------------------------------
# Media tracks
# ---------------------------------------------------------------------------
FULLSCREEN = {4}  # scene 4 picture is covered by the full-screen 100% graphic
videos, audios, pushes = [], [], []
for n in range(1, 7):
    common = f'src="media/scene{n}.mp4" data-start="{f(S(n))}" data-duration="{f(durs[n])}" data-media-start="{f(ins[n])}"'
    if n not in FULLSCREEN:
        videos.append(f'<video id="avatar-{n}" class="avatar-video clip" {common} data-track-index="0" muted playsinline></video>')
        pushes.append(f'tl.fromTo("#avatar-{n}", {{ scale: 1 }}, {{ scale: 1.055, duration: {f(durs[n])}, ease: "sine.inOut" }}, {f(S(n))});')
        if holds[n] > 0:
            hs = starts[n] + durs[n]
            videos.append(f'<img id="hold-{n}" class="avatar-video clip" src="media/hold{n}.jpg" alt="" data-start="{f(hs)}" data-duration="{f(holds[n])}" data-track-index="0" />')
            pushes.append(f'tl.set("#hold-{n}", {{ scale: 1.055 }}, {f(hs)});')
    audios.append(f'<audio id="audio-{n}" {common} data-track-index="10" data-volume="1"></audio>')

FS_IN = E(3) - 0.35
FS_OUT = E(4)

ICON_X = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"><line x1="6" y1="6" x2="18" y2="18"/><line x1="18" y1="6" x2="6" y2="18"/></svg>'
ICON_CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="5 12.5 10 17.5 19 7"/></svg>'
ICON_TROPHY = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 21h8"/><path d="M12 17v4"/><path d="M7 4h10v5a5 5 0 0 1-10 0V4z"/><path d="M17 5h3v2a3 3 0 0 1-3 3"/><path d="M7 5H4v2a3 3 0 0 0 3 3"/></svg>'
ICON_SHIELD = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l8 3v6c0 4.5-3.4 8.3-8 9-4.6-.7-8-4.5-8-9V6l8-3z"/><polyline points="8.5 12 11 14.5 15.5 9.5"/></svg>'
ICON_DOC = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><polyline points="14 3 14 8 19 8"/><line x1="9" y1="13" x2="15" y2="13"/><line x1="9" y1="17" x2="13" y2="17"/></svg>'
ICON_CHAT = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/></svg>'
ICON_DOLLAR = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="2.5" x2="12" y2="21.5"/><path d="M17 6.5H9.8a3.2 3.2 0 0 0 0 6.4h4.4a3.2 3.2 0 0 1 0 6.4H6.5"/></svg>'

RING_R = 250
RING_C = 2 * 3.14159265 * RING_R

HTML = f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <title>Best Medigap Plans for 2027 &ndash; Part 1: Medicare Plan G Explained</title>
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <style>
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ margin: 0; width: 1080px; height: 1920px; overflow: hidden; background: #0b1622; }}
      body {{ font-family: "Montserrat", sans-serif; }}

      @font-face {{
        font-family: "Montserrat";
        src: url("assets/fonts/Montserrat-Variable.woff2") format("woff2");
        font-weight: 100 900; font-style: normal; font-display: block;
      }}

      :root {{
        --brand-blue: #0092d8;
        --brand-blue-text: #005f96;
        --brand-green: #5cb128;
        --brand-green-text: #3f8a1c;
        --navy: #0b1622;
        --paper: #fbfcfa;
        --muted: #a9c2d6;
        --red: #e5484d;
        --gold: #f2b632;
      }}

      #root {{ position: relative; width: 1080px; height: 1920px; background: var(--navy); overflow: hidden; }}
      #scene-main {{ position: absolute; inset: 0; }}

      .avatar-video {{
        position: absolute; top: 0; left: 0; width: 100%; height: 100%;
        object-fit: cover; transform-origin: 50% 11%; will-change: transform;
      }}

      #vignette {{
        position: absolute; inset: 0; pointer-events: none;
        background: linear-gradient(to bottom, rgba(6,12,20,0.35) 0%, rgba(6,12,20,0) 14%, rgba(6,12,20,0) 58%, rgba(6,12,20,0.55) 100%);
      }}

      /* ---------- persistent header sticker ---------- */
      #sticker {{ position: absolute; top: 96px; left: 0; right: 0; display: flex; justify-content: center; opacity: 0; }}
      #sticker .badge {{
        display: inline-flex; border-radius: 14px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.35);
        font-weight: 800; font-size: 26px; letter-spacing: 0.05em; text-transform: uppercase; line-height: 1;
      }}
      #sticker .a {{ background: var(--brand-green); color: var(--navy); padding: 20px 26px; }}
      #sticker .b {{ background: var(--navy); color: var(--paper); padding: 20px 26px; border: 2px solid var(--brand-green); border-left: none; border-radius: 0 14px 14px 0; }}

      /* ---------- bottom card system (content kept clear of the bottom ~200px platform-UI band) ---------- */
      .bottom-card {{
        position: absolute; left: 0; right: 0; bottom: 0; min-height: 420px;
        padding: 50px 56px 210px;
        background: rgba(11,22,34,0.92);
        border-top: 5px solid var(--brand-blue);
        border-radius: 32px 32px 0 0;
        display: flex; flex-direction: column; justify-content: center;
      }}
      .kicker-pill {{
        align-self: flex-start; background: var(--brand-green); color: var(--navy);
        font-weight: 800; font-size: 26px; letter-spacing: 0.08em; text-transform: uppercase;
        padding: 12px 20px; border-radius: 10px; margin-bottom: 22px; opacity: 0;
      }}

      /* scene 1: series hook */
      #hook-card .title {{ color: var(--paper); font-weight: 900; font-size: 74px; line-height: 1.06; letter-spacing: -0.02em; }}
      #hook-card .title .ln {{ display: block; opacity: 0; }}
      #hook-card .title .accent {{ color: var(--brand-blue); }}
      #hook-sub {{ margin-top: 24px; display: flex; align-items: center; gap: 16px; opacity: 0; }}
      #hook-sub .name {{ color: var(--paper); font-weight: 800; font-size: 34px; }}
      #hook-sub .dot {{ width: 10px; height: 10px; border-radius: 50%; background: var(--brand-green); }}
      #hook-sub .yrs {{ color: var(--brand-green); font-weight: 800; font-size: 34px; }}
      #since-chip {{
        position: absolute; right: 56px; top: -40px; background: var(--paper); color: var(--navy);
        border-radius: 18px; padding: 14px 22px; text-align: center; box-shadow: 0 14px 36px rgba(0,0,0,0.4); opacity: 0;
      }}
      #since-chip .s1 {{ font-weight: 700; font-size: 22px; letter-spacing: 0.1em; text-transform: uppercase; color: var(--brand-blue-text); }}
      #since-chip .s2 {{ font-weight: 900; font-size: 54px; line-height: 1; letter-spacing: -0.02em; }}

      /* scene 2: Plan G gold standard */
      #pg-title {{ color: var(--paper); font-weight: 900; font-size: 64px; line-height: 1.05; letter-spacing: -0.02em; opacity: 0; }}
      #pg-title .g {{ color: var(--brand-blue); }}
      #pg-badge {{
        margin-top: 28px; display: flex; align-items: center; gap: 22px; padding: 20px 26px; border-radius: 24px;
        background: rgba(242,182,50,0.12); border: 3px solid var(--gold); opacity: 0;
      }}
      #pg-badge .ic {{ flex: none; width: 86px; height: 86px; border-radius: 50%; background: var(--gold); color: var(--navy); display: flex; align-items: center; justify-content: center; }}
      #pg-badge .ic svg {{ width: 50px; height: 50px; }}
      #pg-badge .num {{ color: var(--gold); font-weight: 900; font-size: 46px; line-height: 1; }}
      #pg-badge .lbl {{ margin-top: 6px; color: var(--paper); font-weight: 700; font-size: 32px; }}
      #pg-tag {{
        margin-top: 24px; align-self: flex-start; color: var(--navy); background: var(--paper); font-weight: 800; font-size: 30px;
        padding: 14px 24px; border-radius: 100px; opacity: 0;
      }}
      #pg-tag i {{ font-style: italic; color: var(--brand-blue-text); }}

      /* scene 3: only cost */
      #cost-box {{
        position: relative; display: flex; align-items: center; gap: 28px; padding: 26px 30px; border-radius: 26px;
        background: rgba(0,146,216,0.14); border: 3px solid var(--brand-blue); opacity: 0;
      }}
      #cost-box .ic {{ flex: none; width: 96px; height: 96px; border-radius: 24px; background: var(--brand-blue); color: var(--paper); display: flex; align-items: center; justify-content: center; }}
      #cost-box .ic svg {{ width: 56px; height: 56px; }}
      #cost-box .k {{ color: var(--brand-blue); font-weight: 800; font-size: 26px; letter-spacing: 0.1em; text-transform: uppercase; }}
      #cost-box .v {{ margin-top: 4px; color: var(--paper); font-weight: 900; font-size: 46px; line-height: 1.05; letter-spacing: -0.01em; }}
      #cost-box .amt {{ margin-top: 8px; color: #bfe6fa; font-weight: 700; font-size: 32px; }}
      #cost-box .amt b {{ color: var(--paper); font-weight: 900; }}
      .no-row {{
        position: relative; margin-top: 18px; display: flex; align-items: center; gap: 22px; padding: 18px 24px;
        border-radius: 20px; background: rgba(229,72,77,0.10); border: 2px solid rgba(229,72,77,0.5); opacity: 0;
      }}
      .no-row .ic {{ flex: none; width: 60px; height: 60px; border-radius: 50%; background: var(--red); color: var(--paper); display: flex; align-items: center; justify-content: center; }}
      .no-row .ic svg {{ width: 32px; height: 32px; }}
      .no-row .label {{ position: relative; color: var(--paper); font-weight: 800; font-size: 38px; }}
      .no-row .strike {{ position: absolute; left: -6px; right: -6px; top: 50%; height: 5px; margin-top: -2px; background: var(--red); transform-origin: 0 50%; }}
      .no-row .zero {{ margin-left: auto; color: var(--brand-green); font-weight: 900; font-size: 40px; opacity: 0; }}
      #thats-it {{
        position: absolute; right: 56px; top: -46px; background: var(--brand-green); color: var(--navy);
        font-weight: 900; font-size: 36px; padding: 14px 26px; border-radius: 100px; box-shadow: 0 14px 36px rgba(0,0,0,0.4); opacity: 0;
      }}

      /* scene 4: full-screen 100% coverage */
      #bg-motion {{ position: absolute; inset: 0; background: var(--navy); overflow: hidden; }}
      #bg-motion .blob {{ position: absolute; border-radius: 50%; filter: blur(90px); }}
      #bg-motion .blob.blue1 {{ width: 680px; height: 680px; top: -160px; left: -180px; background: var(--brand-blue); opacity: 0.45; }}
      #bg-motion .blob.green1 {{ width: 620px; height: 620px; bottom: -160px; right: -160px; background: var(--brand-green); opacity: 0.35; }}
      #bg-motion .grid-overlay {{
        position: absolute; inset: 0;
        background-image: linear-gradient(rgba(255,255,255,0.05) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.05) 1px, transparent 1px);
        background-size: 64px 64px;
      }}
      #fs-wrap {{ position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 180px 70px 230px; }}
      #fs-kicker {{ display: flex; align-items: center; gap: 14px; color: var(--paper); font-weight: 700; font-size: 32px; letter-spacing: 0.02em; opacity: 0; }}
      #fs-kicker .pill {{ background: rgba(255,255,255,0.12); border: 2px solid rgba(255,255,255,0.25); padding: 10px 20px; border-radius: 100px; }}
      #fs-kicker .pill s {{ text-decoration-color: var(--red); text-decoration-thickness: 4px; }}
      #ring-wrap {{ position: relative; margin-top: 46px; width: 600px; height: 600px; opacity: 0; }}
      #ring-wrap svg {{ position: absolute; inset: 0; width: 100%; height: 100%; transform: rotate(-90deg); }}
      #ring-center {{ position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; }}
      #pct {{ color: var(--paper); font-weight: 900; font-size: 190px; line-height: 0.9; letter-spacing: -0.05em; }}
      #pct-sym {{ font-size: 110px; color: var(--brand-green); }}
      #pct-lbl {{ margin-top: 10px; color: var(--brand-green); font-weight: 900; font-size: 46px; letter-spacing: 0.12em; }}
      #fs-title {{ margin-top: 44px; color: var(--paper); font-weight: 800; font-size: 46px; line-height: 1.2; text-align: center; opacity: 0; }}
      #fs-title b {{ color: var(--brand-blue); font-weight: 900; }}
      #fs-tags {{ margin-top: 34px; display: flex; gap: 18px; }}
      .fs-tag {{
        display: inline-flex; align-items: center; gap: 12px; background: var(--brand-green); color: var(--navy);
        font-weight: 900; font-size: 34px; padding: 16px 28px; border-radius: 100px; opacity: 0;
      }}
      .fs-tag svg {{ width: 34px; height: 34px; }}

      /* scene 5: who it's for */
      #prem-chip {{
        align-self: flex-start; display: inline-flex; align-items: center; gap: 14px; margin-bottom: 26px;
        background: rgba(242,182,50,0.14); border: 2px solid var(--gold); color: var(--paper);
        font-weight: 700; font-size: 30px; padding: 12px 22px; border-radius: 100px; opacity: 0;
      }}
      #prem-chip b {{ color: var(--gold); font-weight: 900; }}
      #who-title {{ color: var(--paper); font-weight: 900; font-size: 52px; line-height: 1.08; letter-spacing: -0.02em; opacity: 0; }}
      #who-title .g {{ color: var(--brand-blue); }}
      .chk {{ margin-top: 22px; display: flex; align-items: center; gap: 22px; opacity: 0; }}
      .chk .ic {{ flex: none; width: 66px; height: 66px; border-radius: 50%; background: var(--brand-green); color: var(--navy); display: flex; align-items: center; justify-content: center; }}
      .chk .ic svg {{ width: 38px; height: 38px; }}
      .chk .label {{ color: var(--paper); font-weight: 700; font-size: 38px; line-height: 1.15; }}
      .chk .label b {{ font-weight: 900; color: #c9ecb3; }}

      /* scene 6: guide CTA */
      #cta-card {{ border-top-color: var(--brand-green); }}
      #guide-box {{
        display: flex; align-items: center; gap: 26px; padding: 24px 28px; border-radius: 24px;
        background: var(--paper); opacity: 0;
      }}
      #guide-box .ic {{ flex: none; width: 104px; height: 128px; border-radius: 12px; background: var(--brand-blue); color: var(--paper); display: flex; align-items: center; justify-content: center; box-shadow: 8px 8px 0 var(--brand-green); }}
      #guide-box .ic svg {{ width: 62px; height: 62px; }}
      #guide-box .k {{ color: var(--brand-green-text); font-weight: 800; font-size: 26px; letter-spacing: 0.1em; text-transform: uppercase; }}
      #guide-box .v {{ margin-top: 6px; color: var(--navy); font-weight: 900; font-size: 42px; line-height: 1.1; letter-spacing: -0.01em; }}
      #comment-pill {{
        margin-top: 30px; align-self: center; display: inline-flex; align-items: center; gap: 18px;
        background: var(--brand-green); color: var(--navy); font-weight: 900; font-size: 52px; letter-spacing: -0.01em;
        padding: 22px 40px; border-radius: 100px; box-shadow: 0 0 0 0 rgba(92,177,40,0.6); opacity: 0;
      }}
      #comment-pill svg {{ width: 54px; height: 54px; }}
      #comment-pill .q {{ background: var(--navy); color: var(--paper); padding: 4px 18px; border-radius: 12px; }}

      /* end card (paper background so the logo's dark tagline reads) */
      #scene-end {{ position: absolute; inset: 0; background: var(--paper); display: flex; flex-direction: column; align-items: center; justify-content: center; padding-bottom: 160px; }}
      #end-logo {{ width: 880px; height: auto; opacity: 0; }}
      #end-rule {{ margin-top: 56px; width: 140px; height: 6px; border-radius: 3px; background: var(--brand-green); transform-origin: 50% 50%; }}
      #end-phone {{ margin-top: 48px; color: var(--navy); font-weight: 900; font-size: 68px; letter-spacing: -0.01em; opacity: 0; }}
      #end-site {{ margin-top: 18px; color: var(--brand-blue-text); font-weight: 800; font-size: 46px; letter-spacing: -0.01em; opacity: 0; }}
      #end-cta {{
        margin-top: 48px; display: inline-flex; align-items: center; gap: 14px; background: var(--navy); color: var(--paper);
        font-weight: 800; font-size: 36px; padding: 18px 32px; border-radius: 100px; opacity: 0;
      }}
      #end-cta b {{ color: var(--brand-green); font-weight: 900; }}
      #end-disc {{ position: absolute; left: 70px; right: 70px; bottom: 230px; text-align: center; color: #56606b; font-weight: 500; font-size: 22px; line-height: 1.35; opacity: 0; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{f(TOTAL)}" data-width="1080" data-height="1920">
      <div id="scene-main">
        {chr(10).join('        ' + v for v in videos).strip()}

        <!-- scene 4: full-screen 100% coverage graphic (narration keeps playing via #audio-4) -->
        <div id="bg-motion" class="clip" data-start="{f(FS_IN)}" data-duration="{f(FS_OUT - FS_IN)}" data-track-index="1" data-layout-allow-overflow="true">
          <div class="blob blue1"></div>
          <div class="blob green1"></div>
          <div class="grid-overlay"></div>
        </div>
        <div id="fs-wrap" class="clip" data-start="{f(FS_IN)}" data-duration="{f(FS_OUT - FS_IN)}" data-track-index="2">
          <div id="fs-kicker"><span class="pill">After the Part B deductible</span></div>
          <div id="ring-wrap">
            <svg viewBox="0 0 600 600">
              <circle cx="300" cy="300" r="{RING_R}" fill="none" stroke="rgba(255,255,255,0.10)" stroke-width="36" />
              <circle id="ring" cx="300" cy="300" r="{RING_R}" fill="none" stroke="#5cb128" stroke-width="36" stroke-linecap="round"
                stroke-dasharray="{RING_C:.1f}" stroke-dashoffset="{RING_C:.1f}" />
            </svg>
            <div id="ring-center">
              <div id="pct"><span id="pct-num">0</span><span id="pct-sym">%</span></div>
              <div id="pct-lbl">COVERAGE</div>
            </div>
          </div>
          <div id="fs-title">On all <b>Medicare-approved</b><br />hospital &amp; medical bills</div>
          <div id="fs-tags">
            <div class="fs-tag" id="fs-tag1">{ICON_SHIELD}<span>Zero Surprise Bills</span></div>
          </div>
        </div>

        <div id="vignette"></div>

        <!-- persistent header sticker -->
        <div id="sticker" class="clip" data-start="0" data-duration="{f(MAIN_END)}" data-track-index="5">
          <div class="badge"><span class="a">Best Medigap Plans 2027</span><span class="b">Part 1 &middot; Plan G</span></div>
        </div>

        <!-- scene 1: series hook & persona -->
        <div id="hook-card" class="bottom-card clip" data-start="{f(S(1))}" data-duration="{f(E(1) - S(1))}" data-track-index="3">
          <div id="since-chip"><div class="s1">In business since</div><div class="s2">1994</div></div>
          <div class="kicker-pill" id="hook-kicker">Part 1</div>
          <div class="title"><span class="ln" id="hook-l1">The Best Medigap Plans</span><span class="ln accent" id="hook-l2">for 2027</span></div>
          <div id="hook-sub"><span class="name">Arric Allen</span><span class="dot"></span><span class="yrs">30+ Years Experience</span></div>
        </div>

        <!-- scene 2: Plan G gold standard -->
        <div id="pg-card" class="bottom-card clip" data-start="{f(S(2))}" data-duration="{f(E(2) - S(2))}" data-track-index="3">
          <div id="pg-title">Medicare Supplement<br /><span class="g">Plan G</span></div>
          <div id="pg-badge">
            <div class="ic">{ICON_TROPHY}</div>
            <div><div class="num">#1 Most Popular</div><div class="lbl">Medigap plan nationwide</div></div>
          </div>
          <div id="pg-tag">The <i>&ldquo;Cadillac&rdquo;</i> of Medicare Supplements</div>
        </div>

        <!-- scene 3: only cost = Part B deductible -->
        <div id="cost-card" class="bottom-card clip" data-start="{f(S(3))}" data-duration="{f(E(3) - S(3))}" data-track-index="3">
          <div id="thats-it">2027 amount pending</div>
          <div id="cost-box">
            <div class="ic">{ICON_DOLLAR}</div>
            <div>
              <div class="k">Your only cost</div>
              <div class="v">Part B Annual Deductible</div>
              <div class="amt"><b>$283</b> a year &middot; 2026 amount</div>
            </div>
          </div>
          <div class="no-row" id="no-1"><div class="ic">{ICON_X}</div><div class="label">Doctor copays<span class="strike"></span></div><div class="zero">$0</div></div>
          <div class="no-row" id="no-2"><div class="ic">{ICON_X}</div><div class="label">Hospital deductibles<span class="strike"></span></div><div class="zero">$0</div></div>
        </div>

        <!-- scene 5: who Plan G is perfect for -->
        <div id="who-card" class="bottom-card clip" data-start="{f(S(5))}" data-duration="{f(E(5) - S(5))}" data-track-index="3">
          <div id="prem-chip">Most complete coverage = <b>higher premium</b></div>
          <div id="who-title">Who should choose <span class="g">Plan G?</span></div>
          <div class="chk" id="chk-1"><div class="ic">{ICON_CHECK}</div><div class="label">Sees doctors or <b>specialists</b> often</div></div>
          <div class="chk" id="chk-2"><div class="ic">{ICON_CHECK}</div><div class="label">Wants fixed, <b>predictable</b> budgeting</div></div>
          <div class="chk" id="chk-3"><div class="ic">{ICON_CHECK}</div><div class="label"><b>&ldquo;Set-it-and-forget-it&rdquo;</b> peace of mind</div></div>
        </div>

        <!-- scene 6: guide CTA -->
        <div id="cta-card" class="bottom-card clip" data-start="{f(S(6))}" data-duration="{f(E(6) - S(6))}" data-track-index="3">
          <div class="kicker-pill" id="cta-kicker">Free Resource</div>
          <div id="guide-box">
            <div class="ic">{ICON_DOC}</div>
            <div><div class="k">Free download &middot; 2027 Edition</div><div class="v">Medigap Plan Comparison Guide <span style="color:var(--brand-green-text)">+ rate check</span></div></div>
          </div>
          <div id="comment-pill">{ICON_CHAT}<span>Comment <span class="q">GUIDE</span> below</span></div>
        </div>

        {chr(10).join('        ' + a for a in audios).strip()}
      </div>

      <!-- end card: agency outro -->
      <div id="scene-end" class="clip" data-start="{f(MAIN_END)}" data-duration="{f(END_CARD)}" data-track-index="4">
        <img id="end-logo" src="assets/images/logo.png" alt="Allen &amp; Associates Insurance Agency &mdash; Making Medicare Easy" />
        <div id="end-rule"></div>
        <div id="end-phone">800-324-9986</div>
        <div id="end-site">allenandassociates.agency</div>
        <div id="end-cta">Comment <b>&ldquo;GUIDE&rdquo;</b> for your free guide + rate check</div>
        <div id="end-disc">Allen &amp; Associates Insurance Agency is a non-government entity. We do not offer every plan available in your area. Currently we represent 9 organizations in your area. Please contact Medicare.gov, 1-800-MEDICARE, or your local State Health Insurance Program (SHIP) to get information on all of your options. Not all plans offer all benefits.</div>
      </div>
    </div>

    <script>
      window.__timelines = window.__timelines || {{}};
      const tl = gsap.timeline({{ paused: true }});

      /* subtle push-ins anchored at the measured hairline */
      {chr(10).join('      ' + p for p in pushes).strip()}

      /* header sticker */
      tl.fromTo("#sticker", {{ opacity: 0, y: -18 }}, {{ opacity: 1, y: 0, duration: 0.5, ease: "power3.out" }}, 0.2);
      tl.to("#sticker", {{ opacity: 0, duration: 0.3 }}, {f(MAIN_END - 0.3)});

      /* scene 1: hook */
      tl.fromTo("#hook-card", {{ yPercent: 100 }}, {{ yPercent: 0, duration: 0.55, ease: "power3.out" }}, 0.0);
      tl.fromTo("#hook-kicker", {{ opacity: 0, x: -20 }}, {{ opacity: 1, x: 0, duration: 0.4, ease: "power2.out" }}, 0.35);
      tl.fromTo("#hook-sub", {{ opacity: 0, y: 14 }}, {{ opacity: 1, y: 0, duration: 0.45, ease: "power3.out" }}, {W(1, "am")});
      tl.fromTo("#since-chip", {{ opacity: 0, scale: 0.6, rotation: -6 }}, {{ opacity: 1, scale: 1, rotation: 0, duration: 0.55, ease: "back.out(2)" }}, {W(1, "since")});
      tl.fromTo("#hook-l1", {{ opacity: 0, y: 22 }}, {{ opacity: 1, y: 0, duration: 0.5, ease: "power3.out" }}, {W(1, "best")});
      tl.fromTo("#hook-l2", {{ opacity: 0, y: 22 }}, {{ opacity: 1, y: 0, duration: 0.5, ease: "power3.out" }}, {W(1, "plans")});
      tl.to("#hook-card", {{ opacity: 0, y: 30, duration: 0.3, ease: "power2.in" }}, {f(E(1) - 0.3)});

      /* scene 2: Plan G */
      tl.fromTo("#pg-card", {{ yPercent: 100 }}, {{ yPercent: 0, duration: 0.5, ease: "power3.out" }}, {S(2)});
      tl.fromTo("#pg-title", {{ opacity: 0, y: 22 }}, {{ opacity: 1, y: 0, duration: 0.5, ease: "power3.out" }}, {W(2, "Medicare")});
      tl.fromTo("#pg-badge", {{ opacity: 0, x: -40 }}, {{ opacity: 1, x: 0, duration: 0.5, ease: "power3.out" }}, {W(2, "popular")});
      tl.fromTo("#pg-badge .ic", {{ rotation: -20, scale: 0.6 }}, {{ rotation: 0, scale: 1, duration: 0.7, ease: "elastic.out(1, 0.5)" }}, {W(2, "popular")});
      tl.fromTo("#pg-tag", {{ opacity: 0, scale: 0.9 }}, {{ opacity: 1, scale: 1, duration: 0.45, ease: "back.out(1.7)" }}, {W(2, "comprehensive")});
      tl.to("#pg-card", {{ opacity: 0, y: 30, duration: 0.3, ease: "power2.in" }}, {f(E(2) - 0.3)});

      /* scene 3: only cost */
      tl.fromTo("#cost-card", {{ yPercent: 100 }}, {{ yPercent: 0, duration: 0.5, ease: "power3.out" }}, {S(3)});
      tl.fromTo("#cost-box", {{ opacity: 0, y: 20 }}, {{ opacity: 1, y: 0, duration: 0.5, ease: "power3.out" }}, {W(3, "only")});
      tl.to("#cost-box", {{ scale: 1.04, duration: 0.25, yoyo: true, repeat: 1, ease: "power1.inOut" }}, {W(3, "part")});
      tl.fromTo("#no-1", {{ opacity: 0, x: -30 }}, {{ opacity: 1, x: 0, duration: 0.4, ease: "power3.out" }}, {f(W(3, "part") + 0.9)});
      tl.fromTo("#no-2", {{ opacity: 0, x: -30 }}, {{ opacity: 1, x: 0, duration: 0.4, ease: "power3.out" }}, {f(W(3, "part") + 1.15)});
      tl.fromTo("#no-1 .strike", {{ scaleX: 0 }}, {{ scaleX: 1, duration: 0.35, ease: "power2.inOut" }}, {W(3, "2026")});
      tl.fromTo("#no-2 .strike", {{ scaleX: 0 }}, {{ scaleX: 1, duration: 0.35, ease: "power2.inOut" }}, {f(W(3, "2026") + 0.18)});
      tl.fromTo(".no-row .zero", {{ opacity: 0, scale: 0.6 }}, {{ opacity: 1, scale: 1, duration: 0.35, ease: "back.out(2)", stagger: 0.18 }}, {f(W(3, "2026") + 0.25)});
      tl.fromTo("#thats-it", {{ opacity: 0, scale: 0.5 }}, {{ opacity: 1, scale: 1, duration: 0.45, ease: "back.out(2.2)" }}, {W(3, "that")});

      /* 3 -> 4 kinetic wipe into full-screen 100% */
      tl.to("#cost-card", {{ xPercent: -100, duration: 0.45, ease: "power3.in" }}, {f(FS_IN - 0.05)});
      tl.fromTo("#bg-motion", {{ clipPath: "inset(0% 0% 0% 100%)" }}, {{ clipPath: "inset(0% 0% 0% 0%)", duration: 0.55, ease: "power3.inOut" }}, {f(FS_IN)});
      tl.fromTo("#fs-wrap", {{ clipPath: "inset(0% 0% 0% 100%)" }}, {{ clipPath: "inset(0% 0% 0% 0%)", duration: 0.55, ease: "power3.inOut" }}, {f(FS_IN)});

      /* scene 4: 100% ring */
      tl.fromTo("#bg-motion .blob.blue1", {{ x: 0, y: 0 }}, {{ x: 90, y: 70, duration: {f(FS_OUT - FS_IN)}, ease: "sine.inOut" }}, {f(FS_IN)});
      tl.fromTo("#bg-motion .blob.green1", {{ x: 0, y: 0 }}, {{ x: -80, y: -60, duration: {f(FS_OUT - FS_IN)}, ease: "sine.inOut" }}, {f(FS_IN)});
      tl.fromTo("#fs-kicker", {{ opacity: 0, y: -12 }}, {{ opacity: 1, y: 0, duration: 0.45, ease: "power2.out" }}, {f(max(FS_IN + 0.35, W(4, "deductible") - 0.3))});
      tl.fromTo("#ring-wrap", {{ opacity: 0, scale: 0.85 }}, {{ opacity: 1, scale: 1, duration: 0.55, ease: "power3.out" }}, {W(4, "all")});
      const RING_START = {W(4, "covered", 2)};
      const RING_END = {W(4, "100")};
      tl.fromTo("#ring", {{ attr: {{ "stroke-dashoffset": {RING_C:.1f} }} }}, {{ attr: {{ "stroke-dashoffset": 0 }}, duration: RING_END - RING_START, ease: "power2.inOut" }}, RING_START);
      const cnt = {{ v: 0 }};
      tl.to(cnt, {{ v: 100, duration: RING_END - RING_START, ease: "power2.inOut", onUpdate: () => {{ document.getElementById("pct-num").textContent = Math.round(cnt.v); }} }}, RING_START);
      tl.to("#ring-wrap", {{ scale: 1.06, duration: 0.25, yoyo: true, repeat: 1, ease: "power1.inOut" }}, RING_END);
      tl.fromTo("#fs-title", {{ opacity: 0, y: 16 }}, {{ opacity: 1, y: 0, duration: 0.5, ease: "power3.out" }}, {W(4, "hospital")});
      tl.fromTo("#fs-tag1", {{ opacity: 0, scale: 0.8 }}, {{ opacity: 1, scale: 1, duration: 0.45, ease: "back.out(2)" }}, {f(W(4, "100") + 0.35)});
      tl.to(["#fs-wrap", "#bg-motion"], {{ opacity: 0, duration: 0.3, ease: "power2.in" }}, {f(FS_OUT - 0.3)});

      /* scene 5: who it's for */
      tl.fromTo("#who-card", {{ yPercent: 100 }}, {{ yPercent: 0, duration: 0.5, ease: "power3.out" }}, {S(5)});
      tl.fromTo("#prem-chip", {{ opacity: 0, x: -20 }}, {{ opacity: 1, x: 0, duration: 0.4, ease: "power2.out" }}, {W(5, "premiums")});
      tl.fromTo("#who-title", {{ opacity: 0, y: 18 }}, {{ opacity: 1, y: 0, duration: 0.45, ease: "power3.out" }}, {W(5, "perfect")});
      tl.fromTo("#chk-1", {{ opacity: 0, x: -30 }}, {{ opacity: 1, x: 0, duration: 0.4, ease: "power3.out" }}, {W(5, "doctors")});
      tl.fromTo("#chk-2", {{ opacity: 0, x: -30 }}, {{ opacity: 1, x: 0, duration: 0.4, ease: "power3.out" }}, {W(5, "predictable")});
      tl.fromTo("#chk-3", {{ opacity: 0, x: -30 }}, {{ opacity: 1, x: 0, duration: 0.4, ease: "power3.out" }}, {W(5, "costs")});
      tl.fromTo(".chk .ic", {{ scale: 0.4 }}, {{ scale: 1, duration: 0.45, ease: "back.out(2.4)", stagger: {{ each: 0 }} }}, {W(5, "doctors")});
      tl.to("#who-card", {{ opacity: 0, y: 30, duration: 0.3, ease: "power2.in" }}, {f(E(5) - 0.3)});

      /* scene 6: guide CTA */
      tl.fromTo("#cta-card", {{ yPercent: 100 }}, {{ yPercent: 0, duration: 0.5, ease: "power3.out" }}, {S(6)});
      tl.fromTo("#cta-kicker", {{ opacity: 0, x: -20 }}, {{ opacity: 1, x: 0, duration: 0.4, ease: "power2.out" }}, {f(S(6) + 0.3)});
      tl.fromTo("#guide-box", {{ opacity: 0, y: 20 }}, {{ opacity: 1, y: 0, duration: 0.5, ease: "power3.out" }}, {W(6, "compare")});
      tl.fromTo("#guide-box .ic", {{ rotation: -10, y: 10 }}, {{ rotation: 0, y: 0, duration: 0.7, ease: "elastic.out(1, 0.5)" }}, {W(6, "compare")});
      tl.fromTo("#comment-pill", {{ opacity: 0, scale: 0.7 }}, {{ opacity: 1, scale: 1, duration: 0.5, ease: "back.out(2)" }}, {W(6, "comment")});
      tl.to("#comment-pill", {{ scale: 1.06, duration: 0.3, yoyo: true, repeat: 3, ease: "sine.inOut" }}, {f(W(6, "comment") + 0.8)});

      /* end card */
      tl.fromTo("#scene-end", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.35, ease: "power1.out" }}, {f(MAIN_END)});
      tl.fromTo("#end-logo", {{ opacity: 0, scale: 0.94, y: 16 }}, {{ opacity: 1, scale: 1, y: 0, duration: 0.6, ease: "power2.out" }}, {f(MAIN_END + 0.2)});
      tl.fromTo("#end-rule", {{ scaleX: 0 }}, {{ scaleX: 1, duration: 0.5, ease: "power2.out" }}, {f(MAIN_END + 0.6)});
      tl.fromTo("#end-phone", {{ opacity: 0, y: 12 }}, {{ opacity: 1, y: 0, duration: 0.5, ease: "power2.out" }}, {f(MAIN_END + 0.8)});
      tl.fromTo("#end-site", {{ opacity: 0, y: 12 }}, {{ opacity: 1, y: 0, duration: 0.5, ease: "power2.out" }}, {f(MAIN_END + 1.0)});
      tl.fromTo("#end-cta", {{ opacity: 0, scale: 0.9 }}, {{ opacity: 1, scale: 1, duration: 0.5, ease: "back.out(1.8)" }}, {f(MAIN_END + 1.3)});
      tl.fromTo("#end-disc", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.5 }}, {f(MAIN_END + 1.6)});

      window.__timelines["main"] = tl;
      tl.seek(0);
    </script>
  </body>
</html>
"""

with open(os.path.join(HERE, "index.html"), "w") as fh:
    fh.write(HTML)
print(f"wrote index.html  total={TOTAL:.2f}s  main_end={MAIN_END:.2f}s")
for n in range(1, 7):
    print(f"  scene{n}: start={S(n):6.2f}  in={ins[n]:.2f}  dur={durs[n]:.2f}  hold={holds[n]:.2f}")

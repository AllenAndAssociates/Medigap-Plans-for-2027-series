# Medigap Part 3: High-Deductible Plan G

7 scenes, each 10 seconds or shorter, about 60s total. Same comment-GUIDE funnel as Parts 1 and 2.

How it's split:
- **Google Omni** generates only the talking head: one clip per scene, presenter speaking the line. No text or graphics.
- **Claude Code (HyperFrames)** builds all motion graphics, cutaways and the end card on top of the Omni clips. Follow the `allen-associates-video-style` skill for colors, fonts, pacing and safe zones.
- **ElevenLabs** re-voices each clip to Arric's voice (speech-to-speech), same as Part 2.

---

## Part A: Google Omni talking-head prompts

### Base prompt (paste at the start of every scene)

Vertical 9:16 talking-head video. A friendly, professional Medicare advisor in his 40s, navy blazer, open-collar white shirt. Seated, framed from mid-chest up, centered, with his head in the middle third of the frame and clear space above his head. Locked-off camera, no camera movement, no zoom. Softly blurred bright modern office background. Even, soft front lighting. He speaks directly into the camera in a calm, warm, confident, conversational tone with natural small head movements. No text, captions, logos, graphics or on-screen elements.

(If Omni accepts a reference image, use the same headshot of Arric for every scene. Keep framing, wardrobe and background identical across all 7 clips, and matching Part 2, so the series looks consistent.)

### Scene 1 (8s)
[Base prompt] He says: "What if you could get Plan G coverage for a much lower premium? It's called High-Deductible Plan G. But there's a catch." Slight raise of the eyebrows on "there's a catch." 8 seconds.

### Scene 2 (9s)
[Base prompt] He says: "It covers the same things as Plan G, after a yearly deductible. In 2027, that deductible is three thousand fifty dollars." Calm, clear emphasis on the dollar amount. 9 seconds.

### Scene 3 (9s)
[Base prompt] He says: "Until you reach it, you pay your share of Medicare-approved costs. Once you do, it works just like regular Plan G." Small open-hand gesture on "just like regular Plan G." 9 seconds.

### Scene 4 (8s)
[Base prompt] He says: "So why pick it? The monthly premium is usually much lower than regular Plan G." Small reassuring nod at the end. 8 seconds.

### Scene 5 (10s)
[Base prompt] He says: "Here's the math. In a healthy year, you mostly pay that low premium. In a rough year, you pay up to the deductible, then you're covered." Holds up one hand on "healthy year," the other on "rough year." 10 seconds.

### Scene 6 (10s)
[Base prompt] He says: "It may fit if you're healthy and have savings for the deductible. One heads-up: switching to regular Plan G later may mean health questions." Slight lean toward the camera on "one heads-up." 10 seconds.

### Scene 7 (7s)
[Base prompt] He says: "Comment GUIDE, and I'll send you my free 2027 Medigap comparison guide." Smiles and points down toward the bottom of the frame, then nods. 7 seconds.

---

## Part B: HyperFrames motion graphics (built in Claude Code)

Times are from the start of each clip and approximate. Re-time to the word timestamps from the actual audio. Host stays on screen with floating cards (Part 2 style), except the last scene, which is a full-screen motion graphic with the voice underneath. Keep everything out of the bottom ~200px.

### Scene 1: Hook (0:00–0:08)
- **Layout:** Talking head full frame. Cards in the top third.
- **0.0s:** White "Plan G" card slides in from the left with a price tag; a second card labelled "Plan G" with a smaller price tag slides in from the right and the tag shrinks with a down arrow. No dollar figures.
- **4.0s, on "High-Deductible Plan G":** Navy header card: "High-Deductible Plan G."
- **6.5s, on "there's a catch":** Gold "The catch?" badge pops in under the header.

### Scene 2: What it is (0:08–0:17)
- **Layout:** Talking head full frame. Card in the top third.
- **0.5s, on "same things as Plan G":** Plan G card with 4 green ticks (Hospital coinsurance, Part B coinsurance, Skilled nursing, Excess charges), same design as Part 2 scene 2.
- **4.0s, on "after a yearly deductible":** A navy bar slides across the top of the card: "After a yearly deductible."
- **6.0s, on "three thousand fifty dollars":** Counter rolls up to "$3,050" with a small "2027" tag.

### Scene 3: How it works (0:17–0:26)
- **Full-screen cutaway, 0.5–7.0s** (voice continues): a horizontal meter fills from $0 to $3,050. Left of the marker labelled "You pay your share" (gold). At the marker, a green "Plan G kicks in" stamp; the bar beyond it turns green, labelled "Covered like Plan G."
- **7.0s, on "just like regular Plan G":** Cut back to the talking head with a small green "= Plan G" badge top left.

### Scene 4: Premium (0:26–0:34)
- **Layout:** Talking head full frame. Two cards in the top third.
- **0.5s:** "Regular Plan G" card with a tall premium bar.
- **3.0s, on "much lower":** "High-Deductible G" card with a short bar; label "Lower monthly premium (usually)." No dollar figures (premiums vary by state, age, ZIP and carrier).

### Scene 5: The math (0:34–0:44)
- **Layout:** Talking head full frame. Split card in the top third, matched to his hand gestures (check the clip and swap sides if needed).
- **1.0s, on "healthy year":** Green card: "Healthy year: mostly just the low premium."
- **5.0s, on "rough year":** Gold card: "Rough year: up to $3,050, then covered."

### Scene 6: Who it fits (0:44–0:54)
- **Layout:** Talking head full frame. Card in the top third.
- **0.5s, on "healthy":** Checklist ticks in: "Generally healthy" ✓, "Savings for the deductible" ✓.
- **5.0s, on "one heads-up":** Red-outlined note slides in under the checklist: "Switching to regular G later may require health questions."

### Scene 7: Call to action (0:54–1:01), full-screen motion graphic
- Same as Part 2's last scene: no host, full-screen "Comment GUIDE," guide name, pulsing button, agency disclaimer. Voice continues underneath.

---

## Reel caption

High-Deductible Plan G: same coverage as Plan G, for a lower monthly premium. The catch is a yearly deductible.

1. In 2027, you pay up to $3,050 of Medicare-approved costs yourself. After that, it works just like regular Plan G.
2. In a healthy year, you mostly pay the lower premium. In a rough year, you pay up to the deductible, then you're covered.
3. It may fit if you're generally healthy and have savings to cover the deductible. Switching to regular Plan G later may mean answering health questions.

Comment "GUIDE" and I'll send you my free 2027 Medigap comparison guide.

Allen & Associates Insurance Agency is a non-government entity. We do not offer every plan available in your area. Currently we represent 9 organizations in your area. Please contact Medicare.gov, 1-800-MEDICARE, or your local State Health Insurance Program (SHIP) to get information on all of your options. Not all plans offer all benefits.

#Medicare #Medigap #PlanG #HighDeductiblePlanG #MedicareSupplement #Turning65

## Production notes

- **Confirm the $3,050 figure against CMS before recording.** Several industry sources report CMS set the 2027 high-deductible Plan F/G deductible at $3,050 (up from $2,950 in 2026), but I couldn't find the CMS notice itself. If it differs, change scene 2, the scene 2 and 5 graphics, and the caption.
- **The PDF guide still shows the 2026 figure** ("high-deductible Plan G $2,950 ... may change for 2027"). Update `part1/guide/guide.html` to $3,050 and rebuild the PDF before this Reel goes live, so the guide the DM sends matches the video.
- Scene 3 says "your share of Medicare-approved costs." The Part B deductible counts toward the high deductible, so don't add a separate Part B deductible line here (avoids the Part 2 clip 3 wording problem).
- Premiums vary by state, age, ZIP code and carrier, so keep "usually" in scene 4 and show no premium figures.
- Not every carrier offers High-Deductible Plan G in every state. Massachusetts, Minnesota and Wisconsin use their own standardized Medigap plans.
- Health questions on a later switch: most states allow medical underwriting outside open enrollment and guaranteed-issue situations; a few states have their own rules. Keep the "may" in scene 6.
- Guide name: the CTA says "2027 Medigap comparison guide," same as the Part 2 script. Align with whatever name is picked for the open guide-naming item.
- Funnel: duplicate the Part 2 comment-to-DM workflow, set the Post filter to the Part 3 post, and add a per-video tag (e.g. `medigap-part3`).
- Get compliance review before posting.

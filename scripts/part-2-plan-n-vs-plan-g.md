# Medigap Part 2: Plan N vs Plan G

7 scenes, each 10 seconds or shorter, about 59s total. Same comment-GUIDE funnel as Part 1.

How it's split:
- **Google Omni** generates only the talking head: one clip per scene, presenter speaking the line. No text or graphics.
- **Claude Code (HyperFrames)** builds all motion graphics, captions, cutaways and the end card on top of the Omni clips. Follow the `allen-associates-video-style` skill for colors, fonts and caption style.

---

## Part A: Google Omni talking-head prompts

### Base prompt (paste at the start of every scene)

Vertical 9:16 talking-head video. A friendly, professional Medicare advisor in his 40s, navy blazer, open-collar white shirt. Seated, framed from mid-chest up, centered, with his head in the middle third of the frame and clear space above his head. Locked-off camera, no camera movement, no zoom. Softly blurred bright modern office background. Even, soft front lighting. He speaks directly into the camera in a calm, warm, confident, conversational tone with natural small head movements. No text, captions, logos, graphics or on-screen elements.

(If Omni accepts a reference image, use the same headshot of Arric for every scene. Keep framing, wardrobe and background identical across all 7 clips so the cuts match.)

### Scene 1 (8s)
[Base prompt] He says: "Plan G or Plan N? They look almost identical. But two differences decide which one fits you." Slight lean toward the camera on "two differences." 8 seconds.

### Scene 2 (9s)
[Base prompt] He says: "Quick recap. Plan G covers Medicare's gaps, except the Part B deductible. Pay that once, and G covers the rest." Reassuring nod at the end. 9 seconds.

### Scene 3 (8s)
[Base prompt] He says: "Plan N usually costs less each month. You still pay the Part B deductible, just like Plan G." 8 seconds.

### Scene 4 (9s)
[Base prompt] He says: "Difference one: copays. Plan N may charge up to twenty dollars per office visit, and up to fifty at the ER." Holds up one finger on "Difference one." 9 seconds.

### Scene 5 (9s)
[Base prompt] He says: "Difference two: excess charges. Some doctors bill up to fifteen percent above Medicare's rate. Plan G covers it. N doesn't." Holds up two fingers on "Difference two." 9 seconds.

### Scene 6 (9s)
[Base prompt] He says: "Rarely see the doctor and want a lower premium? Plan N may fit. Want predictable costs? Plan G may fit." Small open-hand gesture to his left on the Plan N line and to his right on the Plan G line. 9 seconds.

### Scene 7 (7s)
[Base prompt] He says: "Comment GUIDE, and I'll send you my free 2027 Medigap comparison guide." Smiles and points down toward the bottom of the frame, then nods. 7 seconds.

---

## Part B: HyperFrames motion graphics (built in Claude Code)

Times are from the start of each clip and approximate. Re-time to the word timestamps from the actual Omni audio.

Layers in every scene: Omni clip (base) → graphics → word-by-word captions in the lower third.

### Scene 1: Hook (0:00–0:08)
- **Layout:** Talking head full frame. Graphics in the top third.
- **0.0s:** "Plan G" card slides in from the left, "Plan N" card from the right, with a "vs" badge popping between them.
- **4.5s, on "two differences":** Cards shrink up. Title "The 2 differences that matter" types on beneath them.

### Scene 2: Plan G recap (0:08–0:17)
- **Layout:** Talking head shifts to the lower half (scale down and slide). Plan G panel in the top half.
- **0.5s:** "Plan G" header, then a checklist of 4 items ticks green one by one: Hospital coinsurance, Part B coinsurance, Skilled nursing, Excess charges.
- **3.5s, on "except the Part B deductible":** A fifth line appears with an amber marker: "Part B deductible: you pay."
- **6.5s, on "G covers the rest":** Panel gets a green "Covered" stamp.

### Scene 3: Plan N premium (0:17–0:25)
- **Layout:** Same split as scene 2, with the Plan N panel in the top half.
- **0.5s:** "Plan N" header. A premium price tag drops in and shrinks with a down arrow. Label: "Lower monthly premium (usually)." No dollar figure.
- **4.0s, on "Part B deductible":** Same amber line as scene 2: "Part B deductible: you pay." "Same as Plan G" tag clicks in beside it.

### Scene 4: Difference 1, copays (0:25–0:34)
- **Layout:** Talking head full frame. Badge top left, cards in the top third.
- **0.0s:** "Difference #1" badge pops in top left.
- **1.0s, on "copays":** Title "Copays" scales in.
- **3.0s, on "twenty dollars":** Stethoscope icon card with a counter rolling up to "$20 office visit."
- **6.0s, on "fifty at the ER":** Hospital icon card with a counter rolling up to "$50 ER visit," plus a small note: "Waived if admitted."

### Scene 5: Difference 2, excess charges (0:34–0:43)
- **0.0–1.5s:** Talking head full frame. "Difference #2" badge pops in top left.
- **1.5–6.0s, cutaway:** Full-screen graphic, with the talking-head audio continuing underneath. A doctor's bill builds line by line: "Medicare-approved amount" bar, then a red "+15% excess charge" bar stacks on top. Label: "Up to 15% above Medicare's rate."
- **6.0s, on "Plan G covers it":** Cut back to the talking head. Split card in the top third: "G ✓ Covered" (green) on the left.
- **7.5s, on "N doesn't":** "N ✗ Not covered" (red) on the right.

### Scene 6: Which one fits (0:43–0:52)
- **Layout:** Talking head full frame. Two cards placed to match his gestures.
- **0.5s, on the Plan N line:** Card on his left (screen right) slides in: "Plan N: lower premium, small copays."
- **5.0s, on the Plan G line:** Card on his right (screen left) slides in: "Plan G: predictable costs."
- **8.0s:** Both cards hold, with a light pulse.
- Check the gesture directions in the Omni clip and swap the card sides if needed.

### Scene 7: Call to action (0:52–0:59), then the end card
- **Layout:** Talking head full frame.
- **0.5s, on "Comment GUIDE":** Large "Comment GUIDE" button graphic in the lower-middle with a bouncing arrow pointing down, matching his point.
- **3.0s, on "free 2027":** Guide cover mockup (`Medigap-Plan-Comparison-Guide-2027-Edition.pdf` page 1) flies in at the top with a soft shadow.
- **0:59–1:02, end card:** Full-screen brand end card with the guide cover, "Comment GUIDE," agency name, and the agency disclaimer (same as Part 1).

---

## Reel caption

Plan G vs Plan N: they look almost the same, but two differences decide which one fits you.

1. Copays: Plan N can charge up to $20 at some office visits and up to $50 at the ER.
2. Excess charges: Plan G covers them. Plan N doesn't.

Comment GUIDE and I'll send you my free 2027 Medigap comparison guide.

#Medicare #Medigap #PlanG #PlanN #MedicareSupplement #Turning65

## Production notes

- If an Omni clip runs long, trim the dead air at the start or end. Don't speed up the voice.
- The 2027 Part B deductible is usually announced in November, so no dollar figure appears. Add it to the caption or a pinned comment once CMS publishes it.
- Some states (CT, MA, MN, NY, OH, PA, RI, VT) ban or limit excess charges. Add a footnote to scene 5 if your audience is in one of them.
- Massachusetts, Minnesota and Wisconsin use their own standardized Medigap plans, so Plans G and N aren't sold there.
- Premiums vary by state, age, ZIP code and carrier, so keep "usually" in scene 3.
- The Facebook comment-to-DM workflow triggers on "GUIDE" anywhere on the Page, so no new workflow is needed. Confirm the PDF guide covers Plan N.
- Get compliance review before posting.

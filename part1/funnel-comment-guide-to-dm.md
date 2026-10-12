# Facebook Comment-to-DM Funnel — Medigap Plan Comparison Guide (2027 Edition)
*Drafted 2026-10-07. Same pattern as the Turning 65 funnel (Gohighlevel_mcp_setup/funnel-comment-to-dm-2026-08-20.md).*

**Flow:** Facebook Reel (Part 1) -> viewer comments **GUIDE** -> automatic Messenger DM with link -> opt-in page (name, email, phone) -> thank-you page with the PDF + guide emailed -> lead tagged and added to the pipeline for the free rate check follow-up.

## Build map

| Piece | Status |
|---|---|
| Guide PDF | Done: `guide/Medigap-Plan-Comparison-Guide-2027-Edition.pdf` |
| Reel video | Done: `Best-Medigap-2027-Part1-Plan-G-v2.mp4` |
| Post caption, DM copy, page copy | Drafted below |
| Facebook Page connected to GHL | Confirm under Settings -> Integrations |
| Upload PDF to GHL Media Library | You (copy the hosted link) |
| Opt-in page + thank-you page | Build in GHL Funnels from the copy below |
| Workflow (comment trigger -> DM -> tag -> email) | Build in GHL Workflows (trigger and DM are not reachable via the MCP) |
| Test with a personal account | Before posting the Reel |

## 1. Reel caption
Plan G is the most popular Medigap plan for a reason. Here's how it works, and how it compares to the other 9 plans.

Comment **GUIDE** and I'll send you our free Medigap Plan Comparison Guide (2027 Edition), plus a free rate check for your area. 👇

*(Add the agency's approved TPMO disclaimer line if your compliance process requires it on social posts.)*

## 2. Auto-DM (sent when someone comments "guide")
Hey! Thanks for commenting 🙌 Here's your free Medigap Plan Comparison Guide. Tell me where to send it and I'll also run a free rate check for your area:

**[LINK TO OPT-IN PAGE]**

Talk soon,
Arric — Allen & Associates

*(Keep it short. Optional second DM 24h later if they haven't opened the link: "Quick reminder, your guide is waiting here: [LINK]".)*

## 3. Opt-in page (`/guide`)
**Headline:** Get Your Free Medigap Plan Comparison Guide
**Sub:** All 10 Medigap plans side by side, Plan G explained, and the questions to ask before you compare rates. Includes a free rate check for your area.
**Bullets:**
- Plan A to N benefits chart on one page
- Why Plan G is the most popular Medigap plan
- 5 questions to ask when comparing carriers
- A free rate check for your ZIP code, no obligation

**Form:** First name, Email (required), Phone (required), ZIP code (so the rate check is ready). Button: **Send Me the Guide ->**
**Consent text under the button (needs your compliance sign-off):** "By submitting, you agree that Allen & Associates may contact you by email, phone or text about Medicare Supplement options. Consent is not a condition of receiving the guide. Message and data rates may apply."
**Footer:** `[INSERT AGENCY'S APPROVED TPMO / CMS MARKETING DISCLAIMER]` and "Not affiliated with or endorsed by the U.S. government or the federal Medicare program."

## 4. Thank-you page (`/guide-sent`)
**Headline:** Your Guide Is Ready
**Body:** Download it below. We also emailed you a copy. We'll follow up shortly with your free rate check. Prefer to talk now? Call 800-324-9986.
**Elements:** Download button (Media Library PDF link), optional "Book a Free Call" button (Calendars), same disclaimer.

## 5. Delivery email (sent by the workflow on form submit)
Subject: Your Medigap Plan Comparison Guide (2027 Edition)
Body: "Hi {{contact.first_name}}, here's your guide: [PDF LINK]. Plan benefits are standardized, so the chart is accurate for 2027. Dollar figures are Medicare.gov's 2026 amounts and I'll send an update when CMS publishes 2027. Want me to check rates for your ZIP code? Just reply to this email or call 800-324-9986. Arric"

## 6. Workflow spec (GHL -> Automation -> Workflows)

**Workflow A: comment to DM**
1. Trigger: Facebook comment on this specific post, comment contains "guide" (not case-sensitive)
2. Action: Send Messenger DM (copy in section 2)
3. Action: Add tag `medigap-guide-comment`

**Workflow B: form submitted**
1. Trigger: Form submitted (opt-in page form)
2. Actions: add tag `medigap-guide-lead`; send delivery email (section 5); create/update opportunity in the pipeline at stage "New Lead", with a task for the rate check; optional internal notification to Arric

## 7. Things to verify before launch
- **Reels support:** confirm the GHL comment trigger works on a Reel and not only on a standard Page post. Test by commenting from a personal account on the published Reel. If it doesn't fire, post the video as a regular Page video and share it as a Reel.
- **Messenger rules:** Meta allows one private reply per comment, within about 7 days of the comment. Don't send promotional follow-ups beyond Meta's messaging window.
- **Page connection and permissions:** the Page must be connected in GHL with messaging permissions, or the DM won't send.
- **Compliance:** TPMO disclaimer, consent language and call/text rules need your agency compliance review before launch.
- **Keyword variants:** consider also matching "guide" with punctuation or typos ("guide!", "Guide pls"). A "contains" match handles most of them.

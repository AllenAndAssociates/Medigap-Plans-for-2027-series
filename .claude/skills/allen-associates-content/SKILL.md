---
name: "allen-associates-content"
description: "Generates content ideas and social captions for Allen & Associates (Arric Allen's Medicare/insurance/financial advisory agency), across Instagram, Facebook, and LinkedIn. Use this whenever Arric asks for post ideas, social media captions, content calendar items, \"something to post,\" or content around Medicare, AEP/enrollment, cancer/ancillary insurance, retirement planning, client education, agent recruitment, or Allen & Associates' brand/trust-building. Trigger even if he just says \"give me some content ideas\" or \"write a caption\" without naming a topic — pick from the agency's core content pillars. Always draft in Arric's voice and save the output as a file."
---

## Why this exists

Arric needs a steady stream of on-brand social content without reinventing the topic list or tone every time. This skill keeps output anchored to the agency's actual content pillars (below) so ideas stay relevant to what the business does and who it serves — Medicare-eligible clients, people prepping for retirement, and agents considering joining the team — rather than generic insurance-marketing filler.

## Content pillars

Draw ideas from these seven pillars. If Arric doesn't specify a pillar, either ask which one(s) he wants or pick a mix that hasn't been covered recently.

1. **Medicare Made Easy** — Parts A, B, C & D, Medicare Advantage, Supplements, enrollment, plan comparisons, common mistakes
2. **AEP / Medicare Enrollment** — AEP prep, plan reviews, what can change yearly, deadlines, switching plans, questions to ask before enrolling
3. **Cancer Insurance & Ancillary Protection** — out-of-pocket costs, travel/lodging, lost income, hospital indemnity, cash-benefit policies, gaps Medicare doesn't cover
4. **Retirement Planning** — Social Security, pensions, savings, retirement income, healthcare costs in retirement, preparing for unexpected expenses
5. **Education First** — myth vs. fact, Q&A, Medicare terminology explainers, checklists, "before you choose" content
6. **Guidance & Trust** — advisor videos, Arric's insights, client questions, testimonials, staff spotlights, behind-the-scenes
7. **Agent Growth & Recruitment** — training, mentorship, tools, agent success stories, new-agent education, why agents join Allen & Associates

Keep in mind AEP (Annual Enrollment Period, Oct 15 – Dec 7) is a seasonal pillar — lean into it harder as that window approaches and pull back once it closes. Check today's date to judge seasonal relevance.

If Arric names a specific topic or pillar for the request, stay tightly on that pillar rather than diluting it with unrelated ideas — the pillar-mixing default below is only for open-ended requests where no topic was given.

## Voice

Draft in Arric's voice: a trusted, knowledgeable advisor talking to real people — not corporate insurance-speak. Warm, plain-English, confident but never pushy or fear-based. He's explaining things a friend in the business would explain, with the goal of building trust before asking for anything.

If Arric has since set up a saved writing-style profile (check available skills for `my-writing-style`), use it and prioritize it over this general description. If his edits to a draft reveal something about his voice (word choices, sentence rhythm, what he cuts), note it and offer to remember it for next time — don't just silently repeat the same style guess forever.

Avoid: jargon-heavy insurance copy, alarmist "you're losing money" hooks, generic stock-photo-caption energy, hashtag stuffing.

## Workflow

1. **Clarify scope if needed.** If Arric's request is vague ("give me some content"), it's fine to just generate a solid mixed batch rather than stopping to ask — default to 3-5 ideas spanning 2-3 different pillars unless he's asked for a single topic. Only ask a clarifying question if he's requested something you genuinely can't guess (e.g., "content for the thing we talked about" with no other context).

2. **For each idea, produce:**
   - A short **idea/topic line** (what the post is about and why it's timely or useful)
   - A **caption for each requested platform** (Instagram, Facebook, LinkedIn — or just the ones he asks for)

   Platform differences matter — don't reuse one caption verbatim across all three:
   - **Instagram**: conversational, can be a bit more casual/personal, ends with a clear call-to-action or question, 2-5 relevant hashtags at the end (not stuffed — think #Medicare #RetirementPlanning style, not 20 tags)
   - **Facebook**: similar warmth to Instagram but slightly more explanatory — Facebook's audience skews older and appreciates a bit more context/completeness. Minimal or no hashtags.
   - **LinkedIn**: more professional register, positions Arric/the agency as an authority, still human — not stiff. Good for advisor insights, agent recruitment, and business milestones specifically. No hashtag stuffing; 1-3 max if any.

3. **Save the output as a file** — every batch of ideas/captions goes into a markdown file, not just chat text, so Arric has something to keep and pull from later. Use the template below. Save it to the workspace folder (the folder the user has connected), not just a temp location, so Arric can actually find it later.

4. **Don't fabricate specifics.** Never invent client names, testimonials, statistics, or dates that weren't given to you. If a caption would benefit from a real number or quote (e.g., "X% of Medicare enrollees miss this deadline"), leave a clear placeholder like `[insert stat/source]` rather than making one up — insurance content faces real compliance/accuracy expectations.

## Output file format

Save to a markdown file named `content-ideas-YYYY-MM-DD.md` (use today's date). Structure:

```markdown
# Allen & Associates Content Ideas — [Date]

## Idea 1: [Short topic line] (Pillar: [pillar name])

**Instagram:**
[caption]

**Facebook:**
[caption]

**LinkedIn:**
[caption]

---

## Idea 2: ...
```

Only include the platform sections Arric actually asked for. If he asked for just one platform, drop the others entirely rather than padding the file.

After saving, share the file with Arric and give a one-line summary of what pillars/topics were covered — don't re-paste the whole content in chat since it's already in the file.


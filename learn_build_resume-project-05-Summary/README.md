# Writing Your Resume Summary with AI

> Lesson five in the "Build Your Resume with AI" series. Time to get your hands dirty—you'll use AI to craft 3-4 targeted Summary versions for different job directions, then mix and match them with your resume body.

## Overview

You made it this far—nice work.

In the previous lessons, we covered the hiring process, ATS mechanics, new grad resumes, and experienced hire resumes. You now understand what a Summary is, why it matters, and what a good one looks like.

Now it's time to actually write one.

This lesson has one goal: **use AI to write Summaries you can put directly on your resume.**

Not theory. Not concepts. Actual output—several Summary versions targeting different job families (Backend, Full-Stack, Data, ML, etc.). Once you have these, you pick the right version for each application and pair it with your resume body.

This is the core Tailoring strategy: keep the resume body mostly the same, swap the Summary based on the role.

---

## Learning Objectives

By the end of this lesson, you will:

1. **Use the `/summary-writer` command**—an interactive AI assistant that helps you brainstorm, find your positioning, and draft your Summary
2. **Use the `/summary-reviewer` command**—a tough interviewer persona that evaluates whether your Summary would make a hiring manager keep reading
3. **Master the two-window workflow**—one writes, one reviews, iterate until you have something solid

---

## Before You Start: Build Your Profile

Before the AI can help you, it needs to understand your background.

**This step is critical.** Put your background information in the `profile/` directory—and be thorough.

Don't just drop in a rough resume draft. Break down your experience into individual items:

- Each project gets its own bullet—what you built, what tech you used, what happened
- Each work experience expanded—not just job titles, but what you actually owned
- Achievements you're proud of, even small optimizations
- Your tech stack, organized by category
- Anything that might be worth mentioning

Why so detailed?

The AI can only work with what you give it. More detail means better insights and positioning. If you give it a bare-bones resume, you'll get a bare-bones Summary.

Think of `profile/` as your raw material bank. It doesn't need to be polished—this isn't for interviewers, it's context for the AI. More is better. Specific is better.

If `profile/` is empty, the AI will ask you for information directly—but preparing ahead makes the whole process smoother and the output better.

---

## Step 1: Draft with summary-writer

### What This Tool Does

`/summary-writer` is an interactive AI coach. Here's the workflow:

1. **Reads your profile**—understands your background
2. **Identifies directions**—based on your experience, suggests 2-4 career directions you could target (Backend Engineer, ML Engineer, Data Engineer, etc.)
3. **Guides your thinking**—asks key questions: How do you want to position yourself? What's your strongest selling point? What type of company are you targeting?
4. **Writes a draft**—produces a Summary based on your discussion
5. **Saves the output**—stores your Summary in `resume/summary/` with a filename matching your direction (e.g., `backend.md`, `fullstack.md`)

### How to Use It

Open your terminal, start Claude Code, and type:

```
/summary-writer
```

That's it. From there, it's a conversation.

The AI reads your profile, then starts asking questions. Answering these questions is the process of clarifying your own thinking.

It might ask:
- "I see you've done backend and data work. Which direction do you want to emphasize?"
- "What was your specific contribution to the XX project? Any measurable outcomes?"
- "Are you targeting big tech, startups, or something in between? Entry-level or mid-level?"

After the discussion, it drafts a Summary for you.

### About Length

For new grads, a Summary is typically two lines—maybe three.

The AI might write slightly longer—that's fine. Longer is easier to trim than short is to expand.

You can:
- Cut unnecessary adjectives
- Remove less important information
- Tighten the phrasing

The AI's job is to help you think clearly and give you a draft you can use immediately with minor edits. Final length and wording are your call.

### Where Output Goes

Summaries are saved to:

```
resume/summary/{direction}.md
```

Write a Backend Summary? It goes to `resume/summary/backend.md`.

This way you accumulate multiple versions. When applying to different roles, you just pick the right one.

---

## Step 2: Evaluate with summary-reviewer

### What This Tool Does

`/summary-reviewer` simulates a tough hiring manager.

The persona: 10 years of hiring experience, reviews hundreds of resumes monthly, has seen every trick. It evaluates your Summary from the interviewer's perspective:

**If I were the Hiring Manager for this role, would this Summary make me want to keep reading? Or would I move on to the next candidate?**

It scores you, points out problems, and suggests improvements.

### What You Need

Give the AI three things:

1. **Job Description**—your target role. Put it in `application/job-description.md` or provide it directly in chat
2. **Your resume**—so the AI understands your overall background
3. **Your Summary**—what it's evaluating. If your resume already includes the Summary, no need to repeat it

### How to Use It

Open your terminal, start Claude Code, and type:

```
/summary-reviewer
```

The AI checks for existing files:
- Looks for a JD in `application/job-description.md`
- Looks for Summaries in `resume/summary/`

If files exist, it asks which Summary you want reviewed. If something's missing, it prompts you.

### Evaluation Criteria

It scores you on five dimensions:

- **Position Fit**: Does your Summary align with what the JD is looking for?
- **Credibility**: Are your claims believable? Any red flags?
- **Differentiation**: Would you stand out from the other 100 applicants?
- **Scannability**: Can I get the key info in 3 seconds?
- **Language Quality**: Is it professional and well-written?

You get an overall score, a verdict, and a "here's how I'd rewrite it" example.

### The Feedback Style

This AI persona is deliberately harsh. It tells you what's wrong:

- "You're a new grad using 'Architected'—that word is too big for your experience level. Now I'm questioning everything else on your resume."
- "'Passionate about technology' tells me nothing. Skip the buzzwords."
- "The JD wants a Data Engineer, but 80% of your Summary talks about web development. Wrong direction."

Don't take it personally—this is the value. Better to hear this from the AI before you submit than to get silently passed over by a real hiring manager.

---

## Step 3: Two Windows, Iterate to Polish

Now you know both commands. They work best **together**.

### Recommended Workflow

1. **Open two terminal windows**, each running a Claude Code instance
2. **Left window runs `/summary-writer`**—for writing and revising
3. **Right window runs `/summary-reviewer`**—for evaluation and challenge

The loop:

1. Draft a Summary in the left window
2. Copy it to the right window for evaluation
3. Right window gives feedback and suggestions
4. Copy those suggestions back to the left window for revision
5. Revise, then send back to the right window
6. Repeat until you get a good score

Usually takes 2-3 rounds to get something solid.

### Why Two Windows?

Because these two AI personas have different jobs.

Summary Writer is your coach—helps you find highlights, organize your pitch, get words on paper. It's biased toward "let's make this work."

Summary Reviewer is a picky interviewer—finds problems, challenges claims, pushes back. It's biased toward "not good enough, try again."

The tension between them pushes your Summary to be better than either could produce alone.

---

## Final Output

After this process, you'll have several Summary files in `resume/summary/`:

```
resume/summary/
├── backend.md
├── fullstack.md
├── ml-engineer.md
└── data-engineer.md
```

Each file targets a different direction. When applying, pick the right Summary for the role and combine it with your resume body.

This is Tailoring at its simplest: same body, swap the Summary.

---

## Assignment

This lesson has two parts.

### Part 1: Submit One Summary for Instructor Review

1. Use `/summary-writer` to draft a Summary
2. Use `/summary-reviewer` to evaluate it
3. Revise based on feedback, then evaluate again
4. **Iterate at least 3 rounds** until you're satisfied

When done, submit the following in the course card comments:

- Your Summary (final version)
- Your resume (or profile content)
- The Job Description you targeted
- The `/summary-reviewer` evaluation from your final round

Your instructor will review your submission, confirm you've got the workflow down, and suggest further improvements.

### Part 2: Prepare 3 Summaries with Different Positioning

After instructor confirmation, continue practicing on your own.

Goal: prepare **3 Summaries targeting different directions**. Same person, different positioning. For example:

- One targeting startups—emphasize ownership, shipping fast, wearing multiple hats
- One targeting product-focused roles—emphasize user-facing work, product thinking, impact metrics
- One targeting AI-native application roles—emphasize LLMs, prompt engineering, RAG systems
- One targeting data-driven roles—emphasize pipelines, analytics, data infrastructure

You don't have to use these exact four. Pick directions that match your background and job search goals.

The key insight: **one person can position themselves multiple ways**. These 3 Summaries become your toolkit for different applications.

---

## Key Takeaways

**First, AI is a tool, not a replacement.** It helps you think clearly, write faster, and get feedback—but final judgment is yours. Edit its drafts. Filter its suggestions.

**Second, longer is easier to fix than shorter.** Let the AI write more, then you trim. Cutting is easier than adding from scratch.

**Third, iteration is normal.** Nobody writes a perfect Summary on the first try. Write-review-revise-review is the standard process.

**Fourth, prepare multiple versions.** Different roles need different positioning. Invest time in creating a Summary for each direction so you can mix and match when applying.

**Fifth, do the final check yourself.** After AI evaluation, paste your Summary into your actual resume document. Check if it fits in two lines. Too long? Cut. Too short? Add.

---

## Mentor's Note

**Why this exercise matters:**

A lot of people overthink the Summary—they want to get it perfect on the first try, or they expect AI to hand them the final answer.

That's not how it works.

A Summary is fundamentally a positioning problem: you're telling the reader who you are, what you can do, and why they should keep reading. That positioning doesn't appear out of nowhere. It emerges through thinking, trying, getting feedback, and revising.

AI accelerates this process. Before, you'd sit alone, draft something, ask friends to review it, revise, repeat. Now you can have a conversation with AI—let it ask you questions, help you articulate your strengths, challenge your assumptions.

But at the end of the day, your Summary tells your story. You own it.

**Key insights:**

- Don't expect AI to give you a perfect answer. Expect a strong starting point that you polish.
- The two-window workflow creates productive tension—one pushes forward, one pushes back.
- Multiple Summary versions aren't extra work—they're your competitive advantage in a tailored job search.

**Next steps:**

After completing this lesson, you'll have a reusable workflow for any future job search. Every time you target a new direction, just run the same process. The tools get smarter as you give them better context, and you get faster as you internalize what makes a Summary work.

Good luck writing a Summary that makes people want to keep reading.

---

## Quick Reference

**Write a Summary:**
```
/summary-writer
```

**Evaluate a Summary:**
```
/summary-reviewer
```

**Key files:**
- `profile/` - Your background information
- `application/job-description.md` - Target job description
- `resume/summary/` - Summary output directory

**Recommended workflow:**
1. Two terminal windows—one writes, one reviews
2. Draft → Evaluate → Take feedback back to revise → Evaluate again
3. Iterate 2-3 rounds until satisfied

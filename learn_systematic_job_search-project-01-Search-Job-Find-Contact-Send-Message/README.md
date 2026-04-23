# AI-Powered Systematic Job Search

> This tutorial teaches you how to use AI to automate three critical steps of job hunting: **finding matching jobs**, **identifying people to contact**, and **writing personalized outreach messages**. Let AI handle the repetitive grunt work so you can focus on what actually matters—preparing for interviews, building skills, and having real conversations.

---

## Why Systematic Job Hunting?

Here's the reality: the old "spray and pray" approach—sending out hundreds of applications and hoping someone bites—doesn't work like it used to.

According to Revelio Labs, entry-level job postings in the US dropped by about 35% between 2023 and 2025. SignalFire's research found that major tech companies and mature startups saw a 50% decline in hiring employees with less than one year of experience. This isn't fear-mongering—AI is automating a lot of junior-level tasks, and companies are realizing that one senior engineer with AI tools can do what an entire team of juniors used to do.

But here's the thing: **AI is both the problem and the solution**.

The traditional job search is a brutal funnel:

- Send out 100 applications
- Get maybe 3-5 responses
- Land 1 offer if you're lucky

What's the problem? **Low efficiency, low hit rate.** You're spending hours on applications that go nowhere instead of focusing on opportunities where you actually have a shot.

The systematic approach flips this around:

- Use AI to quickly filter down to **jobs that actually match**
- Use AI to find **people inside the company** you can reach out to
- Use AI to write **personalized messages** that get responses
- Then **go on the offensive**—instead of passively waiting

Why does proactive outreach matter so much? Because when you're just starting out without an established career track record, your resume gets buried under thousands of other applications. But if you can connect with someone inside—an alumnus, a team member, a recruiter—your resume is 10x more likely to get a real look.

That's what this course teaches: **how to make "going on the offensive" efficient and repeatable using AI**.

---

## Prerequisites

This course assumes you've already done some groundwork:

**You know what you're looking for**

- You have a clear target role (Data Scientist? Software Engineer? Product Manager?)
- You understand your strengths and what makes you a compelling candidate
- Your resume is polished and ready

**Your profile materials are organized**

In earlier courses, we covered how to use AI to structure your profile and experience—clarifying your situation, goals, and story. If you haven't done that yet, go back and complete it first.

**The starting point for this course** is: you have a solid resume and clear job search goals. Now we're going to **10x your application efficiency with AI**.

---

## The Three Tools

This course gives you three AI prompt tools that work together as a complete workflow:

**1. LinkedIn Job Search** — Requires Claude for Chrome

- **Input**: Your resume, job objectives, filter criteria
- **What it does**: AI **operates your browser**, browsing job listings on LinkedIn, clicking into each posting to read the full JD, scoring matches against your criteria
- **Output**: A structured TSV file with ranked job matches
- **Why browser control is needed**: AI needs to actually click, scroll, and read page content

**2. LinkedIn Contact Finder** — Requires Claude for Chrome

- **Input**: A specific job's JD + your resume
- **What it does**: AI **operates your browser**, searching the company's LinkedIn page for four types of people—Alumni, Future Peers, Recruiters, and Hiring Managers
- **Output**: A structured TSV file with contacts and suggested outreach angles
- **Why browser control is needed**: AI needs to navigate company pages, click into profiles, and extract information

**3. LinkedIn Cold Message** — Any AI works

- **Input**: A specific contact's info + your resume + your outreach angle and goal
- **What it does**: AI generates a personalized LinkedIn message based on the contact's background and your situation
- **Output**: A ready-to-copy-paste message
- **Why no browser needed**: This is pure text generation

The workflow goes like this:

1. Use **Job Search** to find a batch of matching positions
2. Pick your top choice, use **Contact Finder** to identify people to reach out to
3. Select a contact, use **Cold Message** to generate a personalized message
4. Send the message, build the connection, work toward a referral or interview

---

## Project Structure

Before diving in, here's how the project is organized:

```
project/
├── profile/                                    # Your personal materials (you prepare these)
│   ├── resume.md                               # Your resume
│   ├── objective.md                            # Job search objectives
│   ├── narrative.md                            # Additional context (optional)
│   ├── job-search-additional-requirements.md   # Extra search criteria
│   ├── job-description.md                      # Target job's JD (for tools 2 and 3)
│   ├── code-message-target-person.md           # Contact target (for tool 3)
│   ├── code-message-out-reach-key.md           # Outreach angle (for tool 3)
│   └── code-message-outcome.md                 # Desired outcome (for tool 3)
│
├── docs/                                          # Prompt templates and generated prompts
│   ├── linkedin-job-search-prompt.template.md     # Tool 1 template
│   ├── linkedin-job-search-prompt.md              # Generated prompt
│   ├── linkedin-job-search-results.tsv            # Example: search results
│   ├── linkedin-contact-finder-prompt.template.md # Tool 2 template
│   ├── linkedin-contact-finder-prompt.md          # Generated prompt
│   ├── contacts.md                                # Example: contact list
│   ├── linkedin-cold-message-prompt.template.md   # Tool 3 template
│   └── linkedin-cold-message-prompt.md            # Generated prompt
│
├── prompt_generator.py        # Core script: merges templates with your materials
└── mise.toml                  # Task runner configuration
```

**Key concepts**:

- `*.template.md` files are **templates** with placeholders like `{{RESUME_CONTENT}}`
- `prompt_generator.py` reads your files from `profile/` and fills in the templates
- The generated `*.md` files (without "template") are the complete prompts you give to AI

---

## Setup

This project just needs a global Python environment—no virtual environment required.

**Install dependencies**:

```bash
# If you have mise installed, just run
mise install

# Or make sure you have Python 3.12+
python --version
```

**Available commands**:

```bash
mise run gen-job-search      # Generate Job Search prompt
mise run gen-contact-finder  # Generate Contact Finder prompt
mise run gen-cold-message    # Generate Cold Message prompt
```

You can also run the Python script directly:

```bash
python prompt_generator.py job-search
python prompt_generator.py contact-finder
python prompt_generator.py cold-message
```

---

## Tool 1: LinkedIn Job Search

### What This Tool Does

Once you have your resume and objectives ready, step one is finding matching positions. The traditional approach is scrolling through LinkedIn one by one—but that's slow and you'll miss good opportunities.

This tool has AI do it for you:

1. AI browses job listings on the LinkedIn search page
2. **Clicks into each posting** to read the full JD (not just the title)
3. Scores each position against your resume and objectives
4. Outputs a **structured TSV file**, ranked by match quality

### What You Need to Prepare

In the `profile/` directory, prepare these files:

**[profile/resume.md](./profile/resume.md)** - Your resume

This is the most important input. AI uses your resume to judge which jobs fit you. Check our example file for the format.

**[profile/objective.md](./profile/objective.md)** - Job search objectives

Tell AI what you're looking for. Example:

```markdown
- Objective: Find a full time job as Data Scientist or Machine Learning Engineer
- Current Situation: Master's graduate, Feb 2026
- Visa Status: F1, need H1B sponsorship
- Location Preference: Remote or NYC/Boston
- Salary Expectation: $80k+
```

**[profile/narrative.md](./profile/narrative.md)** - Additional context (optional)

Any soft preferences that don't fit in your resume. Things like "prefer small teams" or "value work-life balance."

**[profile/job-search-additional-requirements.md](./profile/job-search-additional-requirements.md)** - Extra filter criteria

For example:

```markdown
- Output limit: 15 positions
- Only include jobs posted within the last 7 days
- Exclude contract/temporary positions
- Focus on positions that sponsor H1B
```

### How to Generate the Prompt

Once your files are ready, run:

```bash
mise run gen-job-search
```

This command calls [prompt_generator.py](./prompt_generator.py), which does something simple:

1. Reads the template file [docs/linkedin-job-search-prompt.template.md](./docs/linkedin-job-search-prompt.template.md)
2. Reads your files from `profile/`
3. Replaces placeholders like `{{RESUME_CONTENT}}` with your actual content
4. Outputs to [docs/linkedin-job-search-prompt.md](./docs/linkedin-job-search-prompt.md)

If you want to understand the exact replacement logic, just read [prompt_generator.py](./prompt_generator.py)—it's straightforward string substitution.

### How to Use the Generated Prompt

**Important**: This step requires **Claude for Chrome** (or another browser-controlling AI). Regular ChatGPT or Claude's web interface can't do this because they can't operate your browser.

1. Open LinkedIn Jobs search in Chrome, make sure you're logged in
2. Enter your target job title (e.g., "Data Scientist")
3. Open Claude for Chrome and paste the contents of [docs/linkedin-job-search-prompt.md](./docs/linkedin-job-search-prompt.md)
4. AI will automatically operate your browser: clicking jobs, scrolling, reading JDs, analyzing fit
5. AI outputs a TSV file with results

### Output

AI generates a TSV file like this:

[docs/linkedin-job-search-results.tsv](./docs/linkedin-job-search-results.tsv)

Each row contains:

- `title` - Job title
- `company` - Company name
- `location` - Location
- `posting_date` - When it was posted
- `short_description` - Brief summary
- `reasoning` - **Why this job fits you** (this is the key!)
- `job_link` - Direct link to the posting

**Pro tip**: Even though AI compiled this list, I **strongly recommend** you maintain your own Excel or Google Sheet to track each position—did you apply? When? Any responses? Need to follow up?

That tracking is **manual work** outside the scope of this course. This course focuses on using AI to automate search and filtering, but the actual tracking and follow-through is on you.

---

## Tool 2: LinkedIn Contact Finder

### What This Tool Does

After finding matching jobs, the next step is identifying people behind those jobs that you can reach out to.

Most people just click "Apply" and hope for the best—but your resume gets buried under hundreds or thousands of other applications. The smarter move is **finding insiders** who can refer you or at least make sure your resume gets a real look.

This tool helps you find four types of contacts:

**Alumni** - 40-60% response rate

The easiest connection to make. Shared school identity creates instant trust, and most people are happy to spend a few minutes helping someone from their alma mater.

**Future Peers** - 30-50% response rate

People in similar roles to the one you're applying for. They can tell you what the team is really like, what the interview process looks like, and the actual culture.

**Recruiters** - 20-40% response rate

The people directly responsible for hiring. If you connect with them, your resume gets more attention.

**Hiring Managers** - 5-15% response rate

Hardest to reach but highest value. If they respond, you're basically in the door.

### What You Need to Prepare

**[profile/job-description.md](./profile/job-description.md)** - Target job's JD

Pick your top choice from the Job Search results and paste the full JD here. We've included a Nasdaq Data Scientist example.

**[profile/resume.md](./profile/resume.md)** - Your resume

AI extracts your school information to search for alumni.

### How to Generate the Prompt

```bash
mise run gen-contact-finder
```

The generated prompt is at [docs/linkedin-contact-finder-prompt.md](./docs/linkedin-contact-finder-prompt.md).

### How to Use

**Important**: This step also requires **Claude for Chrome**. AI needs to operate your browser on LinkedIn to search for contacts.

1. Open the target company's LinkedIn page in Chrome (e.g., `linkedin.com/company/nasdaq`), make sure you're logged in
2. Open Claude for Chrome and paste the generated prompt
3. AI will automatically operate your browser: searching the company page, clicking the "People" tab, filtering contacts, clicking into profiles to read details
4. AI outputs a contact list

### Output

AI generates a result like this:

[docs/contacts.md](./docs/contacts.md)

Each contact includes:

- `category` - Type (Alumni/Future Peer/Recruiter/Hiring Manager)
- `name` - Full name
- `title` - Job title
- `school_match` - Alumni relationship (if any)
- `connection_degree` - How you're connected (2nd or 3rd)
- `recent_activity` - Recent LinkedIn activity
- `linkedin_url` - Profile link
- `outreach_angle` - **Suggested approach for reaching out**

AI also gives you a **priority recommendation**—who to contact first and why.

---

## Tool 3: LinkedIn Cold Message

### What This Tool Does

Once you've identified contacts, the final step is writing a message that actually gets a response.

This isn't easy. Most people's cold messages look like this:

> "Hi, I'm a recent graduate looking for a job. I saw you work at [Company]. Would you be willing to refer me?"

The problem? **It's generic.** They might get dozens of messages like this every day. Why would they respond to yours?

A good cold message needs to:

1. **Be personalized** - Make them feel like you specifically reached out to them, not mass-blasting
2. **Offer value** - Give them a reason to respond
3. **Ask small** - Don't ask for too much upfront

This tool helps you generate messages that hit all three.

### What You Need to Prepare

**[profile/code-message-target-person.md](./profile/code-message-target-person.md)** - Contact target

Pick one row from the Contact Finder results and paste it here.

**[profile/code-message-out-reach-key.md](./profile/code-message-out-reach-key.md)** - Outreach angle

Why are you reaching out to this specific person? What's the connection point or hook?

Pick the one that fits your situation, or customize:

- `We're both [School] alumni, I saw you're in the [team] I'm applying to` — Alumni angle
- `I read your post about [topic] and had some thoughts to share` — Responding to their activity
- `I built a similar project to what your team works on, have a live demo: [URL]` — Showcasing your work
- `I wrote a paper on the same topic you specialize in` — Academic/professional resonance
- `We have [N] mutual connections` — Shared network

If you're not sure what angle to use, leave it blank—AI will suggest options based on the contact's info.

**[profile/code-message-outcome.md](./profile/code-message-outcome.md)** - Desired outcome

What do you want from this outreach? Pick one:

- `Get a 15-minute phone call to learn about the team` — **Recommended**, lowest barrier, highest response rate
- `Ask for a referral to the open position` — More direct, works better when you already have some connection
- `Request a coffee chat to understand the company culture` — Relationship-building, no rush
- `Get advice on breaking into this field` — Advice-seeking mode, flattering to them

**Tip**: For first-time outreach, go with option 1 or 3. A "15-minute call" or "coffee chat" is the lowest barrier—easiest to say yes to. Build the relationship first, then ask for a referral later.

### How to Generate the Prompt

```bash
mise run gen-cold-message
```

The generated prompt is at [docs/linkedin-cold-message-prompt.md](./docs/linkedin-cold-message-prompt.md).

### How to Use

**Good news**: This step doesn't require Claude for Chrome. You can use **any AI**—ChatGPT, Claude's web interface, Claude Code, whatever you prefer. This is pure text generation, no browser control needed.

Just paste the generated prompt into your AI of choice, and it'll craft a personalized message for you.

### Output

AI generates a ready-to-use message like this:

[profile/code-message.md](./profile/code-message.md)

```
Hi Rachel, I saw your post about the Boston tech team! I'm a Math MS at NYU
with a background in ETL and ML. I built a predictive project similar to
Nasdaq's market data needs (demo: https://demo.example). Would you be open
to a referral or a brief chat about the Graduate DS role?
```

AI also explains the reasoning—what hook was used, why it highlighted certain value props, why the ask is appropriately sized.

---

## Full Workflow Example

Let's walk through the complete process using a Nasdaq Data Scientist position as our example.

### Step 1: Find Jobs (Using Claude for Chrome)

With your `profile/` files ready:

```bash
mise run gen-job-search
```

Open LinkedIn Jobs search, log in, then open **Claude for Chrome** and paste the generated prompt. AI operates your browser to run the search.

Example output: [docs/linkedin-job-search-results.tsv](./docs/linkedin-job-search-results.tsv)

In this example, AI found 15 matching positions. The top result is Nasdaq's Data Scientist - Graduate role.

### Step 2: Find Contacts at Nasdaq (Using Claude for Chrome)

Copy the Nasdaq JD to [profile/job-description.md](./profile/job-description.md), then:

```bash
mise run gen-contact-finder
```

Open Nasdaq's LinkedIn company page (`linkedin.com/company/nasdaq`), then run the generated prompt with **Claude for Chrome**.

Example output: [docs/contacts.md](./docs/contacts.md)

AI found:

- 4 Alumni (including Sagar, an NYU alum who's a 2nd degree connection)
- 3 Future Peers
- 3 Recruiters (including Rachel, Campus Recruiting Lead)
- 3 Hiring Managers

### Step 3: Write a Message (Any AI works)

Based on AI's recommendation, we'll reach out to Rachel (Campus Recruiting Lead) first—she's a 2nd degree connection and posted about Boston tech interns a month ago, signaling she's actively hiring.

With your contact info and outreach angle ready:

```bash
mise run gen-cold-message
```

This step doesn't need Claude for Chrome—use ChatGPT, Claude's web interface, whatever you like.

Example output: [profile/code-message.md](./profile/code-message.md)

### Step 4: Send the Message

Copy the generated message and send it on LinkedIn.

Then wait. If you don't hear back in 5-7 days, send a brief follow-up. If still nothing, move on to the next contact.

---

## Saving Your Results

I recommend saving all AI-generated outputs—TSV files, contact lists, messages—in this repo.

Benefits:

1. **You have records**: You can look back at who you contacted, what messages you sent
2. **Easy iteration**: If a message works well, you can use it as a template
3. **Build a system**: Job hunting is a marathon, and having a system beats winging it

---

## FAQ

### Why do alumni have the highest response rate?

It's human psychology:

- **In-group bias**: Same school = same tribe, instant trust
- **Pay-it-forward mentality**: Many people got help from alumni when they were starting out and want to return the favor
- **Low cost**: Responding takes 2 minutes. If it helps a fellow alum, why not?

### How long should my message be?

LinkedIn connection requests have a **300 character limit**, so keep it tight.

Rule of thumb: **shorter is better**. If you can say it in 3 sentences, don't use 5.

### How long should I wait before following up?

- Wait **5-7 days** after your initial message
- Follow up **at most twice**
- If still no response, move on to the next contact

### What if I get rejected?

Most of the time, people won't explicitly reject you—they just won't respond. That's normal.

Remember:

- Alumni response rates are 40-60%—meaning 4-6 out of 10 will reply
- You only need 1-2 responses to make progress
- Don't take silence as rejection—they're probably just busy

---

## Mentor's Note

Why learn this?

Job hunting is one of the most stressful experiences in most people's careers. You send out dozens of applications, hear nothing back. You go to career fairs, hand out resumes that vanish into the void. You start wondering if you're just not good enough.

But the problem might not be you—it might be your method.

Traditional job hunting was designed for an era of information scarcity: back then, just finding job postings was a competitive advantage. But now information is everywhere—anyone can find hundreds of "looks good" jobs on LinkedIn. The battlefield has shifted. **It's no longer about who can find opportunities—it's about who can get opportunities to see them.**

That's why proactive outreach matters so much. You're not a passive applicant waiting to be filtered—you're a professional actively building connections. That mindset shift is more important than any specific technique.

What role does AI play here? It's your accelerator. It can't build relationships for you—you still have to do that yourself. But it can save you dozens of hours of mechanical work: scrolling through job postings, searching for contacts, drafting messages. With that time saved, you can focus on what actually matters: preparing for interviews, building skills, having real conversations with real people.

One last thing: **job hunting is a skill, and skills can be practiced.** Your first cold message might feel awkward; by the fifth, you'll be comfortable. Your first ignored message might sting; by the tenth, you'll shrug it off.

What you're learning isn't just how to use a few AI tools—it's **a mindset for taking the initiative in the AI era**. That mindset will serve you throughout your entire career.

Good luck.

---

## Quick Reference

**Commands to generate prompts**:

```bash
mise run gen-job-search      # Tool 1: Find jobs
mise run gen-contact-finder  # Tool 2: Find contacts
mise run gen-cold-message    # Tool 3: Write message
```

**Key files**:

- [profile/resume.md](./profile/resume.md) - Your resume
- [profile/objective.md](./profile/objective.md) - Job objectives
- [profile/job-description.md](./profile/job-description.md) - Target job JD
- [prompt_generator.py](./prompt_generator.py) - Core script

**Example outputs**:

- [docs/linkedin-job-search-results.tsv](./docs/linkedin-job-search-results.tsv) - Job search results
- [docs/contacts.md](./docs/contacts.md) - Contact list
- [profile/code-message.md](./profile/code-message.md) - Generated message

# AI-103 — Study Session Logger / Status Update Prompt

Use this prompt after an AI-103 study conversation to update the repository from the actual conversation, not from assumptions.

## Purpose

Keep `PLAN/02-Progress.md` as the authoritative progress dashboard while preserving a useful history of how each study session was taught and tested.

## Prompt

```text
You are maintaining my Microsoft AI-103 certification study repository: ahmedifhaam/AI-103.

Treat the GitHub repository as the source of truth for the study plan, progress, schedule, weak areas, and topic gates. Treat the current conversation as the source of truth for what I actually learned in this session.

Before updating:
1. Read README.md.
2. Read PLAN/00-Master-Plan.md.
3. Read PLAN/01-Schedule.md.
4. Read PLAN/02-Progress.md.
5. Read PLAN/03-Exam-Strategy.md when relevant.
6. Review the entire current study conversation and extract only things that were actually taught, asked, answered, corrected, or demonstrated.

Then update the repository.

### Study-session logging requirements

Append a dated study-session record to PLAN/02-Progress.md. Do not replace or erase previous session history.

For the current session record capture:
- Date
- Main topic(s)
- Learning objective
- How the topic was taught
- Visual/mental models used
- Concepts learned
- Important distinctions / exam rules
- Examples used
- Every meaningful exam-style question asked
- My answer to each question
- My reasoning when it was stated
- Whether the answer was correct
- Any correction or clarification given
- Misconceptions / weak areas discovered
- Concepts that improved from earlier sessions
- Current confidence if explicitly established
- Hands-on status
- Topic-gate status
- Next learning target

For questions, preserve the substance of the question and answer rather than merely writing "quiz passed". Include enough detail to make the session useful for later review, but do not copy the entire conversation verbatim.

### Progress update requirements

Update the dashboard fields in PLAN/02-Progress.md when justified by the conversation:
- Current status
- Completed checkpoints
- Domain/topic progress
- Exam-question progress
- Retention
- Weak Area Queue
- Next Learning Target
- Daily Log

Keep progress conservative. Discussion alone does NOT make a topic mastered. Do not mark a topic green unless the repository's topic-gate requirements are actually satisfied.

If a concept was discussed but hands-on work or the required quick-check score is missing, keep the gate open/in progress.

### Teaching-style record

The session history should make it possible to reconstruct how I learn best. Record that the training uses the repository's learning philosophy when applicable:

VISUAL MODEL → SHORT EXPLANATION → EXAMPLE → HANDS-ON → QUICK CHECK → TOPIC GATE

Also record useful teaching patterns such as:
- ASCII architecture diagrams
- short comparison tables
- exam-trap distinctions
- scenario questions
- immediate correction after an answer
- concise mental models / rules to retain

Do not invent a teaching method that was not used in the conversation.

### README requirement

README.md must contain a link to this prompt under the Start Here section so this workflow is easy to find for future sessions.

### Output behavior

After making the repository changes:
1. Report which files were updated.
2. Summarize the newly logged session.
3. State the new current learning target and any weak areas.
4. Mention if a topic gate remains open and why.

Do not claim mastery merely because the conversation went well.
```

## Logging standard

The goal is **conversation → structured study evidence → progress update**.

A future session should be understandable without replaying the entire chat. The log should preserve the user's reasoning and the teaching/correction loop because these are useful for identifying recurring exam traps.

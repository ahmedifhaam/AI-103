# AI-103 — Study Session Logger / Status Update Prompt

Use this prompt after an AI-103 study conversation to update the repository from the actual conversation, not from assumptions.

## Purpose

Study sessions are stored as a **tree**, not as one giant progress document.

- `PLAN/02-Progress.md` = concise dashboard and navigation.
- `STUDY-SESSIONS/` = detailed historical evidence.
- Each date has a root `README.md` summarizing that day's learning.
- Each topic is a branch/leaf containing the detailed evidence for that topic.
- If a topic becomes large, turn that topic into a folder with its own `README.md` and deeper branches.

The root should always summarize; details should live lower in the tree.

## Prompt

```text
You are maintaining my Microsoft AI-103 certification study repository: ahmedifhaam/AI-103.

Treat the GitHub repository as the source of truth for the study plan, progress, schedule, weak areas, and topic gates. Treat the current conversation as the source of truth for what I actually learned in this session.

### Before updating

1. Read README.md.
2. Read PLAN/00-Master-Plan.md.
3. Read PLAN/01-Schedule.md.
4. Read PLAN/02-Progress.md.
5. Read PLAN/03-Exam-Strategy.md when relevant.
6. Read STUDY-SESSIONS/README.md if it exists.
7. Inspect the relevant date/session folder if it already exists.
8. Review the entire current study conversation and extract only things that were actually taught, asked, answered, corrected, or demonstrated.

### Core repository structure

Use this model:

```text
STUDY-SESSIONS/
├── README.md                         ← global session-tree index
│
├── YYYY-MM-DD/
│   ├── README.md                     ← date/session root summary
│   │
│   ├── 01-Generic-Topic.md           ← small topic branch/leaf
│   ├── 02-Generic-Topic.md
│   │
│   └── 03-Large-Topic/
│       ├── README.md                 ← topic summary/root
│       ├── 01-Subtopic.md
│       ├── 02-Subtopic.md
│       └── 03-Subtopic.md
```

Do NOT put detailed session transcripts into `PLAN/02-Progress.md`.

### Tree / branching rules

1. **Every study date gets one root `README.md`.**
2. The date root must summarize the day's major topics, results, important mental models, weak areas, and next target.
3. **Generic topics must be branched by meaningful subtopics**, not dumped into one large file.
   - Example: `Agent Tools + RAG` → Agents, Tools, Function Calling, OpenAPI, RAG, Chunking, Embeddings, Vector Search.
   - Example: `Foundry Security` → API Keys, Entra ID, Managed Identity, RBAC, Connections, Agent Identity.
4. If a topic is small, use a single `.md` leaf.
5. If a topic becomes large or contains several independent concepts, convert it into a folder with `README.md` plus subtopic files.
6. **Summarize upward.** A parent README should contain a concise synthesis of its children, not duplicate every detail.
7. Link parent → child and date root → topic branches.
8. Avoid duplication. The same detailed fact/question should have one natural home in the tree.
9. Preserve previous session history. Never erase a previous session merely to reorganize it.
10. When reorganizing an existing session, move its detailed evidence into the tree and leave only the summary/navigation in `PLAN/02-Progress.md`.

### Current-session logging

For the current conversation:

1. Determine the date/session root.
2. Identify the major topics actually covered.
3. Create or update the appropriate topic branches.
4. Put detailed evidence at the lowest sensible level.
5. Update the date root `README.md` with a concise summary of the branches.
6. Update `STUDY-SESSIONS/README.md` with the new date if needed.
7. Update `PLAN/02-Progress.md` only with dashboard-level progress and links to the session tree.

### What every detailed topic leaf should capture

Only when applicable to the actual conversation:

- Date
- Topic / subtopic
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
- Corrections / clarifications given
- Misconceptions / weak areas discovered
- Concepts improved from earlier sessions
- Current confidence if explicitly established
- Hands-on status
- Topic-gate status
- Next learning target

For questions, preserve the substance of the question and answer. Do not merely write "quiz passed" and do not copy the conversation verbatim.

### Root-summary requirements

Every parent/date/topic README should answer, briefly:

- What was learned?
- What is the mental model?
- What was demonstrated successfully?
- What remains weak/open?
- What branches contain the detail?
- What should be learned next?

The root is a **summary and map**, not a second transcript.

### Progress dashboard requirements

Keep `PLAN/02-Progress.md` concise. It should contain:

- Overall readiness
- Domain progress
- Current status
- Completed checkpoints
- Daily/session index with short entries
- Weak Area Queue
- Next Learning Target
- Topic-gate status
- Links to detailed session roots

Do NOT append full teaching notes, all questions, diagrams, or long corrections to the dashboard.

Keep progress conservative. Discussion alone does NOT make a topic mastered.

If hands-on work or the required quick-check score is missing, keep the gate open/in progress.

### Teaching-style record

When actually used, preserve the learning philosophy:

VISUAL MODEL → SHORT EXPLANATION → EXAMPLE → HANDS-ON → QUICK CHECK → TOPIC GATE

Record useful patterns such as:
- ASCII architecture diagrams
- short comparison tables
- exam-trap distinctions
- scenario questions
- immediate correction after an answer
- concise mental models / rules to retain

Do not invent a teaching method that was not used.

### Reorganization rule

When asked to reorganize existing history:

1. Read the existing dashboard and session history.
2. Create the new `STUDY-SESSIONS/` tree.
3. Preserve the actual evidence while moving details into appropriate topic branches.
4. Replace the old verbose session sections in `PLAN/02-Progress.md` with concise summaries and links.
5. Do not create duplicate copies of the same detailed session evidence.
6. Verify that every historical session still has a navigable root.

### README requirement

README.md must contain a link to this prompt under Start Here so the workflow is easy to find for future sessions.

### Output behavior

After making the repository changes:
1. Report which files/folders were created or updated.
2. Show the resulting session-tree structure briefly.
3. Summarize the newly logged session.
4. State the current learning target and weak areas.
5. Mention any topic gate that remains open and why.

Do not claim mastery merely because the conversation went well.
```

## Logging standard

The goal is:

**conversation → structured topic evidence → hierarchical session tree → concise progress dashboard**

The repository should let a future learner start at the root, understand the session quickly, and drill down only into the topic/subtopic details needed for review. Preserve the user's reasoning and the teaching/correction loop because these are useful evidence for recurring exam traps.

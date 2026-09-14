# AI-103 Master Plan

## Target

Prepare for **Exam AI-103: Developing AI Apps and Agents on Azure** using a visual-first, hands-on approach.

**Target exam date:** 2026-10-05

**Core learning deadline:** 2026-09-30

The final days are deliberately reserved for recovery, mocks, weak-area repair, and revision. This prevents one bad day from breaking the entire plan.

## Exam Weighting

| Domain | Weight | Priority |
|---|---:|---|
| Plan and manage an Azure AI solution | 25–30% | 🔴 |
| Generative AI and agentic solutions | 30–35% | 🔴 |
| Computer vision solutions | 10–15% | 🟠 |
| Text analysis solutions | 10–15% | 🟠 |
| Information extraction solutions | 10–15% | 🟠 |

## How We Study

Every topic follows the same gate:

```text
┌──────────────────┐
│ 1. VISUAL MODEL  │  ← architecture / flow / comparison
└────────┬─────────┘
         ↓
┌──────────────────┐
│ 2. CORE CONCEPT  │  ← short explanation only
└────────┬─────────┘
         ↓
┌──────────────────┐
│ 3. AZURE CHOICE  │  ← which service and why
└────────┬─────────┘
         ↓
┌──────────────────┐
│ 4. HANDS-ON      │  ← build / inspect / modify
└────────┬─────────┘
         ↓
┌──────────────────┐
│ 5. QUICK CHECK   │  ← 5–10 questions
└────────┬─────────┘
         ↓
┌──────────────────┐
│ 6. TOPIC GATE    │  ← ≥80% + explain choice
└──────────────────┘
```

## Retention System

Each new session begins with:

1. Five questions from the previous session.
2. One weak-area question.
3. One service-selection scenario.
4. Then new material.

A topic can be marked complete only when the gate is passed.

## Core Topics

### 01 — Plan and Manage

- Microsoft Foundry architecture and projects
- Model selection and deployments
- AI infrastructure
- Identity, managed identity, RBAC and keyless access
- Quotas, scaling, rate limits and cost
- Monitoring, tracing and evaluation
- Responsible AI, safety and guardrails
- Retrieval/indexing choices
- CI/CD for AI solutions

### 02 — Generative AI and Agents

- LLMs, small language models and multimodal models
- Prompt engineering
- Generation parameters
- Foundry SDKs and application integration
- RAG
- Azure AI Search grounding
- Tools and function calling
- Agent instructions, roles and goals
- Conversation state and memory
- Retrieval + tools + memory
- Multi-agent orchestration
- Human approval / safeguards
- Agent evaluation and observability

### 03 — Computer Vision

- Multimodal image understanding
- Image analysis and captions
- Structured JSON extraction from images
- Image generation/editing
- Video generation/editing
- Speech as a modality
- Speech-to-text / text-to-speech
- Audio reasoning

### 04 — Text Analysis

- Natural language processing patterns
- Translation
- Sentiment, entities, key phrases and summaries
- Text classification/extraction
- Speech/language integration

### 05 — Information Extraction

- OCR
- Document Intelligence
- Layout analysis
- Field extraction
- Content Understanding
- Structured/Markdown outputs
- Document/image/audio/video ingestion
- Semantic, vector and hybrid search
- RAG ingestion pipelines

## Hands-On Projects

We will build a small set of reusable labs rather than dozens of disconnected tutorials:

1. **Foundry App** — connect an application to a deployed model.
2. **RAG App** — ingest → index → retrieve → ground → answer.
3. **Agent** — instructions + tools + retrieval + conversation state.
4. **Multimodal App** — image/audio input → structured response.
5. **Document Pipeline** — OCR/layout/fields → grounded structured output.

## Definition of Ready

Before the final revision phase, the target is:

- ≥85% average on topic checks
- ≥80% on every major domain
- Can choose the appropriate Azure service from a scenario
- Can explain RAG architecture without notes
- Can explain agent/tool/memory architecture without notes
- Can recognize the major vision, language and extraction services
- At least two full timed mock exams completed
- All persistent weak areas have a remediation note

## Official Ground Truth

Use Microsoft's AI-103 study guide as the authoritative exam-objective source. The current skills measured date is April 16, 2026.

Official study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-103

Official course: https://learn.microsoft.com/en-us/training/courses/ai-103t00

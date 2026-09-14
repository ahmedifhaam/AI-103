# AI-103 Exam Strategy

## What the Exam Is Testing

The exam is not just asking whether you remember definitions. Expect scenario-based decisions such as:

```text
Requirement
   ↓
Constraints
(cost / latency / modality / security / grounding)
   ↓
Service / model / architecture choice
   ↓
Implementation detail
   ↓
Operational / responsible-AI consideration
```

## Service Selection Method

For every scenario ask, in order:

1. **What is the input?** text / image / audio / video / document / mixed
2. **What is the output?** classification / extraction / generation / search / conversation
3. **Does it need grounding?**
4. **Does it need an agent?**
5. **Does it need deterministic extraction?**
6. **What are the security/cost/latency constraints?**
7. **Which Azure service is purpose-built for this requirement?**

## High-Value Comparisons

These must become instant-recognition topics:

- LLM vs small language model vs multimodal model
- Model deployment choices
- RAG vs model fine-tuning
- Keyword vs semantic vs vector vs hybrid search
- Search vs agent tool
- Function calling vs retrieval
- Conversation state vs long-term knowledge
- OCR vs Document Intelligence vs Content Understanding
- Generative multimodal model vs specialized vision capability
- Speech-to-text vs translation vs language analysis
- Evaluation vs monitoring vs tracing
- Guardrail vs human approval

## Exam Trap Rules

- Do not choose a more general service when a purpose-built service directly satisfies the requirement.
- Separate **retrieval** from **generation**.
- Separate **agent orchestration** from ordinary LLM prompting.
- Treat security and identity requirements as first-class constraints.
- Read every requirement and constraint before choosing a service.
- Watch for words such as **structured**, **grounded**, **real-time**, **multimodal**, **private**, **cost**, **scale**, and **human approval**.

## Final-Day Rule

No major new topic on October 4. Use visual recall, service-selection drills, mistake review, and confidence checks.

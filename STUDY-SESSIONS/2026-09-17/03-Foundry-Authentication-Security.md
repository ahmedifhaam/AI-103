# 03 — Microsoft Foundry Authentication + Security

## Objective
Understand API keys, Microsoft Entra ID, managed identity, RBAC, project connections, and agent identity.

## Teaching Method
Visual identity/authentication/authorization flow, API-key vs Entra comparison, managed-identity contrast, concise mental models, architecture examples, and exam-oriented scenarios.

## Mental Model
```text
WHO?
  ↓
Identity (user / app / managed identity / agent)
  ↓ authentication
Microsoft Entra ID
  ↓ token
Azure resource / API / tool
  ↓ authorization
RBAC
```

## Concepts Learned
- API keys are shared secrets and require secure storage/rotation.
- Entra ID provides identity-based authentication and integrates with RBAC.
- Managed identity is an Azure-managed identity using Entra ID; it reduces stored credentials.
- RBAC controls permissions for an authenticated identity.
- Foundry project connections configure project-scoped access to external resources such as Azure AI Search; the external resource remains external.
- Agent identity can provide an Entra identity for downstream access.
- Agent tool selection and downstream authorization are separate concerns.

## Exam Rules
```text
Entra ID         → identity platform
Managed Identity → Azure-managed identity using Entra ID
RBAC             → permissions
API key          → shared secret

Authentication   → WHO are you?
Authorization    → WHAT can you do?
```

Common pattern:
> Azure-hosted app + no secrets in configuration → **Managed Identity + Entra ID + RBAC**.

## Examples
- Application → API key → Foundry.
- Application → Entra ID → access token → Foundry → RBAC.
- App Service → managed identity → Entra token → Azure resource.
- User → Agent → Search / business API, with separate authorization boundaries.

## Checkpoint Questions
The six questions asked at the end of the session were not answered during the logged session, so results remain pending.

1. Azure-hosted web app calls Foundry without stored API keys — choose authentication approach. **Pending.**
2. Difference between authentication and authorization. **Pending.**
3. Local development: API key or Entra ID as the simpler option? **Pending.**
4. App Service accesses Azure AI Search without stored credentials — choose Azure capability. **Pending.**
5. Agent accesses Storage with least required permissions — identify two concepts. **Pending.**
6. Complete `App Service → ??? → Microsoft Entra ID → ??? → Foundry` and explain managed identity. **Pending.**

## Gate
🟡 **Open.** Concepts taught, but checkpoint answers and hands-on work remain incomplete.

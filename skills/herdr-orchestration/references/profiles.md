# Profiles and bindings

Normative behavior lives in [mode.md](mode.md). This file is the surface/model precedence matrix and configuration notes.

## Precedence

1. Explicit user instruction for model / harness / profile.
2. Selected main-agent model identity (verified at runtime when possible).
3. Reference surface preset below.
4. Local `examples/config.example.json` bindings (pane labels, session name, judgment model id).

Do **not** infer “we are on Cursor ⇒ Auto-main” if the user selected a different main model. Do **not** treat Hermes or Claude loading this skill as proof they can run the full Auto-main or Sol-main path.

## Reference role matrix

| Profile | Conversation owner | Plan gate | Implementation | Closing alignment | Final acceptance |
|---|---|---|---|---|---|
| **Astra-main** | Astra | N/A (already judgment) | Ordinary pool | Optional / as needed for ordinary-owned material work | Astra |
| **Sol-main** | Sol-class coordinator | Early judgment session before plan lock | Ordinary pool + optional judgment-owned core | When ordinary owns material outcomes, core changed, or uncertain—unless final combined result already reviewed | Sol-class coordinator |
| **Auto-main** | Auto | Early judgment session before plan lock | Ordinary pool only (Astra does not implement) | Required for substantive jobs after mandatory checks | Auto |

## Supported reference bindings (configure locally)

| Binding key | Purpose | Notes |
|---|---|---|
| `session` | Herdr session name | Discover live; do not hardcode foreign hosts |
| `judgment_slots` | Pane labels for plan/closing | Verify model banner each start |
| `ordinary_pool` | Pane labels for execution | Prefer fit over broadcast |
| `claims_state_dir` | Shared claims namespace | Must be identical across cooperating coordinators on the server host |
| `judgment_model` | Expected model id + effort | Wrong/missing ⇒ blocker, no substitute |

Alternative model-role policies are **explicit adaptations**, not equivalent-intelligence claims. Document any adaptation in your private config; do not pretend it matches this reference package.

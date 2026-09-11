# Herdr Orchestration

Portable **coordinator orchestration policy** for Herdr worker fleets: **Astra-main**, **Sol-main**, and **Auto-main**.

This repository is the installable companion for agents that already use (or will use) [Herdr](https://github.com/search?q=herdr) as a terminal/agent multiplexer. It does **not** ship the Herdr binary, credentials, model subscriptions, or a worker pool.

**Stock `herdr` skill** = CLI / product authority.  
**This skill (`herdr-orchestration`)** = how a main agent claims panes, gates plans with Astra (when applicable), routes ordinary work, verifies results, and accepts—without recursive worker delegation.

Policy freeze: contract **v3.32** — see [`SOURCE-REVISION.md`](SOURCE-REVISION.md).

## Prerequisites

| Requirement | Notes |
|---|---|
| Herdr CLI installed and a reachable session | Verified separately; this package does not install it |
| Python 3.10+ | For `scripts/claims.py` and tests |
| macOS or Linux (POSIX) | Claims use `fcntl`; Windows adapter not in MVP |
| Configured judgment + ordinary routes | Missing Astra (when required) is a **blocker**, not a silent substitute |
| Shared host-local claims directory | All cooperating coordinators must share one namespace on the Herdr **server host** |

## Agent quickstart (point an agent here)

Paste something like:

> Read this repository `README.md` and `skills/herdr-orchestration/SKILL.md`. Inspect my harness skill location and existing Herdr setup. Install this skill without overwriting existing skills, configure only my selected coordinator profile and worker routes, and verify discovery and prerequisites. Do not launch workers or change my global defaults merely to install.

Then follow [`skills/herdr-orchestration/references/install.md`](skills/herdr-orchestration/references/install.md).

### Proposed installer path (verify on your harness)

```bash
npx skills add btcjon/herdr-orchestration --list
npx skills add btcjon/herdr-orchestration --skill herdr-orchestration
```

Manual: clone a tagged release, then link or copy **only** `skills/herdr-orchestration` into your harness skill directory. Never overwrite an existing destination.

### Activation (separate from install)

- Conversation controls: `Herdr mode on` | `off` | `status` (instruction policy, not a Herdr CLI switch).
- Optional default-on for future sessions: install [`skills/herdr-orchestration/CONTRACT-SNIPPET.md`](skills/herdr-orchestration/CONTRACT-SNIPPET.md) into your global agent contract **only when you explicitly want that**.
- Normal install does **not** alter global defaults, permissions, or auto-start workers.

## Profiles (reference)

| Main agent surface | Default coordinator | Profile |
|---|---|---|
| Codex (primary user chat) | Sol-class long coordinator | **Sol-main** |
| Cursor (primary user chat) | Auto | **Auto-main** |
| Codex with Astra as the main model | Astra | **Astra-main** |

Explicit user model/harness routing wins. Do not infer model identity from the app alone. Details: [`skills/herdr-orchestration/references/profiles.md`](skills/herdr-orchestration/references/profiles.md).

## Support matrix (honest)

| Combination | Status in 0.1.0 |
|---|---|
| Package offline checks + claims unit tests | **Verified** via `scripts/check_package.py` and `tests/test_claims.py` |
| Codex / Cursor / Hermes / Claude discovery | Documented; treat as **unverified** until you run the install path on that harness |
| End-to-end live Herdr canary | **Host-specific**; not claimed for all users by this release |

## Layout

```text
skills/herdr-orchestration/     # installable skill
  SKILL.md
  CONTRACT-SNIPPET.md           # opt-in global fragment
  references/                   # mode, profiles, packets, claims, runbooks, install, adapters
  scripts/claims.py
  examples/                     # synthetic only
tests/                          # claims + policy scenarios + traceability
scripts/check_package.py
```

## Catalog note

The public [`custom-skills`](https://github.com/btcjon/custom-skills) repo may link here for discovery. This repository remains the **authoritative** portable package—no mirrored skill tree inside custom-skills.

## License

MIT — see [`LICENSE`](LICENSE).

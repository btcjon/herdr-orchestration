# Install

Installation, activation, and worker provisioning are **separate** steps. Install alone must not launch agents, change global contracts, bypass sandboxing, enroll remote hosts, or enable default-on Herdr.

## 1. Obtain the package

```bash
# Proposed skills CLI (verify on your harness; not all environments support it)
npx skills add btcjon/herdr-orchestration --list
npx skills add btcjon/herdr-orchestration --skill herdr-orchestration
```

Manual:

```bash
git clone https://github.com/btcjon/herdr-orchestration.git
# link or copy ONLY skills/herdr-orchestration into your harness skill directory
# resolve that directory from your harness docs — do not assume one path
```

Never overwrite an existing destination skill. Verify relative references (`references/`, `scripts/`) remain inside the installed package.

## 2. Harness discovery (document per harness)

| Harness | Load notes | 0.1.0 verification |
|---|---|---|
| Cursor | Project/user skills or linked skill dir; reload agent session | Documented; verify locally |
| Codex | Skills path per Codex docs; new session | Documented; verify locally |
| Hermes | Symlink into Hermes skills dir; `skill_view` / equivalent | Documented; verify locally |
| Claude | Skills / plugin path per product docs | Documented; verify locally |

Treat combinations as **unverified** until you run discovery on that harness. Reload after install. Pin to a git tag for updates; remove only package-owned links/snippets on uninstall.

## 3. Read-only prerequisite checks

After load, check without launching workers:

- `herdr --help` / version
- Reachable selected session
- Python/platform (POSIX for claims)
- Judgment + ordinary routes configured (or honest “missing” status)
- Shared claims `--state-dir` agreed among coordinators
- Permission policy understood

## 4. Activation (optional)

- Per conversation: `Herdr mode on|off|status`
- Default-on for future sessions: explicitly merge [CONTRACT-SNIPPET.md](../CONTRACT-SNIPPET.md) into your global contract

## 5. Offline package verification

```bash
cd /path/to/herdr-orchestration
python3 scripts/check_package.py
python3 -m unittest discover -s tests -t .
```

## Troubleshooting

| Symptom | Action |
|---|---|
| Skill not discovered | Confirm link target is the `herdr-orchestration` package dir containing `SKILL.md` |
| Broken relative links | Do not flatten `references/` away from `SKILL.md` |
| Duplicate dispatches | Align `--state-dir` on the server host |
| `fcntl` / claims errors on Windows | Unsupported in MVP |
| Missing Astra route | Disclose blocker; do not impersonate |

## Operators with a private control plane

If you already project skills from a private control plane, keep that authority for your hosts. Prefer linking this public package or merging by hash-verified copy—do not run unattended `npx skills add` against production projections without review.

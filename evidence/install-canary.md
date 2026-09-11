# Isolated install canary (AC10)

Date: 2026-09-11
Supported combination documented: **manual git clone + symlink into a harness skill directory** on macOS, verified against this package tree (Cursor/Codex/Hermes-compatible layout: directory containing `SKILL.md`).

| Step | Result |
|---|---|
| Clone pinned `v0.1.0` into isolated temp | ok (pin in install-pin.txt) |
| Symlink `skills/herdr-orchestration` only | ok |
| Resolve `SKILL.md`, `references/mode.md`, `scripts/claims.py` | ok |
| Preexisting sibling skill untouched | ok |
| Remove package-owned symlink only | ok |
| Second checkout at main tip (update/pin contrast) | ok (install-update-head.txt) |

`npx skills add` path: **documented as proposed; not executed in this canary** (unverified).
Homebrew/product prerequisite: https://herdr.dev — `herdr 0.9.0` present on this host.
remote_clone_ok
Remote clone of github.com/btcjon/herdr-orchestration@v0.1.0: ok (2026-09-11T12:43Z)

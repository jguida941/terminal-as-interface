---
title: "Evidence Appendix"
permalink: /paper_appendix/
---

# The Terminal as Interface: Evidence Appendix

<nav class="paper-nav">
  <span>Navigation</span>
  <a href="../">&larr; 1. Overview</a>
  <a href="../paper_technical/">&larr; 2. Technical Companion</a>
  <a href="./" class="nav-active">3. Evidence Appendix</a>
</nav>

Return to the [public overview](../) or the [technical companion](../paper_technical/).

## Repository Snapshot

This appendix records the repository snapshot used in the current paper draft. The counts below were taken on March 7, 2026 from the local repository state used for writing.

1. `614` commits in the repository
2. `101` tags
3. `34` top level guard scripts named `check_*.py` in [dev/scripts/checks](https://github.com/jguida941/voiceterm/tree/master/dev/scripts/checks)
4. about `65,565` lines in [rust/src/bin/voiceterm](https://github.com/jguida941/voiceterm/tree/master/rust/src/bin/voiceterm)
5. about `42,974` lines in [dev/scripts/devctl](https://github.com/jguida941/voiceterm/tree/master/dev/scripts/devctl)

## Core Evidence Surfaces

Readers who want to verify the paper quickly should start with these files and directories.

1. [VoiceTerm repository](https://github.com/jguida941/voiceterm)
2. [AGENTS.md](https://github.com/jguida941/voiceterm/blob/master/AGENTS.md)
3. [dev/scripts/checks](https://github.com/jguida941/voiceterm/tree/master/dev/scripts/checks)
4. [check_rust_security_footguns.py](https://github.com/jguida941/voiceterm/blob/master/dev/scripts/checks/check_rust_security_footguns.py)
5. [check_rust_runtime_panic_policy.py](https://github.com/jguida941/voiceterm/blob/master/dev/scripts/checks/check_rust_runtime_panic_policy.py)
6. [AUTOMATION_DEBT_REGISTER.md](https://github.com/jguida941/voiceterm/blob/master/dev/audits/AUTOMATION_DEBT_REGISTER.md)
7. [ENGINEERING_EVOLUTION.md](https://github.com/jguida941/voiceterm/blob/master/dev/history/ENGINEERING_EVOLUTION.md)
8. [rust/src/audio](https://github.com/jguida941/voiceterm/tree/master/rust/src/audio)
9. [latency_measurement.rs](https://github.com/jguida941/voiceterm/blob/master/rust/src/bin/latency_measurement.rs)
10. [guides/USAGE.md](https://github.com/jguida941/voiceterm/blob/master/guides/USAGE.md)
11. [dev/scripts/devctl](https://github.com/jguida941/voiceterm/tree/master/dev/scripts/devctl)

## Claim To Evidence Map

### Claim 1

AI terminal tools act inside the same execution environment as the programmer.

Read:

1. [AGENTS.md](https://github.com/jguida941/voiceterm/blob/master/AGENTS.md)
2. [dev/scripts/devctl](https://github.com/jguida941/voiceterm/tree/master/dev/scripts/devctl)
3. [dev/scripts/checks](https://github.com/jguida941/voiceterm/tree/master/dev/scripts/checks)

### Claim 2

The repository encodes policy as executable checks rather than relying only on informal reviewer memory.

Read:

1. [check_rust_security_footguns.py](https://github.com/jguida941/voiceterm/blob/master/dev/scripts/checks/check_rust_security_footguns.py)
2. [check_rust_runtime_panic_policy.py](https://github.com/jguida941/voiceterm/blob/master/dev/scripts/checks/check_rust_runtime_panic_policy.py)
3. [AGENTS.md](https://github.com/jguida941/voiceterm/blob/master/AGENTS.md)

### Claim 3

Repeated workflow failures can be converted into durable tooling and explicit operational memory.

Read:

1. [AUTOMATION_DEBT_REGISTER.md](https://github.com/jguida941/voiceterm/blob/master/dev/audits/AUTOMATION_DEBT_REGISTER.md)
2. [ENGINEERING_EVOLUTION.md](https://github.com/jguida941/voiceterm/blob/master/dev/history/ENGINEERING_EVOLUTION.md)
3. [dev/audits](https://github.com/jguida941/voiceterm/tree/master/dev/audits)

### Claim 4

Voice input changes the character of programming by moving it closer to orchestration and review.

Read:

1. [rust/src/audio](https://github.com/jguida941/voiceterm/tree/master/rust/src/audio)
2. [guides/USAGE.md](https://github.com/jguida941/voiceterm/blob/master/guides/USAGE.md)
3. [latency_measurement.rs](https://github.com/jguida941/voiceterm/blob/master/rust/src/bin/latency_measurement.rs)

## Suggested Reading Paths

If you are a non technical reader:

1. Read the [public overview](../)
2. Read the Conclusion in the [technical companion](../paper_technical/)
3. Return here only if you want to inspect the source links

If you are a technical reader:

1. Read the [technical companion](../paper_technical/)
2. Use this appendix to verify claims and inspect the repository snapshot
3. Open the linked code and policy files directly

## Evidence Index

Every claim about VoiceTerm in this paper links to its source. For quick reference:

| Evidence | Link |
|---|---|
| VoiceTerm repository | [github.com/jguida941/voiceterm](https://github.com/jguida941/voiceterm) |
| Rust source (~87K LOC) | [rust/src/bin/voiceterm/](https://github.com/jguida941/voiceterm/tree/master/rust/src/bin/voiceterm) |
| Python tooling (~55K LOC) | [dev/scripts/devctl/](https://github.com/jguida941/voiceterm/tree/master/dev/scripts/devctl) |
| 34 guard scripts | [dev/scripts/checks/](https://github.com/jguida941/voiceterm/tree/master/dev/scripts/checks) |
| Security footguns check | [check_rust_security_footguns.py](https://github.com/jguida941/voiceterm/blob/master/dev/scripts/checks/check_rust_security_footguns.py) |
| Panic policy check | [check_rust_runtime_panic_policy.py](https://github.com/jguida941/voiceterm/blob/master/dev/scripts/checks/check_rust_runtime_panic_policy.py) |
| Policy file (AGENTS.md) | [AGENTS.md](https://github.com/jguida941/voiceterm/blob/master/AGENTS.md) |
| 12-step SOP | [Mandatory 12-step SOP](https://github.com/jguida941/voiceterm/blob/master/AGENTS.md#mandatory-12-step-sop-always) |
| AI operating contract | [AI operating contract](https://github.com/jguida941/voiceterm/blob/master/AGENTS.md#ai-operating-contract-required) |
| Error recovery protocol | [Error recovery protocol](https://github.com/jguida941/voiceterm/blob/master/AGENTS.md#error-recovery-protocol) |
| Task router | [Task router](https://github.com/jguida941/voiceterm/blob/master/AGENTS.md#task-router-pick-one-class) |
| Continuous improvement loop | [Continuous improvement loop](https://github.com/jguida941/voiceterm/blob/master/AGENTS.md#continuous-improvement-loop-required) |
| Automation debt register | [AUTOMATION_DEBT_REGISTER.md](https://github.com/jguida941/voiceterm/blob/master/dev/audits/AUTOMATION_DEBT_REGISTER.md) |
| Audit program | [dev/audits/](https://github.com/jguida941/voiceterm/tree/master/dev/audits) |
| Engineering timeline | [ENGINEERING_EVOLUTION.md](https://github.com/jguida941/voiceterm/blob/master/dev/history/ENGINEERING_EVOLUTION.md) |
| Changelog | [CHANGELOG.md](https://github.com/jguida941/voiceterm/blob/master/dev/CHANGELOG.md) |
| Audio/voice pipeline | [rust/src/audio/](https://github.com/jguida941/voiceterm/tree/master/rust/src/audio) |
| Latency measurement tool | [latency_measurement.rs](https://github.com/jguida941/voiceterm/blob/master/rust/src/bin/latency_measurement.rs) |
| Usage guide (voice input) | [USAGE.md](https://github.com/jguida941/voiceterm/blob/master/guides/USAGE.md) |

## Revision Note

Any quantitative statement in the paper should keep a date attached to it. The repository is active, so counts will change over time.

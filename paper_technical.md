---
title: "Reader Guide"
permalink: /paper_technical/
---

{% assign vt = site.data.voiceterm_snapshot %}

# The Terminal as Interface: Reader Guide

Return to the [full paper](../) or jump to the [evidence appendix](../paper_appendix/).

This page is intentionally not a second paper. The root page now contains the
full narrative, all major figures, the technical argument, the limits section,
and a built-in evidence map. This guide remains only to help different readers
enter that long paper efficiently.

## Best Reading Paths

### Nontechnical Reader

Start with:

1. [Why This Matters](../#stakes)
2. [The Controlled System VoiceTerm Actually Exposes](../#control-system)
3. [VoiceTerm as a Governed Case Study](../#voiceterm)
4. [Who Is Affected and How Work Changes](../#labor)
5. [Conclusion](../#conclusion)

### Technical Reader

Start with:

1. [Abstract](../#abstract)
2. [Scope and Method](../#method)
3. [The Controlled System VoiceTerm Actually Exposes](../#control-system)
4. [CI/CD Makes the Policy Durable](../#cicd)
5. [Workflow Example](../#workflow)
6. [Limits and Threats to Validity](../#limits)

### Governance / Process Reader

Start with:

1. [Why This Matters](../#stakes)
2. [Scope and Method](../#method)
3. [CI/CD Makes the Policy Durable](../#cicd)
4. [Workflow Example](../#workflow)
5. [Evidence Map](../#evidence)

### Verification Reader

Start with:

1. [Scope and Method](../#method)
2. [Evidence Map](../#evidence)
3. [Evidence Appendix](../paper_appendix/)

## Figure Guide

The main paper contains every major figure used across the site's history.

1. [Figure 1. Tool comparison matrix](../#stakes)
2. [Figure 2. VoiceTerm control plane map](../#control-system)
3. [Figure 3. VoiceTerm HUD example](../#voiceterm)
4. [Figure 4. Repository governance loop](../#workflow)
5. [Figure 5. Interface history timeline](../#history)

## Snapshot Summary

The current published revision pulls a VoiceTerm snapshot during site deploy and
currently reflects:

1. `{{ vt.stats.commits.display }}` commits
2. `{{ vt.stats.tags.display }}` tags
3. `{{ vt.stats.guard_scripts.display }}` top-level `check_*.py` guard scripts
4. `{{ vt.stats.workflows.display }}` GitHub Actions workflow files
5. `{{ vt.stats.bundle_classes.display }}` routed task classes
6. about `{{ vt.stats.rust_runtime_lines.display }}` lines under `rust/src/bin/voiceterm`
7. `{{ vt.stats.devctl_lines.display }}` lines of source and docs under `dev/scripts/devctl`

## Why This Page Still Exists

Earlier iterations of the site split the argument across overview and technical
pages. That structure made the paper easier to skim but easier to lose. This
page remains only for reader orientation and backward compatibility. The actual
paper now lives at [the root page](../).

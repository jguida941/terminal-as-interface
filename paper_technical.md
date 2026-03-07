---
title: "Reader Guide"
permalink: /paper_technical/
---

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
2. [Introduction: From User to Builder](../#introduction)
3. [How AI CLI Tools Actually Work](../#mechanics)
4. [Who Is Affected and How Work Changes](../#labor)
5. [Conclusion](../#conclusion)

### Technical Reader

Start with:

1. [Abstract](../#abstract)
2. [Scope and Method](../#method)
3. [How AI CLI Tools Actually Work](../#mechanics)
4. [VoiceTerm as a Case Study](../#voiceterm)
5. [Workflow Example](../#workflow)
6. [Limits and Threats to Validity](../#limits)

### Governance / Process Reader

Start with:

1. [Why This Matters](../#stakes)
2. [VoiceTerm as a Case Study](../#voiceterm)
3. [Workflow Example](../#workflow)
4. [Evidence Map](../#evidence)

### Verification Reader

Start with:

1. [Scope and Method](../#method)
2. [Evidence Map](../#evidence)
3. [Evidence Appendix](../paper_appendix/)

## Figure Guide

The main paper contains every major figure used across the site's history.

1. [Figure 1. Tool comparison matrix](../#stakes)
2. [Figure 2. Terminal control loop](../#mechanics)
3. [Figure 3. VoiceTerm system model](../#voiceterm)
4. [Figure 4. VoiceTerm HUD example](../#voiceterm)
5. [Figure 5. Voice-driven prompt entry](../#voiceterm)
6. [Figure 6. How failure becomes policy](../#workflow)
7. [Figure 7. Interface history timeline](../#history)

## Snapshot Summary

The March 7, 2026 paper revision was rechecked against the local VoiceTerm
source tree used for writing and reflects:

1. `616` commits
2. `101` tags
3. `35` top-level `check_*.py` guard scripts
4. about `65,741` lines under `rust/src/bin/voiceterm`
5. over `44,000` lines of source and docs under `dev/scripts/devctl`

## Why This Page Still Exists

Earlier iterations of the site split the argument across overview and technical
pages. That structure made the paper easier to skim but easier to lose. This
page remains only for reader orientation and backward compatibility. The actual
paper now lives at [the root page](../).

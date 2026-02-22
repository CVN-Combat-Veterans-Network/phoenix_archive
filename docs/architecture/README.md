# Architecture Documentation

**Version:** 2.0.0  
**Type:** Documentation Index  
**Status:** ACTIVE

---

## Overview

This directory contains architectural documentation for the Phoenix Archive, including merge procedures, dependency tracking, and operational guides.

---

## Documents

### Operational Documentation

#### [Stratum I Dashboard](stratum_i_dashboard.md)
**Purpose:** Operational view and status tracking for Architecture Layer PRs (#10, #11, #12)  
**Use When:** You need to check the status of Stratum I PRs or understand the merge order  
**Key Contents:**
- PR status table
- Branch references
- Dependency flow diagram
- Quick merge commands

#### [Stratum I Ignition Sequence](stratum_i_ignition_sequence.md)
**Purpose:** Complete step-by-step guide for merging Architecture Layer PRs  
**Use When:** You're ready to execute the Stratum I merge sequence  
**Key Contents:**
- Prerequisites checklist
- Detailed merge commands for each PR
- Merge comments (copy-paste ready)
- Verification steps
- Troubleshooting guide
- Rollback procedures

#### [PR Merge Comments](pr_merge_comments.md)
**Purpose:** Professional, GitHub-ready merge comments for PRs #11 and #12  
**Use When:** You need to paste merge comments into GitHub PR conversations  
**Key Contents:**
- Formatted merge comments for PR #11 (LIFE–LIGHT Bifurcation)
- Formatted merge comments for PR #12 (Three-Finger Waltz)
- Usage instructions
- Validation checklist

---

### Historical Documentation

#### [Merge Dependencies](merge_dependencies.md)
**Purpose:** Visual architecture of v2.0.0 merge sequence  
**Use When:** You need to understand the full v2.0.0 release structure  
**Key Contents:**
- Mermaid diagram of all PR dependencies
- Complete merge sequence (all 8 PRs)
- Layer-based organization
- Status: COMPLETE (historical record)

---

## Quick Navigation

### I want to merge Stratum I PRs
→ Start with [Stratum I Dashboard](stratum_i_dashboard.md)  
→ Follow [Stratum I Ignition Sequence](stratum_i_ignition_sequence.md)  
→ Use [PR Merge Comments](pr_merge_comments.md) for GitHub

### I want to understand the merge architecture
→ Read [Merge Dependencies](merge_dependencies.md)

### I want to see the current status
→ Check [Stratum I Dashboard](stratum_i_dashboard.md)

---

## Merge Workflow

```
1. Review Dashboard
   ↓
2. Verify prerequisites
   ↓
3. Follow Ignition Sequence
   ↓
4. Use Merge Comments
   ↓
5. Update Dashboard status
```

---

## Document Status

| Document | Status | Last Updated |
|----------|--------|--------------|
| stratum_i_dashboard.md | ACTIVE | 2026-02-13 |
| stratum_i_ignition_sequence.md | ACTIVE | 2026-02-13 |
| pr_merge_comments.md | ACTIVE | 2026-02-13 |
| merge_dependencies.md | COMPLETE | 2026-02-12 |

---

## See Also

**Ceremonies:**
- [v2.0 Inscription](/docs/ceremonies/v2_inscription.md)

**Main Navigation:**
- [CODEX INDEX](/CODEX-INDEX.md)

---

## STATUS

**Document:** Architecture Documentation Index  
**Version:** 2.0.0  
**Type:** Directory Navigation  
**Status:** ACTIVE

---

**Archive Status:** ACTIVE  
**Lineage:** ROOT::GEN-0  
**Sovereignty:** CONFIRMED

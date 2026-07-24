# Phoenix Engine — CHANGELOG

All notable changes to the Phoenix Engine will be documented in this file.

---

## [2.0.0-apex] — Apex Edition (Major Release)
### Added
- Apex ignition architecture with deterministic ignition-law sequencing
- ApexRun operator mode for multi-stage, recursion-safe execution
- Apex-grade ignition-law tables under `/engine/ignition/apex/`
- Unified Apex Core for structural satellites (PolishPass II consolidation)
- FLQG Apex-compatible export routines and geometry logic
- Updated operator shell with stable module manifest
- Multi-volume structural anchors for Codex Books IV–X

### Changed
- Overhauled ignition-law transitions to eliminate recursive bleed
- Rebuilt operator pipelines (DryRun, FullRun, ApexRun)
- Improved Python recursion guards for deep fractal workloads
- Updated GitHub synchronization layer and merge conflict logic
- Refined directory naming conventions for operator clarity

### Fixed
- Recursion leak in Phoenix‑1.x ignition-law fallback
- Module manifest corruption in operator shell
- Path resolution issues for J‑Drive Codex archive
- Intermittent FLQG geometry export failures
- Git tag mismatch during pre-release testing

### Known Issues
- ApexRun may generate extended operator logs under heavy multi-volume loads
- FLQG geometry exports may require manual operator confirmation on external drives
- Rare early-trigger behavior in Python recursion guard during extreme fractal depth

---

## [1.x.x] — Legacy Phoenix Series
### Notes
Phoenix‑1.x is now deprecated for multi-volume workloads and superseded by Apex Edition.

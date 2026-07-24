# Polish Pass II → III Migration Checklist

## 1. Registry and naming

- **Verify NOD names**
  - Ensure all NODs used in operator scripts exist in `nod_registry.py`.
  - Deprecate ad‑hoc or legacy names; map them to canonical Third Pillar NODs.
- **Align categories and versions**
  - Confirm each NOD has a clear `category` and `version` for auditability.

## 2. Operator surfaces

- **PowerShell**
  - Update scripts to use `Invoke-PhoenixNod` and `Get-PhoenixNod`.
  - Remove direct kernel calls; route everything through the Third Pillar.
- **Python**
  - Replace manual NOD tables with `get_nod` / `list_nods`.
  - Centralize context construction for reuse across NODs.

## 3. Documentation

- **Third Pillar docs**
  - Extend `Third Pillar Additions (v2.2-v2.4).md` with Pass III changes.
  - Document any new NODs or changed semantics.
- **RELEASES**
  - Create `RELEASES/v2.3.0.md` with explicit migration notes from Pass II → III.

## 4. Testing

- **Registry tests**
  - Expand `test_nod_registry.py` to cover new Pass III NODs.
- **Operator integration**
  - Add tests (or manual runs) for PowerShell loader and Python entrypoints.

## 5. Cleanup and deprecation

- Remove unused legacy scripts that bypass the Third Pillar.
- Mark any transitional NODs as deprecated and schedule removal in v2.4.0.

## 6. Final validation

- Run a full Phoenix operator pipeline using only Third Pillar surfaces.
- Confirm outputs match or exceed Pass II quality and coherence.

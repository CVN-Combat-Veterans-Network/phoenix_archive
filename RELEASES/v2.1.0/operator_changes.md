# Operator Changes — v2.1.0

Complete list of operator additions, modifications, and enhancements in v2.1.0.

## New Operators

### LNS Family
- **LNS_BIND** — Immutable binding operations
  - Purpose: Create immutable bindings between operators
  - Pattern: `(source, target, binding_type) → immutable_binding`
  - Use case: Provenance tracking, audit trails

- **LNS_TRACE** — Provenance tracking
  - Purpose: Track operator invocation lineage
  - Pattern: `(operator, context) → trace_record`
  - Use case: Debugging, audit compliance

### HGN Family (Hydrogenesi)
- **HGN_PROPAGATE** — Wave-based propagation
  - Purpose: Propagate changes across distributed systems
  - Pattern: `(state, propagation_mode) → wave_distribution`
  - Use case: Distributed state synchronization

- **HGN_RESOLVE** — Distributed consensus resolution
  - Purpose: Resolve conflicts in distributed operator states
  - Pattern: `(conflict_set, resolution_strategy) → resolved_state`
  - Use case: Consistency enforcement

### PHX Family (Phoenix)
- **PHX_RENEW** — Lightweight identity renewal
  - Purpose: Refresh identity without full ignition cycle
  - Pattern: `(identity, renewal_scope) → renewed_identity`
  - Use case: Incremental identity updates

- **PHX_VECTOR** — Directed evolutionary transformation
  - Purpose: Apply directional transformation to identity
  - Pattern: `(identity, direction, magnitude) → transformed_identity`
  - Use case: Controlled identity evolution

### Meta-Operators (Stratum IV)
- **Meta-Operator I — Invariance**
  - Purpose: Maintain structural identity across transformations
  - Pattern: `(state, context, transform) → (stabilized_state, drift_delta, stability_score)`
  - Mechanism: Kernel identity projection → transform → invariance check → stabilization
  - Scoring: `stability_score = 1.0 - (drift / max_drift)`
  - Outcomes:
    - Accept: ≥0.8
    - Partial: 0.3-0.8
    - Reject: <0.3

## Enhanced Operators

### Phoenix Operators
- All Phoenix operators now include STATUS metadata blocks
- Documentation standardized with operator type, scale, version, pattern

### Hydrogenesi Operators
- All Hydrogenesi operators now include STATUS metadata blocks
- Cross-references updated for improved navigation

### TheThird Operators
- STATUS blocks standardized to match Archive-wide patterns
- Enhanced documentation for knot operators

### Substrate Meta-Operators
- STATUS blocks added
- Operator of Recursion and Operator of Distinction documented

## Operator Classification

All operators now classified by:
1. **Class** — Prime, Secondary, Tertiary
2. **Harmonic Type** — Ascending, Descending, Cyclic
3. **Binding** — Phoenix, Hydrogenesi, The Third, Universal, Meta
4. **Lineage** — Parent operator reference

## Test Coverage

New test suites added:
- Meta-Operator Invariance: 5 scenarios
  - Identity preservation under scaling
  - Identity under composition
  - Identity collapse rejection
  - Recursion depth constraint scaling
  - Cross-pillar consistency

Existing test coverage maintained:
- Phoenix operators: 19 tests
- Hydrogenesi operators: 11 tests
- Total: 30 tests (all passing)

## Documentation Updates

All operator documentation now includes:
- STATUS metadata block
- Operator classification
- Harmonic type designation
- Lineage reference
- Cross-system integration notes

---

**Total New Operators:** 7 (6 standard + 1 meta-operator)  
**Total Operators in Archive:** ~35 across all families  
**Test Coverage:** 30+ tests  
**Documentation Status:** STANDARDIZED

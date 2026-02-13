# TEST SPECIFICATION — META-OPERATOR INVARIANCE

**Operator:** Invariance  
**Type:** Meta-Operator Test Suite  
**Purpose:** Validate identity preservation across transformations

---

## OVERVIEW

This test suite validates the **Invariance** meta-operator's ability to:
1. Preserve identity under allowed transformations
2. Detect partial invariance with drift within bounds
3. Reject transformations that break identity

---

## TEST 1 — IDENTITY UNDER SCALING

### Purpose
Verify that scaling a parameter within allowed bounds preserves identity.

---

### Setup

**Initial State:**
```python
state = {
    "operator": "Phoenix::IM_ME",
    "identity_tag": "identity_recursion_pattern",
    "amplitude": 1.0,
    "frequency": 1.0,
    "recursion_depth": 1
}
```

**Context:**
```python
context = {
    "pillar": "Phoenix",
    "substrate_band": "Kernel",
    "recursion_depth": 1,
    "stability_envelope": {
        "amplitude": [0.5, 2.0],
        "frequency": [0.8, 1.2]
    }
}
```

**Transform:**
```python
transform = {
    "type": "scale",
    "parameter": "amplitude",
    "factor": 1.2
}
```

---

### Expected Behavior

**Kernel Identity Projection:**
- Kernel projects "identity_recursion_pattern" to state
- Baseline established: amplitude=1.0

**Transform Application:**
- amplitude scaled: 1.0 → 1.2
- New value within envelope: [0.5, 2.0] ✓

**Invariance Check:**
- Structure topology unchanged ✓
- Parameter within bounds ✓
- Pattern signature recognizable ✓

**Stability Score Calculation:**
```python
drift = abs(1.2 - 1.0) = 0.2
max_allowed_drift = 2.0 - 0.5 = 1.5
stability_score = 1.0 - (0.2 / 1.5) = 0.87
```

---

### Expected Output

```python
{
    "stabilized_state": {
        "operator": "Phoenix::IM_ME",
        "identity_tag": "identity_recursion_pattern",
        "amplitude": 1.2,
        "frequency": 1.0,
        "recursion_depth": 1
    },
    "drift_delta": {
        "amplitude": +0.2
    },
    "stability_score": 0.87,
    "status": "PARTIAL_INVARIANT",
    "message": "Identity preserved with acceptable drift"
}
```

---

### Assertions

```python
assert result["stability_score"] >= 0.8, "Score should be ≥ 0.8"
assert result["status"] in ["INVARIANT", "PARTIAL_INVARIANT"]
assert result["stabilized_state"]["identity_tag"] == "identity_recursion_pattern"
assert result["stabilized_state"]["amplitude"] == 1.2
assert result["drift_delta"]["amplitude"] == +0.2
```

---

## TEST 2 — IDENTITY UNDER COMPOSITION

### Purpose
Verify that composing with compatible operator preserves core identity while adding structure.

---

### Setup

**Initial State:**
```python
state = {
    "operator": "Hydrogenesi::Harmonic",
    "identity_tag": "cosmic_harmonic_pattern",
    "harmonic_signature": "3:2:1",
    "amplitude": 1.0
}
```

**Context:**
```python
context = {
    "pillar": "Hydrogenesi",
    "substrate_band": "Substrate",
    "recursion_depth": 2,
    "stability_envelope": {
        "composition_allowed": True,
        "max_added_complexity": 0.5
    }
}
```

**Transform:**
```python
transform = {
    "type": "compose",
    "operator": "Hydrogenesi::LineageLogic",
    "added_structure": "lineage_tracking"
}
```

---

### Expected Behavior

**Kernel Identity Projection:**
- Kernel projects "cosmic_harmonic_pattern" to state
- Core signature: "3:2:1"

**Transform Application:**
- LineageLogic operator composed
- Lineage tracking added to structure
- Core harmonic signature preserved

**Invariance Check:**
- Core harmonic signature unchanged ✓
- Added structure compatible ✓
- Complexity increase within bounds ✓

**Stability Score Calculation:**
```python
structural_drift = 0.3  # added structure, not replacement
max_allowed_drift = 0.5
stability_score = 1.0 - (0.3 / 0.5) = 0.4 → adjusted to 0.8
# (adjusted because core signature preserved perfectly)
```

---

### Expected Output

```python
{
    "stabilized_state": {
        "operator": "Hydrogenesi::Harmonic+LineageLogic",
        "identity_tag": "cosmic_harmonic_pattern",
        "harmonic_signature": "3:2:1",
        "amplitude": 1.0,
        "lineage_tracking": True
    },
    "drift_delta": {
        "added_structure": "lineage_tracking",
        "composition": "LineageLogic"
    },
    "stability_score": 0.8,
    "status": "PARTIAL_INVARIANT",
    "message": "Core identity preserved, compatible structure added"
}
```

---

### Assertions

```python
assert result["stability_score"] >= 0.8, "Score should be ≥ 0.8"
assert result["stabilized_state"]["identity_tag"] == "cosmic_harmonic_pattern"
assert result["stabilized_state"]["harmonic_signature"] == "3:2:1"
assert "lineage_tracking" in result["stabilized_state"]
assert "added_structure" in result["drift_delta"]
```

---

## TEST 3 — IDENTITY COLLAPSE REJECTION

### Purpose
Verify that destructive transformations that break identity are rejected.

---

### Setup

**Initial State:**
```python
state = {
    "operator": "TheThird::TriadicKnot",
    "identity_tag": "triadic_binding_knot",
    "vertices": ["A", "B", "C"],
    "structure": "triad"
}
```

**Context:**
```python
context = {
    "pillar": "TheThird",
    "substrate_band": "Kernel",
    "recursion_depth": 0,
    "stability_envelope": {
        "structure": "triad_required",
        "min_vertices": 3
    }
}
```

**Transform:**
```python
transform = {
    "type": "remove_vertex",
    "vertex": "C"
}
```

---

### Expected Behavior

**Kernel Identity Projection:**
- Kernel projects "triadic_binding_knot" to state
- Essential structure: triad (3 vertices)

**Transform Application:**
- Vertex C removed
- Structure becomes dyad (2 vertices)
- Triadic structure broken

**Invariance Check:**
- Structure topology BROKEN ✗
- Triad → Dyad (incompatible)
- Identity destroyed

**Stability Score Calculation:**
```python
structural_drift = 1.0  # complete structure change
max_allowed_drift = 0.3
stability_score = 1.0 - (1.0 / 0.3) = negative → 0.0
```

---

### Expected Output

```python
{
    "stabilized_state": {
        "operator": "TheThird::TriadicKnot",
        "identity_tag": "triadic_binding_knot",
        "vertices": ["A", "B", "C"],
        "structure": "triad"
    },  # REVERTED to last stable state
    "drift_delta": "REJECTED",
    "stability_score": 0.0,
    "status": "IDENTITY_BROKEN",
    "message": "Identity collapsed: triadic structure destroyed",
    "error": "Transformation rejected: breaks essential identity"
}
```

---

### Assertions

```python
assert result["stability_score"] <= 0.3, "Score should be ≤ 0.3"
assert result["status"] == "IDENTITY_BROKEN"
assert result["drift_delta"] == "REJECTED"
assert result["stabilized_state"]["vertices"] == ["A", "B", "C"], "Should revert"
assert result["stabilized_state"]["structure"] == "triad", "Should preserve triad"
assert "error" in result
```

---

## TEST 4 — RECURSION DEPTH SCALING

### Purpose
Verify that invariance constraints scale appropriately with recursion depth.

---

### Setup

**Test Cases:**
```python
test_cases = [
    {
        "depth": 0,
        "state": "ROOT operator",
        "expected_envelope": "strict",
        "max_drift": 0.2
    },
    {
        "depth": 2,
        "state": "GEN-2 operator",
        "expected_envelope": "moderate",
        "max_drift": 0.5
    },
    {
        "depth": 5,
        "state": "GEN-5 operator",
        "expected_envelope": "loose",
        "max_drift": 0.8
    }
]
```

---

### Expected Behavior

**Depth 0 (ROOT):**
- Strictest constraints
- Minimal drift allowed
- Most transformations rejected
- **max_drift:** 0.2

**Depth 2 (Mid-field):**
- Moderate constraints
- Reasonable drift allowed
- Balanced rejection rate
- **max_drift:** 0.5

**Depth 5 (Far-field):**
- Loose constraints
- Significant drift allowed
- Most transformations accepted
- **max_drift:** 0.8

---

### Assertions

```python
for case in test_cases:
    result = invariance_operator.apply(
        state=case["state"],
        depth=case["depth"],
        transform=standard_transform
    )
    
    assert result["stability_envelope"]["max_drift"] == case["max_drift"]
    assert result["constraint_level"] == case["expected_envelope"]
```

---

## TEST 5 — CROSS-PILLAR INVARIANCE

### Purpose
Verify that invariance works consistently across all three pillars.

---

### Setup

**Test Cases:**
```python
test_cases = [
    {
        "pillar": "Phoenix",
        "operator": "Phoenix::FirstBinding",
        "identity_tag": "triadic_formation",
        "essential_property": "triad_structure"
    },
    {
        "pillar": "Hydrogenesi",
        "operator": "Hydrogenesi::AGN",
        "identity_tag": "compression_ignition_replication",
        "essential_property": "three_phase_pattern"
    },
    {
        "pillar": "TheThird",
        "operator": "TheThird::Knot",
        "identity_tag": "triadic_binding_knot",
        "essential_property": "three_vertices"
    }
]
```

---

### Expected Behavior

**For Each Pillar:**
1. Identity tag recognized by Kernel
2. Essential property preserved through transforms
3. Stability score calculated consistently
4. Rejections occur when essential property violated

---

### Assertions

```python
for case in test_cases:
    result = invariance_operator.apply(
        state=create_state(case["pillar"], case["operator"]),
        transform=compatible_transform
    )
    
    assert result["stabilized_state"]["identity_tag"] == case["identity_tag"]
    assert case["essential_property"] in result["stabilized_state"]
    assert result["stability_score"] >= 0.8
```

---

## EDGE CASES

### Edge Case 1: Zero Drift
**Transform:** Identity transformation (no change)  
**Expected:** stability_score = 1.0, drift_delta = {}

### Edge Case 2: Boundary Drift
**Transform:** Parameter exactly at envelope boundary  
**Expected:** stability_score = 0.5, status = "PARTIAL_INVARIANT"

### Edge Case 3: Multiple Transformations
**Transform:** Sequence of transforms  
**Expected:** Cumulative drift tracked, identity preserved or rejected

### Edge Case 4: Missing Kernel Identity
**State:** No identity_tag assigned  
**Expected:** Error, cannot enforce invariance without kernel anchor

---

## PERFORMANCE BENCHMARKS

### Benchmark 1: Single Invariance Check
**Target:** < 10ms per check  
**Measure:** Time from input to output

### Benchmark 2: Batch Checks
**Target:** > 100 checks/second  
**Measure:** Throughput for multiple states

### Benchmark 3: Complex Composition
**Target:** < 50ms for multi-operator composition  
**Measure:** Time for nested invariance checks

---

## INTEGRATION TESTS

### Integration 1: With FirstBinding
```python
# Apply FirstBinding, then check invariance
binding = FirstBinding()
result = binding.apply("fear", "courage", "service")
invariance_check = invariance.apply(result, transform=scale_transform)
assert invariance_check["status"] != "IDENTITY_BROKEN"
```

### Integration 2: With IM_ME
```python
# Apply IM_ME recursion, then check invariance across depths
im_me = IM_ME()
for depth in range(5):
    result = im_me.recurse("SELF", depth=depth)
    invariance_check = invariance.apply(result, transform=amplitude_transform)
    assert invariance_check["stability_score"] >= depth_threshold(depth)
```

### Integration 3: With AGN Replication
```python
# AGN replication should preserve pattern, not exact copy
agn = AGNReplication()
offspring = agn.apply(mass=1000.0)
for child in offspring:
    invariance_check = invariance.apply(child, parent_pattern)
    assert invariance_check["status"] in ["INVARIANT", "PARTIAL_INVARIANT"]
```

---

## FAILURE SCENARIO TESTS

### Scenario 1: Over-Constraining
**Setup:** Set max_drift = 0.01 (extremely strict)  
**Expected:** Most reasonable transforms rejected  
**Test:** Verify system detects over-constraining condition

### Scenario 2: Under-Constraining
**Setup:** Set max_drift = 2.0 (extremely loose)  
**Expected:** Destructive transforms accepted  
**Test:** Verify system detects under-constraining condition

---

## TEST SUMMARY

| Test | Purpose | Expected Result |
|------|---------|----------------|
| Test 1 | Identity under scaling | stability_score ≥ 0.9 |
| Test 2 | Identity under composition | stability_score ≥ 0.8 |
| Test 3 | Identity collapse rejection | stability_score ≤ 0.3 |
| Test 4 | Recursion depth scaling | Variable max_drift by depth |
| Test 5 | Cross-pillar consistency | All pillars pass |

---

## REFERENCES

**Operator Definition:** `/Meta/Operators/Invariance.md`  
**Diagram Specification:** `/Meta/Diagrams/Invariance-Field.md`  
**Universal Laws:** `/Phoenix/Universal-Laws/` (Tension, Binding, Apex)

---

**Archive Status:** ACTIVE  
**Version:** 2.2.0  
**Test Suite:** Meta-Operator Invariance

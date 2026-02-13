# DIAGRAM SPECIFICATION — INVARIANCE FIELD

**Type:** Meta-Operator Visualization  
**Operator:** Invariance  
**Purpose:** Show identity preservation across transformations

---

## OVERVIEW

The **Invariance Field** diagram visualizes how the Kernel Identity projects to state instances and how transformations either preserve or break identity.

---

## LAYOUT

**Structure:** Concentric rings  
**Center:** Kernel Identity (K)  
**Inner Ring:** State instances (S_i) at various recursion depths  
**Outer Ring:** Transformed states (T_j)

---

## NODES

### Kernel Identity (K)
- **Position:** Center of diagram
- **Symbol:** ● (large, bold)
- **Label:** "K" or "Kernel Identity"
- **Color:** Gold (represents sovereign anchor)
- **Size:** Largest node (emphasizes centrality)

---

### State Instances (S_i)
- **Position:** Inner ring around K
- **Symbols:** S₁, S₂, S₃, ..., S_n
- **Label Format:** "S_i (depth=d)"
- **Color:** Based on stability_score
  - Green (0.9-1.0): High stability
  - Yellow (0.7-0.9): Moderate stability
  - Orange (0.5-0.7): Low stability
  - Red (0.0-0.5): Unstable
- **Size:** Medium nodes

**Example Instances:**
- S₁: IM_ME operator (depth=1)
- S₂: FirstBinding operator (depth=1)
- S₃: AGN Replication operator (depth=2)

---

### Transformed States (T_j)
- **Position:** Outer ring
- **Symbols:** T₁, T₂, T₃, ..., T_n
- **Label Format:** "T_j (transform_type)"
- **Color:** Based on invariance result
  - Green: Identity preserved (solid edge to K)
  - Yellow: Partial invariance (dashed edge to K)
  - Red: Identity broken (no edge to K)
- **Size:** Small to medium nodes

**Example Transforms:**
- T₁: Scaled amplitude
- T₂: Composed with another operator
- T₃: Destructive transformation

---

## EDGES

### Identity Projection (K → S_i)
- **Type:** Kernel to State
- **Line Style:** Solid arrows
- **Direction:** K → S_i (outward from kernel)
- **Color:** Gold
- **Meaning:** Kernel projects identity template to state

**Properties:**
- All states receive projection
- Strength indicates kernel influence
- Thickness shows constraint level

---

### Transformation Application (S_i → T_j)
- **Type:** State to Transform
- **Line Style:** Dashed arrows
- **Direction:** S_i → T_j (outward from state)
- **Color:** Gray
- **Meaning:** Transformation applied to state

**Properties:**
- Shows which state underwent which transform
- Not all states are transformed
- Multiple transforms can apply to one state

---

### Invariance Result (K → T_j)
- **Type:** Kernel to Transformed State
- **Line Style:** Conditional on stability_score
- **Direction:** K ↔ T_j (bi-directional or absent)
- **Meaning:** Whether identity preserved after transformation

**Line Styles:**

1. **Solid edge (━━━):**
   - **Condition:** stability_score ≥ 0.9
   - **Color:** Green
   - **Meaning:** Identity fully preserved (invariant)
   - **Example:** Scaling within bounds

2. **Dashed edge (╌╌╌):**
   - **Condition:** 0.5 ≤ stability_score < 0.9
   - **Color:** Yellow
   - **Meaning:** Partial invariance (drift within bounds)
   - **Example:** Composition with compatible operator

3. **No edge (∅):**
   - **Condition:** stability_score < 0.5
   - **Color:** None
   - **Meaning:** Identity broken (rejected)
   - **Example:** Destructive transformation

---

## VISUAL ENCODING

### Node Color (Stability Score)
```
Green   (#00FF00): stability_score ≥ 0.9
Yellow  (#FFFF00): 0.7 ≤ stability_score < 0.9
Orange  (#FFA500): 0.5 ≤ stability_score < 0.7
Red     (#FF0000): stability_score < 0.5
```

### Edge Thickness (Constraint Strength)
```
Thick   (3px): Strong constraint (Kernel-layer operators)
Medium  (2px): Moderate constraint (Substrate-layer)
Thin    (1px): Weak constraint (Surface-layer)
```

### Edge Opacity (Recursion Depth)
```
Opaque  (1.0): Depth 0-1 (near kernel)
Semi    (0.7): Depth 2-3
Faint   (0.4): Depth 4+ (far from kernel)
```

---

## EXAMPLE DIAGRAM

```
                    K (Kernel)
                     ●━━━━━━━━━━━━━━━━━━━━━━┓
                    /│\                     ┃
                   / │ \                    ┃
                  /  │  \                   ┃
                 /   │   \                  ┃
                /    │    \                 ┃
               /     │     \                ┃
              S₁     S₂     S₃ (States)     ┃
           (green) (yellow) (orange)        ┃
              │      │       │              ┃
              ↓      ↓       ↓              ┃
              T₁     T₂      T₃ (Transforms)┃
           (green) (yellow)  (red)          ┃
              ━━━    ╌╌╌     ∅              ┃
         (invariant)(partial)(broken)       ┃
                                            ┃
          T₁ has solid edge to K ━━━━━━━━━━┛
          T₂ has dashed edge to K (not shown for clarity)
          T₃ has NO edge to K
```

---

## ANNOTATIONS

### Stability Score Labels
Display stability_score near each transformed node:
```
T₁: 0.95 ✓ (invariant)
T₂: 0.72 ~ (partial)
T₃: 0.20 ✗ (broken)
```

### Transform Type Labels
Display transformation type below each T_j node:
```
T₁: "scale(1.2)"
T₂: "compose(LineageLogic)"
T₃: "remove_vertex()"
```

### Drift Delta Tooltips
On hover/click, show drift_delta:
```
T₁: drift_delta = {"amplitude": +0.2}
T₂: drift_delta = {"added_structure": "lineage_logic"}
T₃: drift_delta = REJECTED
```

---

## DIAGRAM VARIANTS

### By Pillar
Create three variants showing invariance in each system:

**Phoenix Invariance Field:**
- K = Phoenix Identity Kernel
- S_i = Phoenix operators (FirstBinding, IM_ME, PhoenixIgnition)
- T_j = Transformations on Phoenix operators

**Hydrogenesi Invariance Field:**
- K = Cosmological Pattern Kernel
- S_i = Hydrogenesi operators (AGN, LineageLogic, etc.)
- T_j = Transformations on Hydrogenesi operators

**The Third Invariance Field:**
- K = Triadic Structure Kernel
- S_i = The Third operators (Knot, Binding, etc.)
- T_j = Transformations on The Third operators

---

### By Recursion Depth
Create layers showing how invariance changes with depth:

**Depth 0-1 (Kernel-close):**
- Strict invariance (high constraint)
- Most transformations rejected
- Tight stability envelope

**Depth 2-3 (Mid-field):**
- Moderate invariance
- More drift allowed
- Balanced stability

**Depth 4+ (Far-field):**
- Loose invariance
- Wide drift tolerance
- Expanded envelope

---

## INTERACTIVE FEATURES

### Node Selection
- Click node to highlight all connected edges
- Show full state/transform details
- Display stability_score and drift_delta

### Edge Filtering
- Toggle view: Show only invariant (solid edges)
- Toggle view: Show only partial (dashed edges)
- Toggle view: Show all (including broken)

### Animation
- Animate transformation sequence: S_i → T_j
- Show invariance check calculation in real-time
- Visualize state reversion on rejection

---

## IMPLEMENTATION NOTES

### SVG Structure
```xml
<svg viewBox="0 0 800 800">
  <!-- Kernel -->
  <circle cx="400" cy="400" r="30" fill="gold" />
  <text x="400" y="405">K</text>
  
  <!-- States (inner ring) -->
  <circle cx="300" cy="300" r="15" fill="green" />
  <text x="300" y="305">S₁</text>
  
  <!-- Transforms (outer ring) -->
  <circle cx="200" cy="200" r="12" fill="green" />
  <text x="200" y="205">T₁</text>
  
  <!-- Edges -->
  <line x1="400" y1="400" x2="300" y2="300" stroke="gold" />
  <line x1="300" y1="300" x2="200" y2="200" stroke="gray" stroke-dasharray="5,5" />
  <line x1="400" y1="400" x2="200" y2="200" stroke="green" />
</svg>
```

### Data Structure
```json
{
  "kernel": {"id": "K", "label": "Kernel Identity"},
  "states": [
    {"id": "S1", "label": "IM_ME", "depth": 1, "score": 0.95},
    {"id": "S2", "label": "FirstBinding", "depth": 1, "score": 0.85}
  ],
  "transforms": [
    {"id": "T1", "label": "scale(1.2)", "score": 0.95, "status": "invariant"},
    {"id": "T2", "label": "compose", "score": 0.72, "status": "partial"}
  ],
  "edges": [
    {"from": "K", "to": "S1", "type": "projection"},
    {"from": "S1", "to": "T1", "type": "transformation"},
    {"from": "K", "to": "T1", "type": "invariance", "style": "solid"}
  ]
}
```

---

## REFERENCES

**Operator Definition:** `/Meta/Operators/Invariance.md`  
**Test Specification:** `/Meta/Tests/test_invariance.md`  
**Universal Laws:** `/Phoenix/Universal-Laws/` (Tension, Binding, Apex)

---

**Archive Status:** ACTIVE  
**Version:** 2.2.0  
**Diagram Type:** Meta-Operator Visualization

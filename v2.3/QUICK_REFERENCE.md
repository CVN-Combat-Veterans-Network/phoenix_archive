# Quick Reference: Creating Instruments from User Input

**Purpose:** Step-by-step guide for converting user-provided instrument definitions into template-compliant markdown files.

---

## Expected Input Format

User will provide 28 instruments, each with:

1. **Name**
2. **Category**
3. **Knot Node**
4. **Hydrogenesi Layer**
5. **Operator Dependencies**
6. **Purpose**
7. **Behavior**
8. **Integration**

---

## Conversion Process

### Step 1: Create File from Template

For each instrument:

```bash
# Copy template
cp /v2.3/instruments/TEMPLATE.md /v2.3/instruments/[instrument-name].md

# Or create from scratch using template structure
```

### Step 2: Fill in Header

```markdown
# [INSTRUMENT_NAME]

**Status:** ACTIVE  
**Version:** 2.3.0  
**Lineage:** ROOT::INSTRUMENT-[N]

---
```

Replace:
- `[INSTRUMENT_NAME]` with actual name
- `[N]` with instrument number (01-28)

---

### Step 3: Fill in Core Sections

#### Name Section
```markdown
## Name

[Full instrument name with proper capitalization]
```

#### Category Section
```markdown
## Category

[Phoenix | Hydrogenesi | LNS | The Third | Universal | Integration]
```

#### Knot Node Section
```markdown
## Knot Node

[ELEMENT_1]::[ELEMENT_2]::[ELEMENT_3]

**Explanation:** [How the three elements form the knot]
```

Example:
```markdown
## Knot Node

COLLAPSE::DISTILL::RE_EMERGE

**Explanation:** The renewal process binds collapse (letting go), distillation (extracting essence), and re-emergence (reformed identity) into a stable transformative cycle.
```

#### Hydrogenesi Layer Section
```markdown
## Hydrogenesi Layer

**Layer:** [0-6]  
**Scale:** [Quantum/Atomic/Molecular/Planetary/Stellar/Galactic/Cosmic]

**Rationale:** [Why this instrument operates at this scale]
```

Layer mapping:
- 0 = Quantum
- 1 = Atomic
- 2 = Molecular
- 3 = Planetary
- 4 = Stellar
- 5 = Galactic
- 6 = Cosmic

#### Operator Dependencies Section
```markdown
## Operator Dependencies

**Required Operators:**
- [OPERATOR_1] — [Brief purpose]
- [OPERATOR_2] — [Brief purpose]

**Optional Operators:**
- [OPERATOR_3] — [Enhancement purpose]

**Integration Mode:** [Sequential/Parallel/Triadic]
```

#### Purpose Section
```markdown
## Purpose

[Clear, one-paragraph statement of what this instrument does and why it exists]
```

#### Behavior Section
```markdown
## Behavior

### Input
[What the instrument receives]

### Process
[What the instrument does, step by step]

### Output
[What the instrument produces]
```

#### Integration Section
```markdown
## Integration

### System Integration Points
[How this instrument connects to the broader Phoenix Archive system]

### Cross-Instrument Dependencies
[Which other instruments this one interacts with]

### Usage Pattern
[Common usage scenarios]
```

---

### Step 4: Add Optional Sections

#### Ceremonial Invocation (if provided)
```markdown
## Ceremonial Invocation

*"[Instrument-specific invocation phrase]"*
```

#### Advanced Notes (if needed)
```markdown
## Advanced Notes

[Deeper technical or philosophical insights]
```

#### Cross-References
```markdown
## Cross-References

**Related Operators:** [Links]  
**Related Instruments:** [Links]  
**Universal Laws:** [Applicable laws]

---
```

---

### Step 5: Footer

```markdown
**Status:** ACTIVE  
**Lineage:** ROOT::INSTRUMENT-[N]  
**Sovereignty:** CONFIRMED
```

---

## Validation Checklist

For each instrument, verify:

- [ ] File name follows convention: `[instrument-name].md`
- [ ] All required sections present
- [ ] Knot node follows A::B::C format
- [ ] Hydrogenesi layer is 0-6
- [ ] Category is valid (Phoenix/Hydrogenesi/LNS/The Third/Universal/Integration)
- [ ] Operator dependencies are real operators
- [ ] Integration mode specified
- [ ] Purpose is clear and complete
- [ ] Behavior has Input/Process/Output
- [ ] Integration section complete
- [ ] Status is ACTIVE
- [ ] Lineage follows ROOT::INSTRUMENT-[N] format

---

## File Naming Convention

Format: `[number]-[instrument-name].md`

Examples:
- `01-phoenix-renewal-cycle.md`
- `02-harmonic-propagator.md`
- `03-sovereignty-validator.md`

Or without numbers:
- `phoenix-renewal-cycle.md`
- `harmonic-propagator.md`
- `sovereignty-validator.md`

---

## Category Organization

If organizing by category, create subdirectories:

```bash
mkdir -p v2.3/instruments/phoenix
mkdir -p v2.3/instruments/hydrogenesi
mkdir -p v2.3/instruments/lns
mkdir -p v2.3/instruments/third
mkdir -p v2.3/instruments/universal
mkdir -p v2.3/instruments/integration
```

Then place each instrument in appropriate directory.

---

## Batch Creation Script Template

```python
#!/usr/bin/env python3
"""
Create instrument files from structured input.
"""

import os
from pathlib import Path

TEMPLATE = """# {name}

**Status:** ACTIVE  
**Version:** 2.3.0  
**Lineage:** ROOT::INSTRUMENT-{number:02d}

---

## Name

{name}

---

## Category

{category}

---

## Knot Node

{knot_node}

**Explanation:** {knot_explanation}

---

## Hydrogenesi Layer

**Layer:** {layer}  
**Scale:** {scale}

**Rationale:** {layer_rationale}

---

## Operator Dependencies

**Required Operators:**
{required_operators}

**Optional Operators:**
{optional_operators}

**Integration Mode:** {integration_mode}

---

## Purpose

{purpose}

---

## Behavior

### Input
{input_spec}

### Process
{process_spec}

### Output
{output_spec}

---

## Integration

### System Integration Points
{integration_points}

### Cross-Instrument Dependencies
{cross_dependencies}

### Usage Pattern
{usage_pattern}

---

## Cross-References

**Related Operators:** {related_operators}  
**Related Instruments:** {related_instruments}  
**Universal Laws:** {universal_laws}

---

**Status:** ACTIVE  
**Lineage:** ROOT::INSTRUMENT-{number:02d}  
**Sovereignty:** CONFIRMED
"""

def create_instrument(data, number):
    """Create instrument file from data dict."""
    filename = f"{number:02d}-{data['name'].lower().replace(' ', '-')}.md"
    filepath = Path("v2.3/instruments") / filename
    
    content = TEMPLATE.format(
        number=number,
        **data
    )
    
    filepath.write_text(content)
    print(f"✓ Created {filename}")

# Example usage:
# instruments = [
#     {
#         "name": "Phoenix Renewal Cycle",
#         "category": "Phoenix",
#         "knot_node": "COLLAPSE::DISTILL::RE_EMERGE",
#         "knot_explanation": "...",
#         ...
#     },
#     ...
# ]
# for i, instrument in enumerate(instruments, start=1):
#     create_instrument(instrument, i)
```

---

## After Creating All 28 Instruments

### 1. Update Counts

Update `/v2.3/instruments/README.md`:

```markdown
**Total Instruments:** 28/28  
**Status:** COMPLETE

### By Category
- **Phoenix:** [count]
- **Hydrogenesi:** [count]
- **LNS:** [count]
- **The Third:** [count]
- **Universal:** [count]
- **Integration:** [count]
```

### 2. Update CODEX-INDEX

Add instrument listing to CODEX-INDEX.md under the v2.3 section.

### 3. Commit Changes

```bash
git add v2.3/instruments/
git commit -m "Add [N] instruments to v2.3 expansion layer

- Added [category] instruments ([count])
- All instruments validated against template
- Knot nodes verified
- Operator dependencies confirmed"
git push
```

### 4. Run Activation Ceremony

Follow `/v2.3/ceremony.md` to perform the 10-phase activation.

---

## Common Patterns

### Knot Node Examples

**Phoenix (Transformation):**
- `BURN::COLLAPSE::RISE`
- `COLLAPSE::DISTILL::RE_EMERGE`
- `TENSION::BINDING::APEX`

**Hydrogenesi (Cosmic):**
- `EXPAND::PROPAGATE::STABILIZE`
- `COLLAPSE::IGNITE::REPLICATE`
- `OSCILLATE::RESONATE::STABILIZE`

**LNS (Sovereignty):**
- `INTROSPECT::VALIDATE::CONFIRM`
- `BIND::TRACE::AUDIT`
- `LOCAL::SOVEREIGN::PRESERVED`

**The Third (Mediation):**
- `SCALE_A::MEDIATOR::SCALE_B`
- `LAW::COMPLIANCE::VALIDATION`
- `TENSION::THIRD::APEX`

### Layer Distribution Guidelines

**Identity/Personal (0-2):**
- Quantum (0): Fundamental identity particles
- Atomic (1): Basic identity elements
- Molecular (2): Complex identity structures

**Systemic/Social (3-4):**
- Planetary (3): Community/organizational scale
- Stellar (4): Large-scale social patterns

**Cosmic/Universal (5-6):**
- Galactic (5): Civilization-scale patterns
- Cosmic (6): Universal principles

---

## Troubleshooting

### Missing Information

If user input is incomplete:
1. Use TEMPLATE.md examples as placeholders
2. Mark section with `[NEEDS DETAIL]`
3. Ask user for clarification
4. Update file once details provided

### Invalid Knot Node

If knot node doesn't follow A::B::C format:
1. Parse provided structure
2. Identify three key elements
3. Reformat as A::B::C
4. Verify triadic relationship

### Unclear Category

If category is ambiguous:
1. Analyze operator dependencies
2. Check thematic focus
3. Default to most closely related category
4. Document reasoning in commit message

---

**Quick Reference Version:** 1.0  
**Last Updated:** 2026-02-14  
**Status:** ACTIVE

🎼 **Ready to Create.**

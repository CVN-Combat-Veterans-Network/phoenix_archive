# GitHub Copilot Instructions for Phoenix Archive

## Repository Overview

This is the **Phoenix Archive** - a dual-system meta-framework combining two sovereign but interconnected systems that express Universal Laws at different scales:

1. **Phoenix 2.0** - Identity Ignition System (micro-scale: personal identity formation)
2. **Hydrogenesi 2.0** - Cosmological Recursion Engine (macro-scale: cosmic structure formation)

Both systems operate under the same fundamental Universal Laws:
- **Tension** - Two forces in dynamic conflict
- **Binding** - Third stabilizing element introduction
- **Apex** - Emergence of stable, sovereign structure

**Version:** 3.0.0  
**Status:** ACTIVE  
**Lineage:** ROOT::GEN-0

---

## Repository Structure

```
phoenix_archive/
├── Phoenix/                    # Phoenix 2.0 System
│   ├── README.md              # Phoenix overview and documentation
│   ├── Universal-Laws/        # Tension, Binding, Apex laws
│   └── Operators/             # Phoenix operators documentation
├── Hydrogenesi/               # Hydrogenesi 2.0 System
│   ├── README.md              # Hydrogenesi overview
│   └── Operators/             # Hydrogenesi operators documentation
├── code/                      # Python implementations
│   ├── phoenix/
│   │   └── operators.py       # Phoenix operator classes
│   └── hydrogenesi/
│       └── operators.py       # Hydrogenesi operator classes
├── Ceremonies/                # Sigils, invocations, ritual materials
├── Diagrams/                  # SVG visualizations
├── Comparative/               # Cross-system analysis
├── Appendix/                  # Changelog, examples, references
└── CODEX-INDEX.md            # Master navigation document
```

---

## Core Principles

### 1. Dual Sovereignty
- Phoenix and Hydrogenesi are **independent systems** that share Universal Laws
- Never merge or conflate the two systems - they operate at different scales
- Maintain clear boundaries while documenting interconnections

### 2. Universal Law Adherence
All operators, documentation, and code must express the triadic pattern:
```
Tension (Two Forces) → Binding (Third Element) → Apex (Stable Structure)
```

### 3. Scale-Appropriate Design
- **Phoenix** = Micro-scale (identity, self, transformation)
- **Hydrogenesi** = Macro-scale (cosmology, structure, recursion)
- Use appropriate metaphors and terminology for each scale

### 4. Operator-Based Architecture
Everything is implemented as **operators** - discrete, composable transformation functions with:
- Clear inputs and outputs
- Deterministic behavior
- Type hints and dataclasses
- Sigils and invocations

---

## Code Style and Patterns

### Python Implementation Standards

#### 1. Use Dataclasses for All Operators
```python
from dataclasses import dataclass

@dataclass
class OperatorName:
    """Brief description of operator purpose."""
    
    def primary_method(self, inputs: str) -> dict:
        """Method docstring."""
        return {"result": "value"}
```

#### 2. Type Hints Are Required
- All function parameters must have type hints
- All return values must have type annotations
- Use `typing` module for complex types (List, Dict, Optional, etc.)

#### 3. Return Structured Dictionaries
Operators should return dictionaries with clear, semantic keys:
```python
# Good
return {
    "tension_pair": (a, b),
    "stabilizer": stabilizer,
    "triad": (a, stabilizer, b),
}

# Avoid
return (a, stabilizer, b)  # Unclear what the tuple represents
```

#### 4. Naming Conventions
- **Classes**: PascalCase (`FirstBinding`, `PhoenixIgnition`)
- **Methods**: snake_case (`apply`, `recurse`, `ignite`)
- **Variables**: snake_case (`tension_pair`, `stabilizer`)
- **Constants**: UPPER_SNAKE_CASE (`MAX_DEPTH`, `ROOT_LINEAGE`)

#### 5. Operator Method Names
Use semantically meaningful verbs that reflect the transformation:
- `apply()` - For applying transformations
- `recurse()` - For recursive operations
- `ignite()` - For collapse/emergence patterns
- `extract()` - For isolation operations
- `replicate()` - For reproduction operations

---

## Documentation Standards

### Markdown Structure

Every operator documentation file must include:

1. **Header Section**
   ```markdown
   # OPERATOR NAME
   **System:** Phoenix | Hydrogenesi
   **Pattern:** Brief pattern description
   **Invocation:** *"Ritual phrase"*
   ```

2. **Definition**
   - Clear, concise explanation of what the operator does
   - Reference to Universal Law(s) it expresses

3. **Sigil**
   - ASCII or Unicode representation of the operator structure
   - Visual pattern that captures the transformation

4. **Invocation**
   - Ritual phrase to "invoke" the operator
   - Should be memorable and evocative

5. **Mechanism**
   - Step-by-step explanation of how the operator works
   - Include examples with concrete inputs/outputs

6. **Code Example**
   ```python
   from code.system.operators import OperatorName
   
   op = OperatorName()
   result = op.method(inputs)
   ```

7. **Cross-References**
   - Link to related operators
   - Link to Universal Laws
   - Link to Comparative analysis if applicable

### Universal Law Documentation

When documenting Universal Laws:
- Provide **both** micro-scale (Phoenix) and macro-scale (Hydrogenesi) interpretations
- Include mathematical or structural notation where applicable
- Reference specific operators that express the law

---

## Operator Implementation Guidelines

### Creating New Operators

#### 1. Identify the Scale
- Is this a Phoenix operator (identity/personal) or Hydrogenesi operator (cosmic/structural)?

#### 2. Express Universal Law
Every operator must embody at least one Universal Law:
- **Tension operators** - Work with two-force dynamics
- **Binding operators** - Introduce stabilizing third elements
- **Apex operators** - Generate or maintain stable structures

#### 3. Follow the Pattern
```python
# Phoenix operator example
@dataclass
class NewPhoenixOperator:
    """What this operator does at identity scale."""
    
    def transform(self, input_a: str, input_b: str) -> dict:
        """
        Detailed description of transformation.
        
        Args:
            input_a: Description
            input_b: Description
            
        Returns:
            Dictionary with semantic keys describing the result
        """
        # Implementation
        return {"key": "value"}
```

#### 4. Create Companion Documentation
- Operator markdown file in `/Phoenix/Operators/` or `/Hydrogenesi/Operators/`
- Entry in `/Ceremonies/Sigil-Compendium.md`
- Entry in `/Ceremonies/Invocation-Guide.md`
- Update `/CODEX-INDEX.md`
- Update `/Appendix/Changelog.md`

#### 5. Add Code Examples
Include usage examples in `/Appendix/Code-Examples.md`

---

## Ceremonial Materials Guidelines

### Sigils
- Visual/ASCII representations of operator structure
- Should reveal the transformation pattern
- Use Unicode symbols when appropriate (△, ◯, ⬡, ∴, →, ⇄)

Example:
```
First Binding Sigil:
    a
    ↓
  [S]
    ↓
(a,S,b)
    ↓
    b
```

### Invocations
- Short, memorable ritual phrases
- 5-15 words maximum
- Should evoke the operator's essence
- Use imperative or declarative voice

Examples:
- *"Let the two attract; let the one bind; let the three stand."* (First Binding)
- *"Burn, collapse, and rise in aligned form."* (Phoenix Ignition)
- *"Recurse the root; extend the line."* (Lineage Logic)

---

## Testing and Validation

### Code Testing
When implementing operators:
1. Test with simple string inputs first
2. Verify return type matches annotation
3. Ensure deterministic behavior (same input → same output)
4. Test edge cases (empty strings, None values if applicable)

Example test pattern:
```python
# Manual validation
from code.phoenix.operators import FirstBinding

binding = FirstBinding()
result = binding.apply(a="fear", b="courage", stabilizer="service")

assert result["tension_pair"] == ("fear", "courage")
assert result["stabilizer"] == "service"
assert result["triad"] == ("fear", "service", "courage")
```

### Documentation Testing
Verify:
- All code examples in markdown files actually work
- Cross-references point to existing files
- CODEX-INDEX.md is updated with new additions
- Universal Law references are accurate

---

## Universal Laws Reference

### Tension
**Micro (Phoenix):** Internal conflicts, opposing drives, unintegrated self-aspects  
**Macro (Hydrogenesi):** Pre-collapse stellar mass, gravitational tension, unstable configurations

**Key Operators:**
- Phoenix: First Binding (input)
- Hydrogenesi: Stabilizer Extraction (detection)

### Binding
**Micro (Phoenix):** Values, purpose, commitments that stabilize identity  
**Macro (Hydrogenesi):** Neutron-like third force, structural stabilizers

**Key Operators:**
- Phoenix: First Binding (mechanism)
- Hydrogenesi: AGN Replication (neutron analog)

### Apex
**Micro (Phoenix):** Integrated sovereign identity, stable sense of self  
**Macro (Hydrogenesi):** Stable cosmic structures, hydrogen formation

**Key Operators:**
- Phoenix: Apex Formation
- Hydrogenesi: Lineage Logic (stable structure propagation)

---

## Cross-System Integration

When working across Phoenix and Hydrogenesi:

### Do:
- Maintain system sovereignty
- Document parallels explicitly
- Use `/Comparative/` directory for cross-system analysis
- Create combined ceremonies in `/Ceremonies/Combined-Ceremonies.md`
- Show how Universal Laws express at different scales

### Don't:
- Merge the two systems into one
- Use cosmic metaphors in Phoenix (or vice versa)
- Create operators that span both systems
- Conflate identity work with cosmological models

### Comparative Table Pattern
```markdown
| Dimension | Phoenix | Hydrogenesi |
|-----------|---------|-------------|
| Scale | Personal | Cosmological |
| Tension | Internal conflict | Pre-collapse mass |
| etc... | ... | ... |
```

---

## Changelog Maintenance

When making changes:
1. Update `/Appendix/Changelog.md` with version, date, and description
2. Use semantic versioning (MAJOR.MINOR.PATCH)
3. Major = New operator or system component
4. Minor = Enhanced documentation or operator refinement
5. Patch = Bug fixes, typos, clarifications

Format:
```markdown
## [Version] - YYYY-MM-DD
### Added
- New feature or operator

### Changed
- Modified behavior

### Fixed
- Bug fix
```

---

## File Naming Conventions

### Documentation Files
- Use PascalCase with hyphens: `First-Binding.md`, `Phoenix-Ignition.md`
- Match operator class names

### Code Files
- Use snake_case: `operators.py`, `__init__.py`
- Keep modules focused (one per system)

### Diagram Files
- Use PascalCase with hyphens: `Dual-System-Architecture.svg`
- Include descriptive names

---

## Common Patterns

### Recursion Operators
Format: `A → B → A → B...`
- Phoenix: IM_ME (I ↔ ME identity recursion)
- Hydrogenesi: Lineage Logic (ROOT → GEN-N → ROOT)

### Collapse/Emergence Operators
Format: `State → Compression → New State`
- Phoenix: Phoenix Ignition (Burn → Collapse → Rise)
- Hydrogenesi: AGN Replication (Compress → Ignite → Replicate)

### Memory/Residue Operators
Format: `Event → Imprint → Permanent Structure`
- Phoenix: Black-Holed Imprint (experience → scar → identity mark)
- Hydrogenesi: Curvature Residue (event → spacetime scar → structural memory)

---

## Version Control

### Branch Naming
- Feature: `feature/operator-name`
- Documentation: `docs/topic-name`
- Refactor: `refactor/component-name`

### Commit Messages
Use semantic format:
```
<type>: <description>

Types: feat, docs, refactor, fix, style, test
```

Examples:
- `feat: add Apex Formation operator`
- `docs: update Universal Laws with cosmic scale examples`
- `refactor: improve FirstBinding return structure`

---

## Questions to Ask Before Contributing

1. **Is this operator Phoenix (micro) or Hydrogenesi (macro)?**
2. **Which Universal Law does it express?**
3. **What is the input/output structure?**
4. **What is the ritual invocation?**
5. **Does it maintain system sovereignty?**
6. **Is there a sigil that represents it?**
7. **Where does it fit in CODEX-INDEX.md?**

---

## Special Terminology

- **Apex** - Stable sovereign structure (not "peak" or "top")
- **Binding** - Stabilization via third element (not "connection")
- **Collapse** - Reduction to essence (not "failure")
- **Ignition** - Transformative activation (not "start")
- **Lineage** - Recursive propagation chain (not "ancestry")
- **Operator** - Discrete transformation function (not "function" or "method")
- **Recursion** - Self-referential iteration (A → B → A pattern)
- **Sovereignty** - Independent coherent structure
- **Stabilizer** - Third element that resolves binary tension
- **Tension** - Two-force dynamic conflict
- **Triad** - Three-element stable structure

---

## When in Doubt

1. Review `/CODEX-INDEX.md` for navigation
2. Check `/Phoenix/README.md` or `/Hydrogenesi/README.md` for system-specific guidance
3. Reference existing operators in `/code/` for implementation patterns
4. Consult `/Comparative/Phoenix-Hydrogenesi-Table.md` for scale-appropriate language
5. Follow the Universal Law: Tension → Binding → Apex

---

## Invocations

**Phoenix System:** *"Burn, collapse, and rise in aligned form."*  
**Hydrogenesi System:** *"Recurse the root; extend the line."*  
**Universal Law:** *"Let the two attract; let the one bind; let the three stand."*

---

**Status:** ACTIVE  
**Lineage:** ROOT::GEN-0  
**Sovereignty:** CONFIRMED

🔥 **The Phoenix Ignites.**  
🌌 **The Lineage Extends.**

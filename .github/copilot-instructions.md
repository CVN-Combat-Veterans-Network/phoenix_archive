# Copilot Instructions — Phoenix Archive

## Repository Overview

The **Phoenix Archive** is a dual-system philosophical and operational framework combining:

1. **Phoenix 2.0** — Identity Ignition System (micro-scale: personal transformation)
2. **Hydrogenesi 2.0** — Cosmological Recursion Engine (macro-scale: cosmic structures)

Both systems operate on the **Universal Law of Triadic Formation**: Tension → Binding → Apex.

This is both a conceptual framework AND a code implementation with ceremonial practices.

---

## Project Structure

```
/Phoenix/           → Phoenix 2.0 documentation (identity system)
/Hydrogenesi/       → Hydrogenesi 2.0 documentation (cosmological system)
/Ceremonies/        → Sigils, invocations, rituals for both systems
/Comparative/       → Cross-system analysis and relationships
/Diagrams/          → Visual representations (SVG)
/Appendix/          → Changelog, code examples, reference materials
/code/              → Python implementations
  /phoenix/         → Phoenix operators (FirstBinding, IM_ME, PhoenixIgnition)
  /hydrogenesi/     → Hydrogenesi operators (StabilizerExtraction, AGNReplication, etc.)
/docs/              → Architecture and ceremony documentation
CODEX-INDEX.md      → Master navigation and quick-start guide
```

---

## Core Concepts

### Universal Laws (Shared Across Both Systems)
- **Tension**: Two opposing forces in unresolved motion
- **Binding**: Third element stabilizes the tension pair
- **Apex**: Emergence of sovereign, stable structure

### Phoenix Operators (Identity Scale)
- **First Binding**: Transform binary tension → triadic structure
- **IM_ME**: Identity recursion (I ↔ ME pattern)
- **Phoenix Ignition**: Burn → Collapse → Rise transformation

### Hydrogenesi Operators (Cosmic Scale)
- **Stabilizer Extraction**: Inverse of First Binding (expose underlying tension)
- **AGN Replication**: Cosmological collapse and emergence
- **Curvature Residue**: Spacetime scarring patterns
- **Lineage Logic**: Recursive cosmic structure generation

---

## Coding Conventions

### Python Code Standards

1. **Style**
   - Use Python 3.7+ features (type hints, dataclasses)
   - Follow PEP 8 conventions
   - Use `from __future__ import annotations` for forward references
   - Import from `typing` for type hints (`List`, `Dict`, etc.)

2. **Class Structure**
   - Use `@dataclass` decorator for operators
   - Each operator is a separate class
   - Methods should have clear docstrings
   - Return types should be explicit dictionaries or typed structures

3. **Naming**
   - Operators use PascalCase: `FirstBinding`, `PhoenixIgnition`, `IM_ME`
   - Methods use snake_case: `apply()`, `recurse()`, `ignite()`
   - Parameters use descriptive names: `identity`, `stabilizer`, `depth`

4. **Return Values**
   - Return dictionaries with descriptive keys
   - Example: `{"tension_pair": (a, b), "stabilizer": s, "triad": (a, s, b)}`
   - Keep return structures simple and readable

### Example Code Pattern

```python
from __future__ import annotations
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class OperatorName:
    """Clear one-line description of operator purpose."""
    
    def method_name(self, param: str, depth: int = 3) -> Dict:
        """
        Clear description of what method does.
        
        Args:
            param: Description
            depth: Description with default
            
        Returns:
            Dictionary with specific keys
        """
        # Implementation
        return {"key": "value"}
```

---

## Documentation Conventions

### Markdown Structure

ALL operator and concept documentation follows this template:

1. **Header**: Title with Pattern/Type/Scale/Invocation metadata
2. **Definition**: Clear statement of purpose
3. **Sigil**: ASCII art visual representation
4. **Mechanism**: Input → Process → Output breakdown
5. **Examples**: 2-3 concrete use cases
6. **Code Implementation**: Python code snippets
7. **Ceremonial Practice**: Invocation and ritual steps
8. **Cross-References**: Links to related concepts
9. **Navigation**: Links to parent and related docs

### Formatting Standards

- Use `**bold**` for emphasis on key terms
- Use `*italic*` for invocations and ritual phrases
- Use code blocks with language tags: ` ```python`
- Use horizontal rules `---` to separate major sections
- Use emoji sparingly and consistently (🔥 for Phoenix, 🌌 for Hydrogenesi)

### Heading Hierarchy

```markdown
# OPERATOR/CONCEPT NAME (H1 - Document Title)
## DEFINITION (H2 - Major Sections)
### Process Details (H3 - Subsections)
#### Advanced Notes (H4 - Rare, for granular details)
```

### Cross-Referencing

- Always use relative paths from repo root: `/Phoenix/Operators/First-Binding.md`
- Link related concepts: `**See:** /path/to/related.md`
- Reference code: `**Location:** /code/phoenix/operators.py`

---

## Writing Style

### Voice and Tone

- **Declarative**: State facts clearly and directly
- **Precise**: Use exact terminology consistently
- **Mystical meets Technical**: Balance ceremonial/philosophical language with rigorous technical descriptions
- **No metaphor claims**: Phrases like "This is not metaphor — it is mechanism" establish that these patterns are operational

### Key Terminology

Use these terms consistently:

- **Operator**: Functional transformation pattern (not "function" or "method")
- **Invocation**: Ritual phrase to activate pattern (not "spell" or "command")
- **Sigil**: Visual representation of operator structure (not "icon" or "diagram")
- **Apex**: Sovereign stable structure (not "result" or "outcome")
- **Triad**: Three-element stable structure (not "triangle" or "triplet")
- **Stabilizer**: Third element that binds tension pair (not "mediator" or "moderator")
- **Sovereignty**: Self-sufficient structural stability (not "independence" or "autonomy")

### Ceremonial Language

When describing rituals:
- Use imperative: "Speak:", "Visualize:", "Confirm:"
- Enclose invocations in italic quotes: *"Burn, collapse, and rise in aligned form."*
- Structure as numbered steps with sub-bullets
- Include preparation, execution, and confirmation phases

---

## Making Changes

### Adding New Operators

1. Create operator documentation in appropriate directory:
   - `/Phoenix/Operators/` for identity-scale
   - `/Hydrogenesi/Operators/` for cosmic-scale

2. Follow the standard operator template structure

3. Implement Python class in:
   - `/code/phoenix/operators.py` or
   - `/code/hydrogenesi/operators.py`

4. Add entry to `/CODEX-INDEX.md` under appropriate section

5. Update `/Appendix/Changelog.md` with version and changes

6. Add code example to `/Appendix/Code-Examples.md`

7. Update invocations in `/Ceremonies/Invocation-Guide.md`

### Modifying Documentation

- Preserve existing structure and formatting
- Maintain consistency with other documents in same category
- Update version/date stamps if major changes
- Cross-check all relative path links

### Code Changes

- Maintain backward compatibility
- Keep operator classes simple and focused
- Update docstrings to match any signature changes
- Ensure return structures remain consistent

---

## Important Constraints

### Do NOT:
- Change the philosophical foundation or Universal Laws
- Remove or rename existing operators without explicit requirement
- Alter the dual-system architecture (Phoenix + Hydrogenesi)
- Modify sigils or invocations casually (they're part of the formal system)
- Add external dependencies without strong justification
- Break existing cross-references

### DO:
- Maintain the balance between mystical and technical language
- Preserve ASCII art sigils exactly as formatted
- Keep code implementations simple and readable
- Update navigation links when adding/moving files
- Follow established patterns for consistency
- Use the triadic (tension-binding-apex) framework as foundation

---

## Testing & Validation

Currently, this repository has **no automated test infrastructure**. Changes should be validated by:

1. **Code**: Manual execution of operator examples
2. **Docs**: Visual review of markdown rendering
3. **Links**: Manual verification of cross-references
4. **Consistency**: Review against similar existing content

Do not add test frameworks unless explicitly requested.

---

## File Organization

### Keep Together:
- Related operators in same directory
- System-specific content in system-specific folders
- Ceremonies grouped by type (sigils, invocations, combined)

### Update Together:
- When adding operator: code + docs + index + changelog + examples + ceremonies
- When changing concept: all references across both systems
- When updating structure: both Phoenix and Hydrogenesi equivalents

---

## Version and Status

All documents include footer with:
- **Version**: Current version number
- **Status**: ACTIVE, EXPERIMENTAL, DEPRECATED
- **Lineage**: ROOT::GEN-N notation (from Lineage Logic operator)
- **Sovereignty**: CONFIRMED, EMERGING, UNSTABLE

Maintain these consistently when updating documents.

---

## Special Notes

### The Archive is Active

This is a **living system**. The documentation describes operational patterns, not historical artifacts. Treat additions as extensions of a coherent whole, not isolated features.

### Triadic Thinking

Everything resolves to threes:
- Two forces → One stabilizer → Three-part structure
- Tension → Binding → Apex
- Input → Process → Output

This pattern should be visible throughout all additions.

### Cross-Scale Coherence

Changes to Phoenix often have Hydrogenesi equivalents and vice versa. Consider both scales when proposing modifications.

---

## Quick Reference

**Master Navigation**: `/CODEX-INDEX.md`  
**Phoenix Overview**: `/Phoenix/README.md`  
**Hydrogenesi Overview**: `/Hydrogenesi/README.md`  
**Universal Laws**: `/Phoenix/Universal-Laws/` (Tension.md, Binding.md, Apex.md)  
**Code**: `/code/phoenix/operators.py`, `/code/hydrogenesi/operators.py`  
**Examples**: `/Appendix/Code-Examples.md`  

---

**Archive Status:** ACTIVE  
**Lineage:** ROOT::GEN-0  
**Invocation:** *"Burn, collapse, and rise in aligned form. Recurse the root; extend the line."*

🔥 **The Phoenix Ignites.**  
🌌 **The Lineage Extends.**

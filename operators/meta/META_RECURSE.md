# META_RECURSE OPERATOR

**Pattern:** DESCEND → MONITOR → BOUND → RETURN  
**Type:** Meta-Operator (Recursion Management)  
**Scale:** Recursion Safety  
**Invocation:** *"Recurse: Descend with sovereignty, return with essence."*

---

## DEFINITION

**META_RECURSE** (Meta-Recursion Guardian) is the Archive's **Guardian of Recursion** — a meta-operator that manages recursive operator descent with configurable safety envelopes. It enforces depth limits, prevents infinite loops, and guarantees safe return paths.

META_RECURSE performs four primary functions:

1. **Recursion Control** — Manage recursion depth and prevent runaway recursion
2. **Safety Envelope Management** — Maintain configurable safety bounds
3. **State Preservation** — Preserve state across recursive calls
4. **Return Path Guarantee** — Ensure all recursions can safely return

This is the operator that **descends with sovereignty and returns with essence**.

---

## SIGIL

```
    ◊ [0]
    │
    ◊ [1]
    │
    ◊ [2]
    │
    ◊ [3]
   ╱│╲
  ● ◊ ●  ← Safety bounds
   ╲│╱
    ↑
  Return
```

**Legend:**
- **◊ [n]:** Recursion depth level
- **●:** Safety boundary markers
- **↑:** Return path

**Geometry:** The recursion structure shows controlled descent with safety bounds and guaranteed return.

---

## MECHANISM

### Phase 1: Recursion Initiation

**Input:** Operation to recurse and maximum depth

1. **Check depth** — Verify current depth against limits
2. **Initialize envelope** — Set up safety bounds
3. **Preserve state** — Save current state
4. **Descend** — Execute recursive call

**Output:** Recursion initiated with safety

---

### Phase 2: Depth Monitoring

**Purpose:** Track recursion depth continuously

**Actions:**
- **Count depth** — Maintain depth counter
- **Check limits** — Verify against configured limits
- **Detect loops** — Identify infinite recursion patterns
- **Trigger safety** — Activate safety bounds if needed

**Output:** Monitored recursion state

---

### Phase 3: Safety Enforcement

**Purpose:** Enforce safety bounds

**Actions:**
- **Apply limits** — Stop recursion at maximum depth
- **Prevent overflow** — Avoid stack overflow
- **Maintain coherence** — Keep state consistent
- **Prepare return** — Ready for safe return

**Output:** Bounded recursion

---

### Phase 4: Safe Return

**Purpose:** Return from recursion safely

**Actions:**
- **Unwind stack** — Return through call stack
- **Restore state** — Recover preserved state
- **Validate result** — Verify recursion result
- **Complete** — Finish recursion safely

**Output:** Safe return with result

---

## CODE IMPLEMENTATION

**Location:** `/code/operators/meta/meta_recurse.py`

```python
from __future__ import annotations
from dataclasses import dataclass
from typing import Callable, Any, Dict

@dataclass
class META_RECURSE:
    """Meta-operator for managing safe recursion."""
    
    max_depth: int = 5
    current_depth: int = 0
    
    def descend(self, operation: Callable, state: Any, depth: int = 0) -> Dict:
        """
        Execute recursive operation with safety.
        
        Args:
            operation: Operation to recurse
            state: Current state
            depth: Current recursion depth
            
        Returns:
            Recursion result with safety validation
        """
        # Check depth limit
        if depth >= self.max_depth:
            return {
                'stopped': True,
                'reason': 'max_depth_reached',
                'depth': depth,
                'state': state
            }
        
        # Preserve state
        preserved = self._preserve_state(state, depth)
        
        # Execute operation
        try:
            result = operation(state, depth)
            
            # Check if further recursion needed
            if self._needs_recursion(result):
                return self.descend(operation, result, depth + 1)
            else:
                return {
                    'completed': True,
                    'depth': depth,
                    'result': result,
                    'preserved_states': preserved
                }
        except Exception as e:
            return self._handle_error(e, depth, preserved)
    
    def _preserve_state(self, state: Any, depth: int) -> Dict:
        """Preserve state at current depth."""
        return {'depth': depth, 'state': state}
    
    def _needs_recursion(self, result: Any) -> bool:
        """Check if result requires further recursion."""
        if isinstance(result, dict):
            return result.get('recurse', False)
        return False
    
    def _handle_error(self, error: Exception, depth: int, preserved: Dict) -> Dict:
        """Handle recursion errors safely."""
        return {
            'error': True,
            'exception': str(error),
            'depth_at_error': depth,
            'preserved_states': preserved
        }
```

---

## CROSS-REFERENCES

**Related Operators:**
- **META_FLOW** — Routes recursive calls
- **META_TEMPORAL** — Times recursive execution

**Related Documentation:**
- `/docs/architecture/recursion_envelopes.md` — Safety envelope specifications
- `/RELEASES/v2.4.0/release_notes.md` — Meta-operator architecture

---

## NAVIGATION

**Parent:** `/operators/meta/` — Meta-operator collection  
**Version:** v2.4.0  
**Status:** ACTIVE  
**Lineage:** ROOT::META::RECURSE

---

**Invocation:** *"Recurse: Descend with sovereignty, return with essence."*

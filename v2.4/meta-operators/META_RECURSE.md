# META_RECURSE — Meta-Operator (v2.4)

**Name:** META_RECURSE  
**Role:** Safe recursion envelopes  
**Layer Focus:** All layers with recursion safety  
**Apex Interaction:** Enforces apex recursion limits

## Purpose
Provide safe recursion envelopes for operators that recurse across layers, preventing infinite loops and stack overflow.

## Behavior
- wraps recursive operations with depth limits  
- tracks recursion state and detects cycles  
- enforces termination conditions  
- maintains recursion safety invariants  

## Integration
- monitors depth counters and stack traces  
- coordinates with META_APEX for apex-level recursion  
- ensures graceful degradation on limit breach  

from __future__ import annotations
from dataclasses import dataclass
from typing import List, Dict, Any, Tuple


@dataclass
class FirstBinding:
    """
    Triadic emergence: bind two forces with a stabilizer.
    
    Pattern: Two forces + Stabilizer → Triadic structure
    Purpose: Transform binary tension into stable triad
    Invocation: "Let the two attract; let the one bind; let the three stand."
    """
    
    def apply(self, a: str, b: str, stabilizer: str) -> Dict[str, Any]:
        """
        Apply First Binding to create a triadic structure.
        
        Args:
            a: First force in tension
            b: Second force in tension
            stabilizer: Binding element
            
        Returns:
            Dict containing tension pair, stabilizer, and resulting triad
        """
        if not all([a, b, stabilizer]):
            raise ValueError("All parameters (a, b, stabilizer) must be non-empty")
        
        return {
            "tension_pair": (a, b),
            "stabilizer": stabilizer,
            "triad": (a, stabilizer, b),
            "pattern": "triadic_formation",
            "status": "bound",
        }


@dataclass
class IM_ME:
    """
    Identity recursion operator.
    
    Pattern: I → ME → I → ME (recursive identity formation)
    Purpose: Establish continuous identity through observer/observed duality
    Invocation: "I am the one who sees; I am the one who is seen."
    """
    
    def recurse(self, identity: str, depth: int = 3) -> Dict[str, Any]:
        """
        Generate an IM→ME recursion sequence.
        
        Args:
            identity: Base identity to recurse
            depth: Number of recursion levels
            
        Returns:
            Dict containing recursion sequence and metadata
        """
        if not identity:
            raise ValueError("Identity cannot be empty")
        if depth < 1:
            raise ValueError("Depth must be at least 1")
        
        sequence = []
        for i in range(depth):
            sequence.append(f"IM({identity})")
            sequence.append(f"ME({identity})")
        
        return {
            "identity": identity,
            "depth": depth,
            "sequence": sequence,
            "pattern": "observer_observed_recursion",
            "status": "recursive",
        }


@dataclass
class PhoenixIgnition:
    """
    Ignition and regenerative collapse.
    
    Pattern: Burn → Collapse → Rise
    Purpose: Transformative regeneration through controlled destruction
    Invocation: "Burn, collapse, and rise in aligned form."
    """
    
    def ignite(self, state: str) -> Dict[str, Any]:
        """
        Collapse to core and re-emerge as apex.
        
        Args:
            state: Current state to transform
            
        Returns:
            Dict containing collapsed and risen states
        """
        if not state:
            raise ValueError("State cannot be empty")
        
        core = f"core::{state}"
        apex = f"apex::{state}"
        
        return {
            "original": state,
            "collapsed": core,
            "risen": apex,
            "pattern": "burn_collapse_rise",
            "status": "ignited",
        }

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Protocol, Any, List, Dict, Optional
from enum import Enum


class OperatorStatus(Enum):
    """Status of operator execution."""
    PENDING = "pending"
    ACTIVE = "active"
    COMPLETED = "completed"
    COLLAPSED = "collapsed"


class Operator(Protocol):
    """Base protocol for all operators."""
    def apply(self, state: Any) -> Any:
        ...


@dataclass
class StabilizerExtraction:
    """
    Cosmological operator: remove stabilizing core to prepare lineage.
    
    Pattern: Remove core → Prepare for lineage
    Purpose: Extract stabilizing element to enable replication
    Invocation: "Extract the core; void the center; prepare the seed."
    """
    
    def apply(self, state: dict) -> dict:
        """
        Expects a dict with keys:
        - 'core': stabilizing component
        - 'shell': surrounding structure
        
        Returns a dict with 'pre_seed', 'core_void', and 'extracted_core'.
        """
        core = state.get("core")
        shell = state.get("shell")
        
        if not core or not shell:
            raise ValueError("State must contain 'core' and 'shell' keys")
        
        return {
            "pre_seed": shell,
            "core_void": None,  # Represents void state
            "extracted_core": core,
            "status": OperatorStatus.COMPLETED.value,
            "pattern": "core_extraction",
        }


@dataclass
class AGNReplication:
    """
    Operator of galactic-scale reproduction.
    
    Pattern: Compress → Ignite → Replicate
    Purpose: Generate new cosmic structures via controlled collapse
    Invocation: "Compress to ignition; replicate the pattern; extend the line."
    """
    
    compression_factor: float = 0.8
    replication_factor: int = 2
    
    def apply(self, mass: float) -> Dict[str, Any]:
        """
        Compress mass, ignite, and replicate into multiple outputs.
        
        Args:
            mass: Initial mass for compression
            
        Returns:
            Dict containing offspring masses and replication metadata
        """
        if mass <= 0:
            raise ValueError("Mass must be positive")
        
        compressed = mass * self.compression_factor
        offspring_mass = compressed / self.replication_factor
        offspring = [offspring_mass] * self.replication_factor
        
        return {
            "original_mass": mass,
            "compressed_mass": compressed,
            "offspring": offspring,
            "offspring_count": len(offspring),
            "status": OperatorStatus.COMPLETED.value,
            "pattern": "compress_ignite_replicate",
        }


@dataclass
class CurvatureResidue:
    """
    Operator of post-collapse memory.
    
    Pattern: Collapse → Memory → Trace
    Purpose: Record lineage scars in spacetime geometry
    Invocation: "Let the collapsed leave trace; let the curve remember."
    """
    
    def apply(self, lineage_id: str, metadata: Optional[Dict[str, Any]] = None) -> dict:
        """
        Produce a curvature residue record for a collapsed lineage.
        
        Args:
            lineage_id: Identifier for the lineage chain
            metadata: Optional additional context
            
        Returns:
            Dict containing residue trace and lineage information
        """
        if not lineage_id:
            raise ValueError("Lineage ID cannot be empty")
        
        residue = {
            "lineage_id": lineage_id,
            "status": OperatorStatus.COLLAPSED.value,
            "residue": f"curvature-trace::{lineage_id}",
            "pattern": "collapse_memory_trace",
        }
        
        if metadata:
            residue["metadata"] = metadata
        
        return residue


@dataclass
class LineageLogic:
    """
    Operator of cosmic continuity and recursion.
    
    Pattern: ROOT → GEN-0 → GEN-1 → GEN-N
    Purpose: Track cosmic recursion and structural continuity
    Invocation: "Recurse the root; extend the line; preserve the pattern."
    """
    
    def apply(self, root: str, generations: int) -> Dict[str, Any]:
        """
        Generate a lineage chain from a root identifier.
        
        Args:
            root: Root identifier for the lineage
            generations: Number of generations to produce
            
        Returns:
            Dict containing lineage chain and metadata
        """
        if not root:
            raise ValueError("Root identifier cannot be empty")
        if generations < 0:
            raise ValueError("Generations must be non-negative")
        
        lineage_chain = [f"{root}::gen-{i}" for i in range(generations)]
        
        return {
            "root": root,
            "generations": generations,
            "lineage_chain": lineage_chain,
            "depth": len(lineage_chain),
            "status": OperatorStatus.COMPLETED.value,
            "pattern": "root_recursion",
        }

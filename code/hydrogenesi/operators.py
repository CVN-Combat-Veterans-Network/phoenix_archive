from __future__ import annotations
from dataclasses import dataclass
from typing import Protocol, Any, List


class Operator(Protocol):
    def apply(self, state: Any) -> Any:
        ...


@dataclass
class StabilizerExtraction:
    """Cosmological operator: remove stabilizing core to prepare lineage."""

    def apply(self, state: dict) -> dict:
        """
        Expects a dict with keys:
        - 'core': stabilizing component
        - 'shell': surrounding structure
        Returns a dict with 'pre_seed' and 'core_void'.
        """
        core = state.get("core")
        shell = state.get("shell")
        return {
            "pre_seed": shell,
            "core_void": None,
            "extracted_core": core,
        }


@dataclass
class AGNReplication:
    """Operator of galactic-scale reproduction."""

    compression_factor: float = 0.8
    replication_factor: int = 2

    def apply(self, mass: float) -> List[float]:
        """
        Compress mass, ignite, and replicate into multiple outputs.
        """
        compressed = mass * self.compression_factor
        return [compressed / self.replication_factor] * self.replication_factor


@dataclass
class CurvatureResidue:
    """Operator of post-collapse memory."""

    def apply(self, lineage_id: str) -> dict:
        """
        Produce a curvature residue record for a collapsed lineage.
        """
        return {
            "lineage_id": lineage_id,
            "status": "collapsed",
            "residue": f"curvature-trace::{lineage_id}",
        }


@dataclass
class LineageLogic:
    """Operator of cosmic continuity and recursion."""

    def apply(self, root: str, generations: int) -> List[str]:
        """
        Generate a simple lineage chain from a root identifier.
        """
        return [f"{root}::gen-{i}" for i in range(generations)]

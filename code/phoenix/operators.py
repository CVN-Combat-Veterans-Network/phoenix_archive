from __future__ import annotations
from dataclasses import dataclass
from typing import List


@dataclass
class FirstBinding:
    """Triadic emergence: bind two forces with a stabilizer."""

    def apply(self, a: str, b: str, stabilizer: str) -> dict:
        return {
            "tension_pair": (a, b),
            "stabilizer": stabilizer,
            "triad": (a, stabilizer, b),
        }


@dataclass
class IM_ME:
    """Identity recursion operator."""

    def recurse(self, identity: str, depth: int = 3) -> List[str]:
        """
        Generate an IM→ME recursion sequence.
        """
        sequence = []
        for i in range(depth):
            sequence.append(f"IM({identity})")
            sequence.append(f"ME({identity})")
        return sequence


@dataclass
class PhoenixIgnition:
    """Ignition and regenerative collapse."""

    def ignite(self, state: str) -> dict:
        """
        Collapse to core and re-emerge as apex.
        """
        core = f"core::{state}"
        apex = f"apex::{state}"
        return {"collapsed": core, "risen": apex}

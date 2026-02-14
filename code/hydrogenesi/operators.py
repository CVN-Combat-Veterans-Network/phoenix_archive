from __future__ import annotations
from dataclasses import dataclass, field
from typing import Protocol, Any, List, Dict, Optional
from enum import Enum
import math


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


@dataclass
class HarmonicRecursion:
    """
    v2.3 Recursion Mode: Wave-based recursion with frequency/amplitude control.
    
    Pattern: Frequency → Amplitude → Damping → Depth
    Purpose: Enable natural, energy-conserving recursion patterns
    Invocation: "Let frequencies align; let amplitudes guide; let the wave recurse."
    """
    
    frequency: float = 1.0
    amplitude: float = 1.0
    damping: float = 0.1
    
    def set_frequency(self, frequency: float) -> None:
        """
        Set the recursion frequency parameter.
        
        Higher frequency = faster oscillation = more recursion cycles
        Lower frequency = slower oscillation = fewer recursion cycles
        
        Args:
            frequency: Frequency value (typically 0.1 to 10.0)
        """
        if frequency <= 0:
            raise ValueError("Frequency must be positive")
        self.frequency = frequency
    
    def get_frequency_characteristics(self) -> Dict[str, Any]:
        """
        Get characteristics of the current frequency setting.
        
        Returns:
            Dict containing frequency analysis
        """
        period = 2 * math.pi / self.frequency if self.frequency > 0 else float('inf')
        
        return {
            "frequency": self.frequency,
            "period": period,
            "cycles_per_unit": self.frequency / (2 * math.pi),
            "category": self._categorize_frequency(),
        }
    
    def _categorize_frequency(self) -> str:
        """Categorize frequency into ranges."""
        if self.frequency < 0.5:
            return "low_frequency"
        elif self.frequency < 2.0:
            return "medium_frequency"
        else:
            return "high_frequency"
    
    def set_amplitude(self, amplitude: float) -> None:
        """
        Set the recursion amplitude parameter.
        
        Amplitude controls the maximum depth of recursion.
        Higher amplitude = deeper recursion potential
        Lower amplitude = shallower recursion potential
        
        Args:
            amplitude: Amplitude value (typically 0.1 to 10.0)
        """
        if amplitude <= 0:
            raise ValueError("Amplitude must be positive")
        self.amplitude = amplitude
    
    def modulate_amplitude(self, factor: float) -> float:
        """
        Modulate amplitude by a given factor.
        
        Args:
            factor: Multiplication factor for amplitude
            
        Returns:
            New amplitude value
        """
        if factor <= 0:
            raise ValueError("Modulation factor must be positive")
        
        self.amplitude *= factor
        return self.amplitude
    
    def get_amplitude_characteristics(self) -> Dict[str, Any]:
        """
        Get characteristics of the current amplitude setting.
        
        Returns:
            Dict containing amplitude analysis
        """
        return {
            "amplitude": self.amplitude,
            "max_potential_depth": self.amplitude * 10,  # Approximate max depth
            "category": self._categorize_amplitude(),
            "energy_level": "high" if self.amplitude > 2.0 else "medium" if self.amplitude > 0.5 else "low",
        }
    
    def _categorize_amplitude(self) -> str:
        """Categorize amplitude into ranges."""
        if self.amplitude < 0.5:
            return "low_amplitude"
        elif self.amplitude < 2.0:
            return "medium_amplitude"
        else:
            return "high_amplitude"
    
    def set_damping(self, damping: float) -> None:
        """
        Set the recursion damping parameter.
        
        Damping controls the exponential decay of recursion over generations.
        Higher damping = faster decay = shorter recursion lifetime
        Lower damping = slower decay = longer recursion lifetime
        
        Args:
            damping: Damping coefficient (typically 0.0 to 1.0)
        """
        if damping < 0:
            raise ValueError("Damping must be non-negative")
        self.damping = damping
    
    def calculate_damping_factor(self, n: int) -> float:
        """
        Calculate exponential damping factor for generation n.
        
        Args:
            n: Generation number
            
        Returns:
            Damping factor value (between 0 and 1)
        """
        return math.exp(-self.damping * n)
    
    def get_damping_characteristics(self) -> Dict[str, Any]:
        """
        Get characteristics of the current damping setting.
        
        Returns:
            Dict containing damping analysis
        """
        # Calculate half-life: when damping factor = 0.5
        half_life = math.log(2) / self.damping if self.damping > 0 else float('inf')
        
        return {
            "damping": self.damping,
            "half_life": half_life,
            "decay_rate": self.damping * 100,  # As percentage
            "category": self._categorize_damping(),
        }
    
    def _categorize_damping(self) -> str:
        """Categorize damping into ranges."""
        if self.damping < 0.05:
            return "low_damping"
        elif self.damping < 0.2:
            return "medium_damping"
        else:
            return "high_damping"
    
    def apply(self, n: int, max_depth: int = 10) -> Dict[str, Any]:
        """
        Calculate harmonic recursion depth for generation n.
        
        Formula: depth(n) = amplitude * sin(frequency * n) * e^(-damping * n)
        
        Args:
            n: Current generation number
            max_depth: Maximum allowed recursion depth
            
        Returns:
            Dict containing depth, wave parameters, and recursion metadata
        """
        if n < 0:
            raise ValueError("Generation number must be non-negative")
        if max_depth <= 0:
            raise ValueError("Max depth must be positive")
        
        # Calculate harmonic depth
        raw_depth = self.amplitude * math.sin(self.frequency * n) * math.exp(-self.damping * n)
        
        # Normalize to valid depth range [0, max_depth]
        normalized_depth = max(0, min(max_depth, abs(raw_depth) * max_depth))
        
        return {
            "generation": n,
            "raw_depth": raw_depth,
            "normalized_depth": normalized_depth,
            "frequency": self.frequency,
            "amplitude": self.amplitude,
            "damping": self.damping,
            "max_depth": max_depth,
            "status": OperatorStatus.COMPLETED.value,
            "pattern": "harmonic_recursion",
            "recursion_mode": "harmonic",
        }


@dataclass
class MetaRecursion:
    """
    v2.3 Recursion Mode: Second-order recursion that operates on recursion patterns.
    
    Pattern: Introspect → Adjust → Recurse → Meta
    Purpose: Enable adaptive, self-modifying recursion
    Invocation: "Let recursion witness recursion; let patterns evolve; let meta emerge."
    """
    
    base_depth: int = 3
    adaptation_rate: float = 0.1
    complexity_threshold: float = 0.5
    
    def apply(self, pattern: Dict[str, Any], iterations: int = 5) -> Dict[str, Any]:
        """
        Apply meta-recursion to an existing recursion pattern.
        
        Meta-recursion observes and modifies recursion parameters dynamically.
        
        Args:
            pattern: Base recursion pattern to meta-recurse
            iterations: Number of meta-recursion iterations
            
        Returns:
            Dict containing evolved pattern and meta-recursion trace
        """
        if iterations < 0:
            raise ValueError("Iterations must be non-negative")
        
        trace = []
        current_pattern = pattern.copy()
        current_depth = self.base_depth
        
        for i in range(iterations):
            # Introspect current recursion pattern
            complexity = self._calculate_complexity(current_pattern)
            
            # Adjust parameters based on complexity
            adjustment = self._calculate_adjustment(complexity)
            current_depth = max(1, int(current_depth * (1 + adjustment)))
            
            # Apply adjusted recursion
            current_pattern["depth"] = current_depth
            current_pattern["complexity"] = complexity
            current_pattern["adjustment"] = adjustment
            
            # Record trace
            trace.append({
                "iteration": i,
                "depth": current_depth,
                "complexity": complexity,
                "adjustment": adjustment,
            })
        
        return {
            "original_pattern": pattern,
            "evolved_pattern": current_pattern,
            "iterations": iterations,
            "trace": trace,
            "final_depth": current_depth,
            "status": OperatorStatus.COMPLETED.value,
            "pattern": "meta_recursion",
            "recursion_mode": "meta",
        }
    
    def _calculate_complexity(self, pattern: Dict[str, Any]) -> float:
        """
        Calculate complexity metric of current recursion pattern.
        
        Args:
            pattern: Recursion pattern to analyze
            
        Returns:
            Complexity value between 0.0 and 1.0
        """
        # Simple complexity metric based on depth and number of parameters
        depth = pattern.get("depth", self.base_depth)
        param_count = len(pattern.keys())
        
        # Normalize to [0, 1] range
        complexity = min(1.0, (depth / 10.0 + param_count / 20.0) / 2.0)
        return complexity
    
    def _calculate_adjustment(self, complexity: float) -> float:
        """
        Calculate parameter adjustment based on complexity.
        
        Args:
            complexity: Current complexity measure
            
        Returns:
            Adjustment factor (positive = increase, negative = decrease)
        """
        # If below threshold, increase depth (positive adjustment)
        # If above threshold, decrease depth (negative adjustment)
        deviation = complexity - self.complexity_threshold
        adjustment = -deviation * self.adaptation_rate
        
        return adjustment
    
    def introspect_pattern(self, pattern: Dict[str, Any]) -> Dict[str, Any]:
        """
        Perform deep introspection on recursion pattern.
        
        Args:
            pattern: Recursion pattern to introspect
            
        Returns:
            Dict containing pattern analysis
        """
        complexity = self._calculate_complexity(pattern)
        depth = pattern.get("depth", self.base_depth)
        
        # Analyze pattern structure
        analysis = {
            "complexity": complexity,
            "depth": depth,
            "parameter_count": len(pattern.keys()),
            "complexity_category": self._categorize_complexity(complexity),
            "depth_category": self._categorize_depth(depth),
            "optimization_suggestion": self._suggest_optimization(complexity, depth),
        }
        
        return analysis
    
    def adjust_parameters_dynamic(
        self, 
        pattern: Dict[str, Any],
        target_complexity: float
    ) -> Dict[str, Any]:
        """
        Dynamically adjust recursion parameters to target complexity.
        
        Args:
            pattern: Current recursion pattern
            target_complexity: Desired complexity level (0.0 to 1.0)
            
        Returns:
            Adjusted pattern with new parameters
        """
        if not (0.0 <= target_complexity <= 1.0):
            raise ValueError("Target complexity must be between 0.0 and 1.0")
        
        current_complexity = self._calculate_complexity(pattern)
        adjusted_pattern = pattern.copy()
        
        # Calculate required depth adjustment
        complexity_gap = target_complexity - current_complexity
        depth_adjustment = complexity_gap / self.adaptation_rate
        
        current_depth = pattern.get("depth", self.base_depth)
        new_depth = max(1, int(current_depth + depth_adjustment))
        
        adjusted_pattern["depth"] = new_depth
        adjusted_pattern["target_complexity"] = target_complexity
        adjusted_pattern["adjustment_applied"] = depth_adjustment
        
        return {
            "original_pattern": pattern,
            "adjusted_pattern": adjusted_pattern,
            "original_complexity": current_complexity,
            "target_complexity": target_complexity,
            "depth_change": new_depth - current_depth,
            "status": "adjusted",
        }
    
    def _categorize_complexity(self, complexity: float) -> str:
        """Categorize complexity into ranges."""
        if complexity < 0.3:
            return "low_complexity"
        elif complexity < 0.7:
            return "medium_complexity"
        else:
            return "high_complexity"
    
    def _categorize_depth(self, depth: int) -> str:
        """Categorize depth into ranges."""
        if depth < 3:
            return "shallow"
        elif depth < 7:
            return "medium"
        else:
            return "deep"
    
    def _suggest_optimization(self, complexity: float, depth: int) -> str:
        """Suggest optimization based on complexity and depth."""
        if complexity > 0.8 and depth > 8:
            return "reduce_depth_for_efficiency"
        elif complexity < 0.2 and depth < 2:
            return "increase_depth_for_richness"
        else:
            return "optimal_balance"

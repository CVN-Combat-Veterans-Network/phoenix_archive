"""
Telemetry & Logging Module for Integration Engine

Provides production-ready monitoring with structured logging
and performance metrics collection.
"""

from __future__ import annotations
from typing import Dict, List, Any, Optional
from datetime import datetime
import logging
import json
from .meta_operators import WaltzPhase
from .cache import CachedThreeFingerWaltz


class WaltzLogger:
    """
    Structured logging for Integration Engine.
    
    Provides JSON-formatted logs for integration with monitoring
    and log aggregation systems.
    """
    
    def __init__(self, name: str = "integration_engine", level: int = logging.INFO):
        """
        Initialize logger.
        
        Args:
            name: Logger name
            level: Logging level (default: INFO)
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        # Remove existing handlers to avoid duplicates
        self.logger.handlers = []
        
        # JSON formatter
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '{"time": "%(asctime)s", "level": "%(levelname)s", "message": %(message)s}'
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
    
    def log_waltz_start(self, patterns_count: int):
        """
        Log waltz execution start.
        
        Args:
            patterns_count: Number of patterns being integrated
        """
        self.logger.info(json.dumps({
            "event": "waltz_start",
            "patterns_count": patterns_count,
            "timestamp": datetime.now().isoformat()
        }))
    
    def log_waltz_complete(self, result: Dict[str, Any], duration: float):
        """
        Log successful waltz completion.
        
        Args:
            result: Waltz result dictionary
            duration: Execution duration in seconds
        """
        self.logger.info(json.dumps({
            "event": "waltz_complete",
            "status": result.get("status"),
            "recursion_depth": result.get("recursion_depth"),
            "energy_conservation": result.get("energy_conservation"),
            "duration_seconds": duration,
            "from_cache": result.get("from_cache", False),
            "timestamp": datetime.now().isoformat()
        }))
    
    def log_waltz_error(self, error: Exception, patterns_count: Optional[int] = None):
        """
        Log waltz execution error.
        
        Args:
            error: Exception that occurred
            patterns_count: Number of patterns (if known)
        """
        self.logger.error(json.dumps({
            "event": "waltz_error",
            "error_type": type(error).__name__,
            "error_message": str(error),
            "patterns_count": patterns_count,
            "timestamp": datetime.now().isoformat()
        }))
    
    def log_cache_hit(self, patterns_count: int):
        """
        Log cache hit.
        
        Args:
            patterns_count: Number of patterns
        """
        self.logger.debug(json.dumps({
            "event": "cache_hit",
            "patterns_count": patterns_count,
            "timestamp": datetime.now().isoformat()
        }))
    
    def log_cache_miss(self, patterns_count: int):
        """
        Log cache miss.
        
        Args:
            patterns_count: Number of patterns
        """
        self.logger.debug(json.dumps({
            "event": "cache_miss",
            "patterns_count": patterns_count,
            "timestamp": datetime.now().isoformat()
        }))


class WaltzMetrics:
    """
    Collect performance metrics for Integration Engine.
    
    Tracks execution statistics, timing, and performance indicators
    for operational monitoring.
    """
    
    def __init__(self):
        """Initialize metrics collector."""
        self.total_executions = 0
        self.total_duration = 0.0
        self.total_patterns = 0
        self.error_count = 0
        self.phase_durations: Dict[WaltzPhase, List[float]] = {
            phase: [] for phase in WaltzPhase
        }
        self._start_time = datetime.now()
    
    def record_execution(
        self, 
        duration: float, 
        patterns_count: int, 
        phases: Optional[Dict[WaltzPhase, float]] = None
    ):
        """
        Record successful waltz execution.
        
        Args:
            duration: Total execution duration in seconds
            patterns_count: Number of patterns integrated
            phases: Optional dict of phase durations
        """
        self.total_executions += 1
        self.total_duration += duration
        self.total_patterns += patterns_count
        
        if phases:
            for phase, phase_duration in phases.items():
                self.phase_durations[phase].append(phase_duration)
    
    def record_error(self):
        """Record execution error."""
        self.error_count += 1
    
    def get_summary(self) -> Dict[str, Any]:
        """
        Get metrics summary.
        
        Returns:
            Dictionary with aggregated metrics
        """
        avg_duration = (
            self.total_duration / self.total_executions 
            if self.total_executions > 0 
            else 0
        )
        
        avg_patterns = (
            self.total_patterns / self.total_executions 
            if self.total_executions > 0 
            else 0
        )
        
        error_rate = (
            self.error_count / (self.total_executions + self.error_count) 
            if (self.total_executions + self.error_count) > 0 
            else 0
        )
        
        phase_avg_durations = {
            phase.value: (
                sum(durations) / len(durations) 
                if durations 
                else 0
            )
            for phase, durations in self.phase_durations.items()
        }
        
        uptime = (datetime.now() - self._start_time).total_seconds()
        
        return {
            "total_executions": self.total_executions,
            "avg_duration_seconds": avg_duration,
            "avg_patterns_per_execution": avg_patterns,
            "error_count": self.error_count,
            "error_rate": error_rate,
            "phase_avg_durations": phase_avg_durations,
            "total_duration_seconds": self.total_duration,
            "uptime_seconds": uptime,
            "executions_per_minute": (
                (self.total_executions / uptime) * 60 
                if uptime > 0 
                else 0
            )
        }
    
    def reset(self):
        """Reset all metrics."""
        self.total_executions = 0
        self.total_duration = 0.0
        self.total_patterns = 0
        self.error_count = 0
        self.phase_durations = {phase: [] for phase in WaltzPhase}
        self._start_time = datetime.now()


class InstrumentedThreeFingerWaltz(CachedThreeFingerWaltz):
    """
    Fully instrumented Three-Finger Waltz.
    
    Combines caching with comprehensive logging and metrics collection
    for production monitoring and observability.
    """
    
    def __init__(
        self, 
        cache_size: int = 128, 
        log_level: int = logging.INFO,
        **kwargs
    ):
        """
        Initialize instrumented waltz.
        
        Args:
            cache_size: Maximum cache size
            log_level: Logging level (default: INFO)
            **kwargs: Additional arguments for ThreeFingerWaltz
        """
        super().__init__(cache_size=cache_size, **kwargs)
        self.logger = WaltzLogger(level=log_level)
        self.metrics = WaltzMetrics()
    
    def _extract_phase_durations(self) -> Dict[WaltzPhase, float]:
        """
        Extract phase durations from step timestamps.
        
        Returns:
            Dictionary mapping phases to durations
        """
        phase_durations = {}
        
        if not self._steps:
            return phase_durations
        
        # Calculate duration for each phase based on timestamps
        for i, step in enumerate(self._steps):
            if i > 0:
                prev_timestamp = self._steps[i-1].timestamp
                duration = (step.timestamp - prev_timestamp).total_seconds()
                phase_durations[step.phase] = duration
            else:
                # First step duration from initialization
                duration = (step.timestamp - self._initialized_at).total_seconds()
                phase_durations[step.phase] = duration
        
        return phase_durations
    
    def __call__(self, patterns: List[Any]) -> Dict[str, Any]:
        """
        Execute instrumented waltz with full telemetry.
        
        Args:
            patterns: List of patterns to integrate
            
        Returns:
            Integration result with telemetry metadata
        """
        start_time = datetime.now()
        self.logger.log_waltz_start(len(patterns))
        
        try:
            # Execute waltz (with caching via parent)
            result = super().__call__(patterns)
            duration = (datetime.now() - start_time).total_seconds()
            
            # Log cache hit/miss
            if result.get("from_cache", False):
                self.logger.log_cache_hit(len(patterns))
            else:
                self.logger.log_cache_miss(len(patterns))
            
            # Record metrics
            phase_durations = self._extract_phase_durations()
            self.metrics.record_execution(duration, len(patterns), phase_durations)
            
            # Log completion
            self.logger.log_waltz_complete(result, duration)
            
            # Add telemetry to result
            result["telemetry"] = {
                "duration_seconds": duration,
                "cached": result.get("from_cache", False),
                "timestamp": datetime.now().isoformat()
            }
            
            return result
        
        except Exception as e:
            self.logger.log_waltz_error(e, len(patterns))
            self.metrics.record_error()
            raise
    
    def get_metrics_summary(self) -> Dict[str, Any]:
        """
        Get comprehensive metrics summary.
        
        Returns:
            Dictionary with metrics and cache stats
        """
        return {
            "metrics": self.metrics.get_summary(),
            "cache": self.cache_stats()
        }
    
    def reset(self):
        """Reset waltz, cache, and metrics."""
        super().reset()
        self.metrics.reset()

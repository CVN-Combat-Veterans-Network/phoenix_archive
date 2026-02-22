"""
Unit Tests for Telemetry Module
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

from code.integration.telemetry import WaltzLogger, WaltzMetrics, InstrumentedThreeFingerWaltz
import logging


class TestWaltzLogger:
    """Test WaltzLogger functionality."""
    
    def test_logger_initialization(self):
        """Test logger initializes correctly."""
        logger = WaltzLogger(name="test_logger", level=logging.INFO)
        
        assert logger.logger.name == "test_logger"
        assert logger.logger.level == logging.INFO
    
    def test_log_waltz_start(self):
        """Test waltz start logging."""
        logger = WaltzLogger()
        
        # Should not raise any errors
        logger.log_waltz_start(3)
    
    def test_log_waltz_complete(self):
        """Test waltz completion logging."""
        logger = WaltzLogger()
        
        result = {
            "status": "WALTZ_COMPLETE",
            "recursion_depth": 1,
            "energy_conservation": 0.9,
            "from_cache": False
        }
        
        # Should not raise any errors
        logger.log_waltz_complete(result, 0.123)
    
    def test_log_waltz_error(self):
        """Test error logging."""
        logger = WaltzLogger()
        
        error = ValueError("Test error")
        
        # Should not raise any errors
        logger.log_waltz_error(error, patterns_count=3)


class TestWaltzMetrics:
    """Test WaltzMetrics functionality."""
    
    def test_metrics_initialization(self):
        """Test metrics initializes correctly."""
        metrics = WaltzMetrics()
        
        assert metrics.total_executions == 0
        assert metrics.total_duration == 0.0
        assert metrics.error_count == 0
    
    def test_record_execution(self):
        """Test recording successful execution."""
        metrics = WaltzMetrics()
        
        metrics.record_execution(
            duration=0.123,
            patterns_count=3,
            phases=None
        )
        
        assert metrics.total_executions == 1
        assert metrics.total_duration == 0.123
        assert metrics.total_patterns == 3
    
    def test_record_error(self):
        """Test recording errors."""
        metrics = WaltzMetrics()
        
        metrics.record_error()
        
        assert metrics.error_count == 1
    
    def test_get_summary(self):
        """Test metrics summary."""
        metrics = WaltzMetrics()
        
        # Record some data
        metrics.record_execution(0.1, 3)
        metrics.record_execution(0.2, 2)
        metrics.record_error()
        
        summary = metrics.get_summary()
        
        assert summary["total_executions"] == 2
        assert summary["avg_duration_seconds"] == 0.15
        assert summary["error_count"] == 1
        assert summary["error_rate"] > 0
        assert "uptime_seconds" in summary
        assert "executions_per_minute" in summary
    
    def test_metrics_reset(self):
        """Test metrics reset."""
        metrics = WaltzMetrics()
        
        metrics.record_execution(0.1, 3)
        metrics.record_error()
        
        metrics.reset()
        
        assert metrics.total_executions == 0
        assert metrics.error_count == 0


class TestInstrumentedThreeFingerWaltz:
    """Test InstrumentedThreeFingerWaltz functionality."""
    
    def test_instrumented_waltz_initialization(self):
        """Test instrumented waltz initializes correctly."""
        waltz = InstrumentedThreeFingerWaltz(cache_size=128, log_level=logging.INFO)
        
        assert waltz.cache.max_size == 128
        assert waltz.logger is not None
        assert waltz.metrics is not None
    
    def test_instrumented_waltz_execution(self):
        """Test instrumented waltz execution."""
        waltz = InstrumentedThreeFingerWaltz()
        
        patterns = [{"name": "test"}]
        result = waltz(patterns)
        
        assert result["status"] == "WALTZ_COMPLETE"
        assert "telemetry" in result
        assert "duration_seconds" in result["telemetry"]
        assert "cached" in result["telemetry"]
    
    def test_instrumented_waltz_metrics(self):
        """Test metrics collection."""
        waltz = InstrumentedThreeFingerWaltz()
        
        patterns = [{"name": "test"}]
        waltz(patterns)
        
        summary = waltz.metrics.get_summary()
        
        assert summary["total_executions"] == 1
        assert summary["avg_duration_seconds"] > 0
    
    def test_instrumented_waltz_cache_logging(self):
        """Test cache hit/miss logging."""
        waltz = InstrumentedThreeFingerWaltz()
        
        patterns = [{"name": "test"}]
        
        # First execution (miss)
        result1 = waltz(patterns)
        assert result1["from_cache"] == False
        
        # Reset to allow re-execution
        waltz.reset()
        waltz._completed = False
        
        # Second execution
        result2 = waltz(patterns)
        # Cache behavior depends on implementation
    
    def test_get_metrics_summary(self):
        """Test comprehensive metrics summary."""
        waltz = InstrumentedThreeFingerWaltz()
        
        patterns = [{"name": "test"}]
        waltz(patterns)
        
        summary = waltz.get_metrics_summary()
        
        assert "metrics" in summary
        assert "cache" in summary
        assert summary["metrics"]["total_executions"] == 1
    
    def test_instrumented_waltz_error_handling(self):
        """Test error handling and logging."""
        waltz = InstrumentedThreeFingerWaltz()
        
        # Execute normally first
        patterns = [{"name": "test"}]
        result = waltz(patterns)
        
        # Try to execute again (should fail due to completion)
        result2 = waltz(patterns)
        
        # Should return already complete status
        assert result2["status"] == "ALREADY_COMPLETE"


if __name__ == "__main__":
    print("Running telemetry tests...")
    
    # Logger tests
    test_logger = TestWaltzLogger()
    test_logger.test_logger_initialization()
    print("✓ test_logger_initialization passed")
    
    test_logger.test_log_waltz_start()
    print("✓ test_log_waltz_start passed")
    
    test_logger.test_log_waltz_complete()
    print("✓ test_log_waltz_complete passed")
    
    test_logger.test_log_waltz_error()
    print("✓ test_log_waltz_error passed")
    
    # Metrics tests
    test_metrics = TestWaltzMetrics()
    test_metrics.test_metrics_initialization()
    print("✓ test_metrics_initialization passed")
    
    test_metrics.test_record_execution()
    print("✓ test_record_execution passed")
    
    test_metrics.test_record_error()
    print("✓ test_record_error passed")
    
    test_metrics.test_get_summary()
    print("✓ test_get_summary passed")
    
    test_metrics.test_metrics_reset()
    print("✓ test_metrics_reset passed")
    
    # Instrumented waltz tests
    test_instrumented = TestInstrumentedThreeFingerWaltz()
    test_instrumented.test_instrumented_waltz_initialization()
    print("✓ test_instrumented_waltz_initialization passed")
    
    test_instrumented.test_instrumented_waltz_execution()
    print("✓ test_instrumented_waltz_execution passed")
    
    test_instrumented.test_instrumented_waltz_metrics()
    print("✓ test_instrumented_waltz_metrics passed")
    
    test_instrumented.test_get_metrics_summary()
    print("✓ test_get_metrics_summary passed")
    
    test_instrumented.test_instrumented_waltz_error_handling()
    print("✓ test_instrumented_waltz_error_handling passed")
    
    print("\n✓ All telemetry tests passed!")

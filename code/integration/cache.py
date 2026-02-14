"""
Pattern Caching Module for Three-Finger Waltz

Provides LRU caching for repeated waltz pattern integrations
to improve performance and reduce redundant computations.
"""

from __future__ import annotations
from typing import Dict, List, Any, Optional
from hashlib import sha256
import json
from .meta_operators import ThreeFingerWaltz


class PatternCache:
    """
    LRU cache for repeated waltz patterns.
    
    Caches integration results based on pattern hash to avoid
    redundant waltz executions for identical pattern sets.
    """
    
    def __init__(self, max_size: int = 128):
        """
        Initialize pattern cache.
        
        Args:
            max_size: Maximum number of cached results
        """
        self.max_size = max_size
        self._cache: Dict[str, Dict[str, Any]] = {}
        self._access_count: Dict[str, int] = {}
        self._total_hits = 0
        self._total_misses = 0
    
    def _hash_patterns(self, patterns: List[Any]) -> str:
        """
        Generate SHA256 hash of pattern list.
        
        Args:
            patterns: List of patterns to hash
            
        Returns:
            Hexadecimal hash string
        """
        pattern_str = json.dumps(patterns, sort_keys=True, default=str)
        return sha256(pattern_str.encode()).hexdigest()
    
    def get(self, patterns: List[Any]) -> Optional[Dict[str, Any]]:
        """
        Retrieve cached result if exists.
        
        Args:
            patterns: List of patterns to look up
            
        Returns:
            Cached result dictionary, or None if not in cache
        """
        pattern_hash = self._hash_patterns(patterns)
        if pattern_hash in self._cache:
            self._access_count[pattern_hash] += 1
            self._total_hits += 1
            return self._cache[pattern_hash].copy()
        
        self._total_misses += 1
        return None
    
    def put(self, patterns: List[Any], result: Dict[str, Any]):
        """
        Cache integration result.
        
        Args:
            patterns: List of patterns that were integrated
            result: Result dictionary to cache
        """
        pattern_hash = self._hash_patterns(patterns)
        
        # LRU eviction if cache is full
        if len(self._cache) >= self.max_size and pattern_hash not in self._cache:
            # Find least recently used item
            lru_key = min(self._access_count, key=self._access_count.get)
            del self._cache[lru_key]
            del self._access_count[lru_key]
        
        self._cache[pattern_hash] = result.copy()
        self._access_count[pattern_hash] = 1
    
    def _calculate_hit_rate(self) -> float:
        """Calculate cache hit rate."""
        total = self._total_hits + self._total_misses
        if total == 0:
            return 0.0
        return self._total_hits / total
    
    def stats(self) -> Dict[str, Any]:
        """
        Cache statistics.
        
        Returns:
            Dictionary with cache metrics
        """
        return {
            "size": len(self._cache),
            "max_size": self.max_size,
            "total_accesses": sum(self._access_count.values()),
            "hit_rate": self._calculate_hit_rate(),
            "total_hits": self._total_hits,
            "total_misses": self._total_misses
        }
    
    def clear(self):
        """Clear all cached data."""
        self._cache.clear()
        self._access_count.clear()
        self._total_hits = 0
        self._total_misses = 0


class CachedThreeFingerWaltz(ThreeFingerWaltz):
    """
    Three-Finger Waltz with pattern caching.
    
    Extends ThreeFingerWaltz to cache results of pattern integrations,
    improving performance for repeated pattern sets.
    """
    
    def __init__(self, cache_size: int = 128, **kwargs):
        """
        Initialize cached waltz.
        
        Args:
            cache_size: Maximum cache size
            **kwargs: Additional arguments for ThreeFingerWaltz
        """
        super().__init__(**kwargs)
        self.cache = PatternCache(max_size=cache_size)
        self._cache_hits = 0
        self._cache_misses = 0
    
    def __call__(self, patterns: List[Any]) -> Dict[str, Any]:
        """
        Execute waltz with caching.
        
        Args:
            patterns: List of patterns to integrate
            
        Returns:
            Integration result (from cache or fresh execution)
        """
        # Try cache first
        cached = self.cache.get(patterns)
        if cached is not None:
            self._cache_hits += 1
            cached["from_cache"] = True
            cached["cache_hit"] = True
            return cached
        
        # Execute waltz
        self._cache_misses += 1
        result = super().__call__(patterns)
        
        # Cache result (only if successful)
        if result.get("status") == "WALTZ_COMPLETE":
            self.cache.put(patterns, result)
        
        result["from_cache"] = False
        result["cache_hit"] = False
        
        return result
    
    def cache_stats(self) -> Dict[str, Any]:
        """
        Cache performance statistics.
        
        Returns:
            Dictionary with cache metrics including hit/miss counts
        """
        base_stats = self.cache.stats()
        
        total_requests = self._cache_hits + self._cache_misses
        hit_rate = self._cache_hits / total_requests if total_requests > 0 else 0.0
        
        return {
            **base_stats,
            "waltz_cache_hits": self._cache_hits,
            "waltz_cache_misses": self._cache_misses,
            "waltz_hit_rate": hit_rate,
            "total_waltz_requests": total_requests
        }
    
    def reset(self):
        """Reset waltz and clear cache."""
        super().reset()
        self.cache.clear()
        self._cache_hits = 0
        self._cache_misses = 0

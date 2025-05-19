from MemoryCache import MemoryCache
from CacheStrategy import CacheStrategy
class CacheManager:

    def __init__(self, cache_strategies : dict[str, CacheStrategy]):
        self.cache : CacheStrategy = MemoryCache()
        self.cache_strategies = cache_strategies

    def get(self, key) -> dict:
        return self.cache.get(key)
    
    def put(self, key, response):
        return self.cache.put(key, response)
    
    def clear_all(self):
        for cache in self.cache_strategies.values():
            cache.clear()
        return 
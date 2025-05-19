from CacheStrategy import CacheStrategy

class MemoryCache(CacheStrategy):
    def __init__(self):
        self.cache = {}
    
    def get(self, key : str):
        return self.cache.get(key, {})
    
    def put(self, key: str, data: dict):
        self.cache["key"] = data
        return 
    
    def clear(self):
        self.cache.clear()
        return
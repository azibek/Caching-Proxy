from src.CacheStrategy import CacheStrategy

class MemoryCache(CacheStrategy): #TODO: check for serious caveats in python
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MemoryCache, cls).__new__(cls)
            cls._instance.cache = {}
        return cls._instance

    def get(self, key):
        return self.cache.get(key)

    def put(self, key, value):
        self.cache[key] = value

    def clear(self):
        self.cache.clear()

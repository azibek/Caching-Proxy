import unittest
import os
from pathlib import Path
from cache import CacheAPI

class TestJsonDumpMultipleWrites(unittest.TestCase):
    # def __init__(self, methodName = "runTest"):
    #     super().__init__(methodName)

    # def setUp(self, dir_path: str):
    #     # create a test directory and file
    #     os.makedirs(dir_path, exist_ok=True)
    #     return super().setUp()
    # def tearDown(self, dir_path):
    #     os.rmdir(dir_path)
    #     return super().tearDown()
    
    def test_writing_cache_to_json(self):
        cache_dir = os.getenv("CACHE_DIR", "C:\\Users\\Aqeel\\Documents\\projects\\Caching-Proxy") 
        
        cache_api = CacheAPI(cache_dir)
        file_name = "tmp.json"
        file_path = Path(cache_dir) / file_name
        id = "12345"
        status_code = 200
        content = {
            "content" : {
                "abc" : "xyz"
            }
        }
        data = {
            "id": id,
            "status_code": 200,
            "content" : content
        }
        cache_api.write_cache(status_code, content, file_path, id=id)
        self.assertTrue(file_path.exists())

        cache_exists = cache_api.cache_exists(id, file_path=file_path)
        print(file_path)
        self.assertTrue(cache_exists)

import json
from uuid import uuid4
from typing import Literal
from pathlib import Path
# VALID_STATUS_CODES = Literal[200] TODO: generate list of valid http codes.
class CacheAPI:
    def __init__(self, cache_dir):
        self.cache_dir : Path = Path(cache_dir)
        pass
    def cache_exists(self, key: str, path_params : dict = None, query_params : dict = None, body : dict = None, file_path : Path = None ):
        with open(file_path) as f:
            data = [json.loads(line) for line in f]
            # data = json.load(f)
        # print((data))
        keys = [b["id"] for b in data]
        print(keys, key)
        if key in keys: return True
        return False
        ...
    def write_cache(self, status_code, content, file_path : Path, id= str(uuid4())):
        if not file_path.exists():
            file_path.touch()
        data = {
            "id" : id,
            "status_code" : status_code,
            "content": json.dumps(content)
        }
        with open(file_path, "a") as f:
            f.write(json.dumps(data)+ "\n")

    def create_file(file_path: Path):
        file_path.touch(exist_ok=True)
        return None
        



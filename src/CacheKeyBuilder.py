import hashlib
import urllib.parse
from src.HttpInfo import RequestInfo

class CacheKeyBuilder:
    @staticmethod
    def build(request_info: RequestInfo) -> str:
        parsed_url = urllib.parse.urlparse(request_info.url)

        # Construct normalized query string from params
        normalized_query = urllib.parse.urlencode(sorted(request_info.params.items()))

        key_parts = [request_info.method.upper(), parsed_url.path, normalized_query]

        headers = request_info.headers or {}
        if 'Authorization' in headers:
            key_parts.append(headers['Authorization'])
        if 'Content-Type' in headers:
            key_parts.append(headers['Content-Type'])

        # if request_info.body:
        #     body_hash = hashlib.sha256(request_info.body.encode()).hexdigest()
        #     key_parts.append(body_hash)

        key_string = "|".join(key_parts)
        cache_key = hashlib.sha256(key_string.encode()).hexdigest()
        return cache_key


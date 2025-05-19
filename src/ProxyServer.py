import httpx
from fastapi import Request
from CacheManager import CacheManager
from CacheKeyBuilder import CachekeyBuilder
from HttpParser import HttpParser
from src.HttpInfo import RequestInfo
class ProxyServer:
    def __init__(self):
        self.cacheManager = CacheManager()
        self.CacheKeyBuilder = CachekeyBuilder
        self.requestParser = HttpParser # TODO: create a request parser (additionally create a data class to hold values like method, url, etc)
    
    def handle_request(self, request : Request):
        key = self.CacheKeyBuilder.build(request)

        cached_response = self.cacheManager.get(key)

        if cached_response:
            return cached_response
        
        req_info = HttpParser.parse_request(request)
        
        resp = self.fetch_from_origin(req_info)
        resp_json = resp.to_json()
        self.cacheManager.put(key, resp_json)
        return resp_json
    
    def get(self, key):
        return self.cacheManager.get(key)

    def put(self, key, response):
        return self.cacheManager.put(key, response)
    
    def clear(self, key):
        return self.cacheManager.clear(key)
    
    def clear_all(self):
        return self.cacheManager.clear_all()
    
    def fetch_from_origin(self, req_info : RequestInfo):
        client = httpx.AsyncClient()
        resp = client.request(
            method=req_info.method,
            url=req_info.url,
            headers=req_info.headers,
            params=req_info.params,
            body=req_info.body
        )

        return HttpParser.parse_response(resp)

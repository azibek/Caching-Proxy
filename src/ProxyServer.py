import httpx
from fastapi import Request, Response
from fastapi.responses import JSONResponse
from src.CacheManager import CacheManager
from src.CacheKeyBuilder import CacheKeyBuilder
from src.HttpParser import HttpParser
from src.HttpInfo import RequestInfo
from src.CacheStrategy import CacheStrategy
class ProxyServer:
    CACHE_HIT = "HIT"
    CACHE_MISS = "MISS"
    def __init__(self, cache_strategies : dict[str, CacheStrategy], upstream_base_url : str):
        self.cacheManager = CacheManager(cache_strategies)
        self.CacheKeyBuilder = CacheKeyBuilder
        self.requestParser = HttpParser # TODO: create a request parser (additionally create a data class to hold values like method, url, etc)
        self.base_url = upstream_base_url
    
    async def handle_request(self, request : Request):
        # extract necessary info from request object
        req_info = await HttpParser.parse_request(request, self.base_url)
        
        print("handle_request -> reqInfo",req_info.to_json())
        key = self.CacheKeyBuilder.build(req_info)

        cached_response_json = self.cacheManager.get(key)

        if cached_response_json:
            headers = {"X-CACHE": self.CACHE_HIT}
            print("Type of cached_response_json:", type(cached_response_json))

            print(headers)
            return JSONResponse(
                headers = headers,
                content=cached_response_json,
                media_type="application/json"
            )
        
        resp = await self.fetch_from_origin(req_info)
        resp_parsed = HttpParser.parse_response(resp)
        print(resp.content, "*" * 60)
        # resp_json = resp.to_json()
        if resp_parsed.status_code == 200:
            self.cacheManager.put(key, resp_parsed.to_json())
        headers = resp_parsed.headers
        headers["X-CACHE"] = self.CACHE_MISS
        return Response(
            status_code=resp_parsed.status_code,
            headers=headers,
            content=resp_parsed.content,
            media_type=resp_parsed.media_type
        )
    
    def get(self, key):
        return self.cacheManager.get(key)

    def put(self, key, response):
        return self.cacheManager.put(key, response)
    
    def clear(self, key):
        return self.cacheManager.clear(key)
    
    def clear_all(self):
        return self.cacheManager.clear_all()
    
    async def fetch_from_origin(self, req_info : RequestInfo):
        async with httpx.AsyncClient() as client:
            resp = await client.request(
                method=req_info.method,
                url=req_info.url,
                headers=req_info.headers,
                params=req_info.params
                # json=req_info.body
            )
            # print("Fetch_From_Origin", resp.json())

        return resp

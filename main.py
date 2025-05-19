from fastapi import FastAPI, Request, Response
import httpx
from  src.ProxyServer import ProxyServer
from src.MemoryCache import MemoryCache
app = FastAPI()
upstream_url = "https://api.agify.io/"  # example upstream base URL

'''
fastapi request layer and httpx response layers modify the original request to some degree, for more general proxy server, prefer go or rust"
'''
@app.api_route("/{full_path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS", "HEAD"])
async def proxy(full_path: str, request: Request):
    proxy_server = ProxyServer({"memory": MemoryCache()})
    return await proxy_server.handle_request(request)

import httpx
from fastapi import Request
from src.HttpInfo import RequestInfo, ResponseInfo
import datetime
class HttpParser:
    @staticmethod
    async def parse_request(request : Request) -> RequestInfo:

        method = request.method
        url = str(request.url) + request.path_params.get('full_path')
        headers = dict(request.headers)
        params = dict(request.query_params)
        body = await request.body()
        body = body.decode('utf-8')

        return RequestInfo(
            method,
            url,
            headers,
            params,
            body
        )
    
    @staticmethod
    def parse_response(response: httpx.Response) -> ResponseInfo:
        excluded_headers = {
            "content-encoding",
            "transfer-encoding",
            "connection",
            "keep-alive",
            "proxy-authenticate",
            "proxy-authorization",
            "te",
            "trailer",
            "upgrade",
            "content-length"
        }
        headers = {
            key.lower(): value for key, value in response.headers.items()
            if key.lower() not in excluded_headers
        }
        status_code = response.status_code
        content = response.content
        media_type = response.headers.get("content-type", "").split(";")[0].strip()
        url = str(response.url)
        timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()

        return ResponseInfo(
            status_code=status_code,
            url=url,
            headers=headers,
            content=content,
            media_type=media_type,
            timestamp=timestamp
        )

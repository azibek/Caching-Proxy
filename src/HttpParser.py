# src/http_parser.py
import httpx
from fastapi import Request
from src.HttpInfo import RequestInfo, ResponseInfo
from src.utils.http_utils import filter_headers
import datetime


class HttpParser:
    EXCLUDED_REQUEST_HEADERS = {
        "host", "connection", "keep-alive", "proxy-authenticate",
        "proxy-authorization", "te", "trailer", "transfer-encoding", "upgrade"
    }

    EXCLUDED_RESPONSE_HEADERS = {
        "content-encoding", "transfer-encoding", "connection", "keep-alive",
        "proxy-authenticate", "proxy-authorization", "te", "trailer", "upgrade", "content-length"
    }



    @staticmethod
    async def parse_request(request: Request, base_url: str) -> RequestInfo:
        clean_headers = filter_headers(dict(request.headers), HttpParser.EXCLUDED_REQUEST_HEADERS)
        params = dict(request.query_params)

        try:
            body = (await request.body()).decode('utf-8')
        except UnicodeDecodeError:
            body = None  # Or log it and set to some placeholder

        url = str(request.url)
        if 'full_path' in request.path_params:
            url += request.path_params['full_path']

        return RequestInfo(
            method=request.method,
            url=url,
            headers=clean_headers,
            params=params,
            body=body
        )

    @staticmethod
    def parse_response(response: httpx.Response) -> ResponseInfo:
        headers = filter_headers(dict(response.headers), HttpParser.EXCLUDED_RESPONSE_HEADERS)
        media_type = response.headers.get("content-type", "").split(";")[0].strip()

        return ResponseInfo(
            status_code=response.status_code,
            url=str(response.url),
            headers=headers,
            content=response.content,
            media_type=media_type,
            timestamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
        )

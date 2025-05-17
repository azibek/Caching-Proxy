from fastapi import FastAPI, Request, Response
import httpx

app = FastAPI()
upstream_url = "https://api.agify.io/"  # example upstream base URL

'''
fastapi request layer and httpx response layers modify the original request to some degree, for more general proxy server, prefer go or rust"
'''
@app.api_route("/{full_path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS", "HEAD"])
async def proxy(full_path: str, request: Request):
    # Construct the full URL to upstream
    url = upstream_url + full_path

    # Extract method, headers, query params, and body from incoming request
    method = request.method
    headers = dict(request.headers)
    params = dict(request.query_params)
    body = await request.body()

    # Remove 'host' header to avoid conflicts
    headers.pop("host", None)

    async with httpx.AsyncClient(default_encoding=False) as client:
        resp = await client.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            content=body,
            timeout=10.0
        )

    # Build a response with the same status code, headers, and content
    # Filter out hop-by-hop headers that should not be forwarded
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
    response_headers = {
        key: value for key, value in resp.headers.items()
        if key.lower() not in excluded_headers
    }

    return Response(
        content=resp.content,
        status_code=resp.status_code,
        headers=response_headers,
        media_type=resp.headers.get("content-type"),
    )

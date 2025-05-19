from fastapi import Request, Response
from HttpInfo import RequestInfo, ResponseInfo
class HttpParser:
    @staticmethod
    def parse_request(request : Request) -> RequestInfo:
        ...
    
    @staticmethod
    def parse_response(response : Response) -> ResponseInfo:
        ...
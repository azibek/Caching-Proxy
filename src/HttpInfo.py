from dataclasses import dataclass
from typing import Literal
from datetime import datetime

@dataclass
class RequestInfo:
    method : Literal["GET", "PUT", "POST", "DELETE"] # TODO: add more methods as needed
    url : str
    headers : dict
    params : dict
    # body : dict

    def to_json(self): # TODO: add conversion logic
        return {
            "method": self.method,
            "url": self.url,
            "headers": self.headers,
            "params" : self.params
            # "body": self.body
        }

@dataclass
class ResponseInfo:
    url : str
    headers : dict
    status_code : str # TODO: add proper literals for status codes
    content: dict | bytes 
    media_type : str
    timestamp : datetime
    
    def to_json(self): # TODO: add conversion logic
        return {
            "url": self.url,
            "headers": self.headers,
            "status_code": self.status_code,
            "content": self.content,
            "media_type" : self.media_type
        }
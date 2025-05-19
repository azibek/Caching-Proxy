from dataclasses import dataclass
from typing import Literal

@dataclass
class RequestInfo:
    method : Literal["GET", "PUT", "POST", "DELETE"] # TODO: add more methods as needed
    url : str
    headers : dict
    params : dict
    body : dict

    def to_json(): # TODO: add conversion logic
        ...

class ResponseInfo:
    method : Literal["GET", "PUT", "POST", "DELETE"] # TODO: add more methods as needed
    url : str
    headers : dict
    status_code : str # TODO: add proper literals for status codes
    
    def to_json(): # TODO: add conversion logic
        ...
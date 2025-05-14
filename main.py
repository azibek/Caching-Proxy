from requests import request
from typing import Literal


request_params = {
    "method": "GET",
    "url": "https://catfact.ninja/fact",
    "params": {
        "status": "active",
        "limit": 10,
        "page": 1
    },
    "json": None
}

VALID_METHODS = Literal["GET", "POST", "PUT", "OPTION"]

def fetch(method: VALID_METHODS, url: str, params: dict, json,):
    response = request(method, url, params=params, json=json)
    return response.json()

print(fetch(request_params["method"], request_params["url"],request_params["params"], request_params["json"]))
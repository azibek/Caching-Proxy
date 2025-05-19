def filter_headers(headers: dict, excluded_keys: set) -> dict:
    return {
        k.lower(): v for k, v in headers.items()
        if k.lower() not in excluded_keys
    }

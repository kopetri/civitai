CIVITAI_V1_URL = "https://civitai.com/api/v1"

def __parse_parameter__(**kwargs):
    [(key, value)] = kwargs.items()
    return "" if value is None else f"{key}={value}"

def __append_parameter__(parameters=[]):
    return "?" + "&".join([p for p in parameters if p])
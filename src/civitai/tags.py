import requests
from .utils import __append_parameter__, __parse_parameter__
from .utils import CIVITAI_V1_URL as CIVITAI_BASE_URL

class Tag():
    def __init__(self, jsondata) -> None:
        self.data = jsondata
        
    @property
    def name(self):
        return self.data["name"]
    
    @property
    def modelCount(self):
        return self.data["modelCount"]
    
    @property
    def link(self):
        return self.data["link"]

class TagResponse():
    def __init__(self, response) -> None:
        self.data = response
        self.items = [Tag(i) for i in response["items"]]
    
    @property
    def totalItems(self):
        return self.data["metadata"]["totalItems"]
    
    @property
    def currentPage(self):
        return self.data["metadata"]["currentPage"]
    
    @property
    def pageSize(self):
        return self.data["metadata"]["pageSize"]

    @property
    def totalPages(self):
        return self.data["metadata"]["totalPages"]
    
    @property
    def nextPage(self):
        return self.data["metadata"]["nextPage"]
    
    @property
    def prevPage(self):
        return self.data["metadata"]["prevPage"]
    
    
def get(limit:int=None, page:int=None, query:str=None):
    set_limit = __parse_parameter__(limit=limit)
    set_page  = __parse_parameter__(page=page)
    set_query = __parse_parameter__(query=query)
    url = f'{CIVITAI_BASE_URL}/tags{__append_parameter__([set_limit, set_page, set_query])}'
    x = requests.get(url)
    return TagResponse(x.json())
import requests
from typing import Union
from .utils import __append_parameter__, __parse_parameter__
from .utils import CIVITAI_V1_URL as CIVITAI_BASE_URL

class Image():
    def __init__(self, jsondata) -> None:
        self.data = jsondata
        
    @property
    def id(self):
        return self.data["id"]
    
    @property
    def url(self):
        return self.data["url"]
    
    @property
    def hash(self):
        return self.data["hash"]
    
    @property
    def width(self):
        return self.data["width"]
    
    @property
    def height(self):
        return self.data["height"]
    
    @property
    def nsfw(self):
        return self.data["nsfw"]
    
    @property
    def nsfwLevel(self):
        return self.data["nsfwLevel"]
    
    @property
    def createdAt(self):
        return self.data["createdAt"]
    
    @property
    def postId(self):
        return self.data["postId"]
    
    @property
    def cryCount(self):
        return self.data["stats"]["cryCount"]
    
    @property
    def laughCount(self):
        return self.data["stats"]["laughCount"]
    
    @property
    def likeCount(self):
        return self.data["stats"]["likeCount"]
    
    @property
    def dislikeCount(self):
        return self.data["stats"]["dislikeCount"]
    
    @property
    def heartCount(self):
        return self.data["stats"]["heartCount"]
    
    @property
    def commentCount(self):
        return self.data["stats"]["commentCount"]  
    
    @property
    def meta(self):
        return self.data["meta"]    
    
    @property
    def username(self):
        return self.data["username"]
    
    @property
    def prompt(self):
        if self.meta is None: return None
        return self.meta["prompt"]
    
    
class ImagesResponse():
    def __init__(self, response) -> None:
        self.data = response
        self.items = [Image(i) for i in response["items"]]
    
    @property
    def nextCursor(self):
        return self.data["metadata"]["nextCursor"]
    
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
    
    
def get(
           limit:         int=None, 
           postId :       int=None, 
           modelId :      int=None, 
           modelVersionId:int=None, 
           username:      str=None, 
           nsfw:          Union[bool,str,None]=None, 
           sort:          str=None, 
           period:        str=None, 
           page:          int=None):
    params = [
    __parse_parameter__(limit=limit),
    __parse_parameter__(postId=postId),
    __parse_parameter__(modelId=modelId),
    __parse_parameter__(modelVersionId=modelVersionId),
    __parse_parameter__(username=username),
    __parse_parameter__(nsfw=nsfw),
    __parse_parameter__(sort=sort),
    __parse_parameter__(period=period),
    __parse_parameter__(page=page),
    ]    
    url = f'{CIVITAI_BASE_URL}/images{__append_parameter__(params)}'
    x = requests.get(url)
    return ImagesResponse(x.json())
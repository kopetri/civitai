import requests
from .utils import __append_parameter__, __parse_parameter__
from .utils import CIVITAI_V1_URL as CIVITAI_BASE_URL

class ModelVersion:
    def __init__(self, data) -> None:
        self.data = data
    @property
    def id(self):
        return self.data["id"]
    @property
    def modelId(self):
        return self.data["modelId"]
    @property
    def name(self):
        return self.data["name"]
    @property
    def createdAt(self):
        return self.data["createdAt"]
    @property
    def updatedAt(self):
        return self.data["updatedAt"]
    @property
    def publishedAt(self):
        return self.data["publishedAt"]
    @property
    def trainedWords(self):
        return self.data["trainedWords"]
    @property
    def trainingStatus(self):
        return self.data["trainingStatus"]
    @property
    def trainingDetails(self):
        return self.data["trainingDetails"]
    @property
    def baseModel(self):
        return self.data["baseModel"]
    @property
    def baseModelType(self):
        return self.data["baseModelType"]
    @property
    def earlyAccessTimeFrame(self):
        return self.data["earlyAccessTimeFrame"]
    @property
    def description(self):
        return self.data["description"]
    @property
    def vaeId(self):
        return self.data["vaeId"]
    @property
    def stats(self):
        return self.data["stats"]
    @property
    def files(self):
        return self.data["files"]
    @property
    def images(self):
        return self.data["images"]
    @property
    def downloadUrl(self):
        return self.data["downloadUrl"]

class Model():
    def __init__(self, jsondata) -> None:
        self.data = jsondata
        self.modelVersions = [ModelVersion(mv) for mv in self.data["modelVersions"]]
    @property
    def id(self):
        return self.data["id"]
    
    @property
    def name(self):
        return self.data["name"]
    
    @property
    def description(self):
        return self.data["description"]
    
    @property
    def type(self):
        return self.data["type"]
    
    @property
    def nsfw(self):
        return self.data["nsfw"]
    
    @property
    def tags(self):
        return self.data["tags"]
    
    @property
    def mode(self):
        return self.data["mode"]
    
    @property
    def creator_username(self):
        return self.data["creator"]["username"]
    
    @property
    def creator_image(self):
        return self.data["creator"]["image"]
    
    @property
    def downloadCount(self):
        return self.data["stats"]["downloadCount"]
    
    @property
    def favoriteCount(self):
        return self.data["stats"]["favoriteCount"]
    
    @property
    def commentCount(self):
        return self.data["stats"]["commentCount"]
    
    @property
    def ratingCount(self):
        return self.data["stats"]["ratingCount"]
    
    @property
    def rating(self):
        return self.data["stats"]["rating"]
    
class ModelResponse():
    def __init__(self, response) -> None:
        self.data = response
        self.items = [Model(i) for i in response["items"]]
    
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
           limit:                   int=None, 
           page:                    int=None, 
           query:                   str=None, 
           tag:                     str=None, 
           username:                str=None, 
           types:                   str=None, 
           sort:                    str=None, 
           period:                  str=None, 
           rating:                  int=None,
           favorites:               bool=None,
           hidden:                  bool=None,
           primaryFileOnly:         bool=None,
           allowNoCredit:           bool=None,
           allowDerivatives:        bool=None,
           allowDifferentLicenses:  bool=None,
           allowCommercialUse:      bool=None,
           nsfw:                    bool=None,
           ):
    params = [
    __parse_parameter__(limit=limit),
    __parse_parameter__(page=page),
    __parse_parameter__(query=query),
    __parse_parameter__(tag=tag),
    __parse_parameter__(username=username),
    __parse_parameter__(types=types),
    __parse_parameter__(sort=sort),
    __parse_parameter__(period=period),
    __parse_parameter__(rating=rating),
    __parse_parameter__(favorites=favorites),
    __parse_parameter__(hidden=hidden),
    __parse_parameter__(primaryFileOnly=primaryFileOnly),
    __parse_parameter__(allowNoCredit=allowNoCredit),
    __parse_parameter__(allowDerivatives=allowDerivatives),
    __parse_parameter__(allowDifferentLicenses=allowDifferentLicenses),
    __parse_parameter__(allowCommercialUse=allowCommercialUse),
    __parse_parameter__(nsfw=nsfw),
    ]    
    url = f'{CIVITAI_BASE_URL}/models{__append_parameter__(params)}'
    x = requests.get(url)
    return ModelResponse(x.json())

def get_model(modelId: str):
    url = f"{CIVITAI_BASE_URL}/models/{modelId}"
    x = requests.get(url)
    return Model(x.json())

def get_by_modelVersion(modelVersionId: str):
    url = f"{CIVITAI_BASE_URL}/model-versions/{modelVersionId}"
    x = requests.get(url)
    return ModelVersion(x.json())

def get_by_hash(hash: str):
    url = f"{CIVITAI_BASE_URL}/model-versions/by-hash/{hash}"
    x = requests.get(url)
    return ModelVersion(x.json())

# Civitai.com API Package

This is a small wrapper of the [civitai.com API](https://github.com/civitai/civitai/wiki/REST-API-Reference)

## Install

```
pip install civitai
```

## Usage Creators

```python
from civitai import creators

result = creators.get(query="Lykon")
N = result.totalItems
creator = result.items[0]
creator.username   # Lykon
creator.modelCount # 212
```

## Usage Images

```python
from civitai import images

# https://civitai.com/posts/442123
result = images.get(postId=442123)
image = result.items[0]
image.url
image.likeCount
image.dislikeCount
```

## Usage Models

```python
from civitai import models

# https://civitai.com/models/4384/dreamshaper?modelVersionId=128713
model = models.get_model(modelId=4384)
modelVersion = models.get_by_modelVersion(modelVersionId=128713)
model.name                # DreamShaper
modelVersion.name         # 8
```

## Usage Tags

```python
from civitai import tags

result = tags.get(query="realism")
tag = result.items[0]
result.totalItems # 4
tag.modelCount    # 383
```
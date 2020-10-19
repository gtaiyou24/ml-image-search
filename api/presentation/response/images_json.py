from __future__ import annotations

from typing import List
from dataclasses import dataclass


@dataclass(init=False)
class ImagesJson:
    image_list: List[Image]

    def __init__(self, image_list: List[ImagesJson.Image]):
        assert image_list is not None, "画像リストは必須です。"

        super().__setattr__("image_list", image_list)

    def to_json(self) -> dict:
        return {'result': [{"name": image.name, "url": image.url} for image in self.image_list]}

    @dataclass(init=False)
    class Image:
        name: str
        url: str

        def __init__(self, name: str, url: str):
            assert name is not None, "画像名は必須です。"
            assert url is not None, "画像URLは必須です。"
            assert isinstance(name, str), "画像名には文字列を指定してください。"
            assert isinstance(url, str), "画像URLには文字列を指定してください。"
            super().__setattr__("name", name)
            super().__setattr__("url", url)

from __future__ import annotations

from typing import List


class SearchResultDto:

    def __init__(self, image_list: List[SearchResultDto.Image]):
        assert image_list is not None, "画像リストは必須です。"
        assert isinstance(image_list, list), "画像リストには、Listを指定している。"
        self.image_list = image_list

    class Image:

        def __init__(self, name: str, url: str):
            assert (name is not None) and (name != ""), "名前は必須です。"
            assert (url is not None) and (url != ""), "URLは必須です。"
            assert isinstance(name, str), "名前には文字列を指定してください。"
            assert isinstance(url, str), "URLには文字列を指定してください。"
            self.name = name
            self.url = url

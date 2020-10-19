from dataclasses import dataclass


@dataclass(init=False, unsafe_hash=True, frozen=True)
class ImageUrl:
    url: str

    def __init__(self, url: str):
        assert (url is not None) and (url != ""), "画像URLは必須です。"
        assert isinstance(url, str), "画像URLには文字列を指定してください。"

        super().__setattr__("url", url)
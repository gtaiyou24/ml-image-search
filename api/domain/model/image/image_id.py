from dataclasses import dataclass


@dataclass(init=True, frozen=True)
class ImageId:
    id: str

    def __init__(self, id: str):
        assert (id is not None) and (id != ""), "画像IDは必須です。"
        assert isinstance(id, str), "画像IDには文字列を指定してください。"
        super().__setattr__("id", id)

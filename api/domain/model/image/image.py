from dataclasses import dataclass

from api.domain.model.image.image_id import ImageId
from api.domain.model.image.image_url import ImageUrl


@dataclass(init=True, unsafe_hash=True, frozen=True)
class Image:
    image_id: ImageId
    image_url: ImageUrl

    def __init__(self, image_id: ImageId, image_url: ImageUrl):
        assert image_id is not None, "画像IDは必須です。"
        assert image_url is not None, "画像URLは必須です。"
        assert isinstance(image_id, ImageId), "画像IDには、ImageIdを指定してください。"
        assert isinstance(image_url, ImageUrl), "画像URLには、ImageUrlを指定してください。"
        super().__setattr__("image_id", image_id)
        super().__setattr__("image_url", image_url)

from api.domain.model.image import Image, ImageId, ImageUrl
from api.domain.repository import ImageRepository


class InMemoryImageRepository(ImageRepository):

    def get(self, image_id: ImageId) -> Image:
        return Image(ImageId(image_id.id), ImageUrl("http://example.co.jp/images/{}.jpg".format(image_id.id)))

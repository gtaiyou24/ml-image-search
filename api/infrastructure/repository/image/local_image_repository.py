from api.domain.model.image import ImageId, Image, ImageUrl
from api.domain.repository import ImageRepository


class LocalImageRepository(ImageRepository):

    def get(self, image_id: ImageId) -> Image:
        return Image(ImageId(image_id.id),
                     ImageUrl("http://localhost/cifar/{}.jpg".format(image_id.id)))

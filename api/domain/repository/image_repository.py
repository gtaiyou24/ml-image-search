import abc

from api.domain.model.image import Image
from api.domain.model.image.image_id import ImageId


class ImageRepository(abc.ABC):

    @abc.abstractmethod
    def get(self, image_id: ImageId) -> Image:
        pass

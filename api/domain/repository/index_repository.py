import abc
from typing import List

from api.domain.model.image import ImageId
from api.domain.model.vector.vector import Vector


class IndexRepository(abc.ABC):

    @abc.abstractmethod
    def search(self, vector: Vector, k: int) -> List[ImageId]:
        pass

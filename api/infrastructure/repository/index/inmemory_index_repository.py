from typing import List

from api.domain.model.image import ImageId
from api.domain.model.vector.vector import Vector
from api.domain.repository import IndexRepository


class InMemoryIndexRepository(IndexRepository):

    def search(self, vector: Vector, k: int) -> List[ImageId]:
        return [ImageId(str(i)) for i in range(1, k + 1)]

from typing import List

import faiss

from api.domain.model.image import ImageId
from api.domain.model.vector.vector import Vector
from api.domain.repository import IndexRepository


class FaissIndexRepository(IndexRepository):

    def __init__(self, faiss_index_path):
        self.index = faiss.read_index(faiss_index_path)

    def search(self, vector: Vector, k: int) -> List[ImageId]:
        distance, ids = self.index.search(vector.value, k)
        return [ImageId(str(id)) for id in ids[0]]

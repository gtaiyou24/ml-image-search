import os

import faiss

from batch.domain.model.vector import Vectors
from batch.domain.repository import IndexRepository


class FaissIndexRepository(IndexRepository):

    def __init__(self, dimension: int, index_path: str, index_name):
        self.dimension = dimension
        self.index = faiss.IndexFlatL2(dimension)
        self.index_path = os.path.join(index_path, '{}.index'.format(index_name))

    def save(self, vectors: Vectors):
        for vector in vectors.set:
            self.index.add(vector.values.reshape(1, self.dimension))
        faiss.write_index(self.index, self.index_path)

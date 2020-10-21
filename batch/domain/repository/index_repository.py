import abc

from batch.domain.model.vector import Vectors


class IndexRepository(abc.ABC):

    @abc.abstractmethod
    def save(self, vectors: Vectors):
        pass

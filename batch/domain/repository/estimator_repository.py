import abc
from batch.domain.model.estimator import Estimator


class EstimatorRepository(abc.ABC):

    @abc.abstractmethod
    def get_or_create(self, name: str, version: float) -> Estimator:
        pass

    @abc.abstractmethod
    def save(self, estimator: Estimator):
        pass

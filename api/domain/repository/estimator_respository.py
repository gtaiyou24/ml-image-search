import abc

from api.domain.model.estimator import Estimator


class EstimatorRepository(abc.ABC):

    @abc.abstractmethod
    def get(self, name: str, version: float) -> Estimator:
        pass

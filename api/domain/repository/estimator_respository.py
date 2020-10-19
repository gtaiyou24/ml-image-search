import abc

from api.domain.model.estimator import Estimator


class EstimatorRepository(abc.ABC):

    @abc.abstractmethod
    def get_latest(self) -> Estimator:
        pass

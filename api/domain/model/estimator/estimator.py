import abc

from api.domain.model.feature import Feature
from api.domain.model.vector.vector import Vector


class Estimator(abc.ABC):

    @abc.abstractmethod
    def predict(self, feature: Feature) -> Vector:
        pass

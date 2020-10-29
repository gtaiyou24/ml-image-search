from api.domain.model.estimator import Estimator
from api.domain.model.estimator.impl import RandomEstimator
from api.domain.repository import EstimatorRepository


class InMemoryEstimatorRepository(EstimatorRepository):

    def get(self, name: str, version: float) -> Estimator:
        return RandomEstimator()

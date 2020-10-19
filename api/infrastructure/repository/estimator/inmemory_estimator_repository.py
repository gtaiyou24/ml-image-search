from api.domain.model.estimator import Estimator
from api.domain.model.estimator.impl import RandomEstimator
from api.domain.repository import EstimatorRepository


class InMemoryEstimatorRepository(EstimatorRepository):

    def get_latest(self) -> Estimator:
        return RandomEstimator()

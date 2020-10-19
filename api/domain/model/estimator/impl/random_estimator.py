import numpy as np

from ..estimator import Estimator
from ...feature import Feature
from ...vector.vector import Vector


class RandomEstimator(Estimator):

    def __init__(self, p: int = 100):
        self.p = p

    def predict(self, feature: Feature) -> Vector:
        return Vector(np.random.rand(self.p).reshape((1, self.p)))

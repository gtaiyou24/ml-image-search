from __future__ import annotations

import abc
import numpy as np

from batch.domain.model.vector import Vectors


class Estimator(abc.ABC):

    def __init__(self, name: str, version: float):
        self._name = name
        self._version = version

    def name(self) -> str:
        return self._name

    def version(self) -> float:
        return self._version

    @abc.abstractmethod
    def fit(self, X, y):
        pass

    @abc.abstractmethod
    def predict(self, X) -> np.ndarray:
        pass

import os
import tensorflow as tf

from batch.domain.model.estimator import Estimator
from batch.domain.model.estimator.impl import CnnEstimator
from batch.domain.repository import EstimatorRepository


class LocalTensorflowEstimatorRepository(EstimatorRepository):

    def __init__(self, to_full_path: str):
        self.to_full_path = to_full_path

    def get_or_create(self, name: str, version: float) -> Estimator:
        file_path = self.to_full_path + '{}_{}.h5'.format(name, version)
        if os.path.isfile(file_path):
            estimator = CnnEstimator(name, version)
            estimator.model = tf.keras.models.load_model(file_path)
            return estimator
        else:
            return CnnEstimator(name, version)

    def save(self, estimator: CnnEstimator):
        estimator.save(self.to_full_path + '{}_{}.h5'.format(estimator.name(), estimator.version()))
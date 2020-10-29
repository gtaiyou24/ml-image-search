import os
import tensorflow as tf

from api.domain.model.estimator import Estimator
from api.domain.model.estimator.impl import CnnEstimator
from api.domain.repository import EstimatorRepository


class LocalTensorflowEstimatorRepository(EstimatorRepository):

    def __init__(self, dir_where_estimator_is_stored: str):
        self.dir_where_estimator_is_stored = dir_where_estimator_is_stored

    def get(self, name: str, version: float) -> Estimator:
        file_path = os.path.join(self.dir_where_estimator_is_stored, '{}_{}.h5'.format(name, version))
        estimator = CnnEstimator(name, version)
        estimator.model = tf.keras.models.load_model(file_path)
        return estimator

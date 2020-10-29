import numpy as np

from keras.models import Model

from ..estimator import Estimator
from ...feature import Feature
from ...vector.vector import Vector


class CnnEstimator(Estimator):

    def __init__(self, name: str, version: float):
        self.name = name
        self.version = version
        self.model = None
        self.hidden_layer_model = None

    def predict(self, feature: Feature) -> Vector:
        if self.hidden_layer_model is None:
            # 出力層から１つ前の中間層を出力
            self.hidden_layer_model = Model(inputs=self.model.input,
                                            outputs=self.model.get_layer('image_vector_dense').output)
        return Vector(self.hidden_layer_model.predict(self._feature_of(feature)))

    @staticmethod
    def _feature_of(feature: Feature):
        # 特徴量の正規化(0~1の値に変換する)
        X = feature.value / 255.
        return X

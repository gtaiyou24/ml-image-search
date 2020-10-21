import numpy as np

from keras.models import Model
from keras.utils import to_categorical

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, MaxPooling2D

from batch.domain.model.estimator import Estimator


class CnnEstimator(Estimator):

    def __init__(self, name: str, version: float):
        super(CnnEstimator, self).__init__(name, version)
        self.model = Sequential([
            Conv2D(32, (3, 3), strides=(1, 1), padding="valid", activation='relu', input_shape=(32, 32, 3)),
            MaxPooling2D(pool_size=(2, 2), strides=None, padding="valid"),
            Conv2D(64, (3, 3), activation='relu'),
            MaxPooling2D((2, 2)),
            Conv2D(64, (3, 3), activation='relu'),
            Flatten(),
            Dense(64, activation='relu', name="image_vector_dense"),
            Dense(10, activation='softmax')
        ])
        self.hidden_layer_model = None

    def fit(self, X, y):
        X_train, X_test = X
        Y_train, Y_test = y
        self.model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        self.model.fit(self._feature_of(X_train), self._teacher_of(Y_train),
                       epochs=5,
                       validation_data=(self._feature_of(X_test),
                                        self._teacher_of(Y_test)))
        # 出力層から１つ前の中間層を出力
        self.hidden_layer_model = Model(inputs=self.model.input, outputs=self.model.get_layer('image_vector_dense').output)

    def predict(self, X) -> np.ndarray:
        return self.hidden_layer_model.predict(self._feature_of(X))

    def _feature_of(self, X):
        # 特徴量の正規化(0~1の値に変換する)
        X = X / 255.
        return X

    def _teacher_of(self, Y):
        # 10次元の1-hotベクトルを作成
        return to_categorical(Y, 10)

    def save(self, path: str):
        self.model.save(path)

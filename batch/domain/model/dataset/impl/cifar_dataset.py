import numpy as np

from ..dataset import DataSet


class CIFARDataSet(DataSet):
    X_train: np.ndarray
    Y_train: np.ndarray
    X_test: np.ndarray
    Y_test: np.ndarray

    def __init__(self, X_train, Y_train, X_test, Y_test):
        super().__setattr__("X_train", X_train)
        super().__setattr__("Y_train", Y_train)
        super().__setattr__("X_test", X_test)
        super().__setattr__("Y_test", Y_test)

    def X(self) -> tuple:
        return (self.X_train, self.X_test)

    def Y(self) -> tuple:
        return (self.Y_train, self.Y_test)

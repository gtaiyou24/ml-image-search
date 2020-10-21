from keras.datasets import cifar10

from batch.domain.model.dataset.impl import CIFARDataSet
from batch.domain.repository import DataSetRepository


class CIFARDataSetRepository(DataSetRepository):

    def get_trainable_dataset(self) -> CIFARDataSet:
        (X_train, Y_train), (X_test, Y_test) = cifar10.load_data()
        return CIFARDataSet(X_train, Y_train, X_test, Y_test)
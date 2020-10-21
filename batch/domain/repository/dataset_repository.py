import abc

from batch.domain.model.dataset import DataSet


class DataSetRepository(abc.ABC):

    @abc.abstractmethod
    def get_trainable_dataset(self) -> DataSet:
        pass

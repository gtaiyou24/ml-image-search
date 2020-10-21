import abc

from dataclasses import dataclass


@dataclass(init=False, unsafe_hash=True, frozen=True)
class DataSet(abc.ABC):

    @abc.abstractmethod
    def X(self):
        pass

    @abc.abstractmethod
    def Y(self):
        pass

import numpy as np

from dataclasses import dataclass


@dataclass(init=False, unsafe_hash=True, frozen=True)
class Vector:
    id: str
    values: np.ndarray

    def __init__(self, id: str, values: np.ndarray):
        super().__setattr__("id", id)
        super().__setattr__("values", values)

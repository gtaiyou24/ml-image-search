from __future__ import annotations

import numpy as np

from dataclasses import dataclass


@dataclass(init=False, unsafe_hash=False, frozen=True)
class Vector:
    id: str
    values: np.ndarray

    def __init__(self, id: str, values: np.ndarray):
        super().__setattr__("id", id)
        super().__setattr__("values", values)

    def __hash__(self):
        return hash(self.id + "_" + self.values.__str__())

    def __eq__(self, other: Vector):
        assert isinstance(other, Vector), "Vector型を指定してください。"
        return self.id == other.id and self.values == other.values
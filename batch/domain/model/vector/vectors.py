from __future__ import annotations

from typing import Set

import numpy as np

from dataclasses import dataclass

from batch.domain.model.vector import Vector


@dataclass(init=False, frozen=True)
class Vectors:
    set: Set[Vector]

    def __init__(self, vectors: Set[Vector]):
        super().__setattr__("set", vectors)

    @staticmethod
    def of(vector_arr: np.ndarray) -> Vectors:
        arg_vectors = set()
        for i, arr in enumerate(vector_arr):
            arg_vectors.add(Vector(str(i), arr))
        return Vectors(arg_vectors)

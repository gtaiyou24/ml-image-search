from typing import Set

import numpy as np

from dataclasses import dataclass

from batch.domain.model.vector import Vector


@dataclass(init=False, frozen=True)
class Vectors:
    set: Set[Vector]

    def __init__(self, vectors: Set[Vector]):
        super().__setattr__("values", vectors)

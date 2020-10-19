import numpy as np

from dataclasses import dataclass


@dataclass(init=False, unsafe_hash=True, frozen=True)
class Vector:
    value: np.ndarray

    def __init__(self, value: np.ndarray):
        assert value is not None, "valueは必須です。"
        assert isinstance(value, np.ndarray), "valueにはnp.ndarrayを指定してください。"

        super().__setattr__("value", value)

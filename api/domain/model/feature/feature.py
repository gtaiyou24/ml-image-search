from dataclasses import dataclass

import numpy as np


@dataclass(init=False, frozen=True)
class Feature:
    value: np.ndarray

    def __init__(self, value: np.ndarray):
        assert value is not None, "Valueは必須です。"
        assert isinstance(value, np.ndarray), "Valueにはnp.ndarrayを指定してください。"
        super().__setattr__("value", value)

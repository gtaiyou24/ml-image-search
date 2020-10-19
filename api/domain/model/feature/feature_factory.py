import urllib
import numpy as np
import cv2

from api.domain.model.feature import Feature
from api.domain.model.image.image_url import ImageUrl


class FeatureFactory:

    def make(self, image_url: ImageUrl) -> Feature:
        image_arr = self.url_to_image(image_url.url)
        image_arr = cv2.resize(image_arr, (32, 32))
        image_arr = image_arr / 255
        # 1データの32×32の3チャネルデータにする
        image_arr = image_arr.reshape((1, 32, 32, 3))
        return Feature(image_arr)

    def url_to_image(self, url: str) -> np.ndarray:
        resp = urllib.request.urlopen(url)
        image = np.asarray(bytearray(resp.read()), dtype="uint8")
        return cv2.imdecode(image, cv2.IMREAD_COLOR)

from typing import List

from api.application.dto import SearchResultDto
from api.domain.model.feature import FeatureFactory
from api.domain.model.image import Image, ImageUrl
from api.domain.repository import EstimatorRepository, IndexRepository, ImageRepository


class SearchImageUseCase:

    def __init__(self,
                 feature_factory: FeatureFactory,
                 estimator_repository: EstimatorRepository,
                 index_repository: IndexRepository,
                 image_repository: ImageRepository):
        self.feature_factory = feature_factory
        self.estimator_repository = estimator_repository
        self.index_repository = index_repository
        self.image_repository = image_repository

    def search(self, image_url: str, k: int = 5) -> SearchResultDto:
        # 1. 画像URLからモデル入力データを生成する
        feature = self.feature_factory.make(ImageUrl(image_url))

        # 2. モデルリポジトリから最新モデルを取得する
        estimator = self.estimator_repository.get_latest()

        # 3. モデルに特徴ベクトルを入力し、画像ベクトルを出力する
        image_vector = estimator.predict(feature)

        # 5. 最近傍探索で k 個の画像IDを取得する
        image_ids = self.index_repository.search(image_vector, k)

        # 6. 画像IDをもとに画像を取得する
        image_list = [self.image_repository.get(image_id) for image_id in image_ids]

        # 7. DTO(Data Transfer Object)を生成する
        return self._make_dto(image_list)

    def _make_dto(self, image_list: List[Image]) -> SearchResultDto:
        return SearchResultDto([
            SearchResultDto.Image(image.image_id.id, image.image_url.url) for image in image_list])

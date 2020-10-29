from flask import Flask, request, jsonify

from api.application.dto import SearchResultDto
from api.application.usecase import SearchImageUseCase
from api.domain.model.feature import FeatureFactory
from api.infrastructure.repository.estimator import InMemoryEstimatorRepository, LocalTensorflowEstimatorRepository
from api.infrastructure.repository.image import InMemoryImageRepository
from api.infrastructure.repository.index import InMemoryIndexRepository, FaissIndexRepository
from api.presentation.response import ImagesJson


ESTIMATOR_NAME = 'CNNモデル'
VERSION = 1.0

ImageSearchController = Flask(__name__)

search_image_usecase = SearchImageUseCase(
    ESTIMATOR_NAME, VERSION,
    FeatureFactory(),
    LocalTensorflowEstimatorRepository('./'),
    FaissIndexRepository('./cifarインデックス.index'),
    InMemoryImageRepository()
)


@ImageSearchController.route('/image/search', methods=['POST'])
def search() -> str:
    image_url = request.json['image_url']
    k = request.json['k']
    search_result_dto = search_image_usecase.search(image_url, k)
    images_json = _make_images_json(search_result_dto)
    return jsonify(images_json.to_json())


def _make_images_json(search_result_dto: SearchResultDto) -> ImagesJson:
    image_list = []
    for image in search_result_dto.image_list:
        image_list.append(ImagesJson.Image(image.name, image.url))
    return ImagesJson(image_list)
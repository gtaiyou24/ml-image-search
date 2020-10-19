from flask import Flask, request, jsonify

from api.application.dto import SearchResultDto
from api.application.usecase import SearchImageUseCase
from api.domain.model.feature import FeatureFactory
from api.infrastructure.repository.estimator import InMemoryEstimatorRepository
from api.infrastructure.repository.image import InMemoryImageRepository
from api.infrastructure.repository.index import InMemoryIndexRepository
from api.presentation.response import ImagesJson


ImageSearchController = Flask(__name__)

search_image_usecase = SearchImageUseCase(
    FeatureFactory(),
    InMemoryEstimatorRepository(),
    InMemoryIndexRepository(),
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
from batch.domain.model.vector import Vectors
from batch.domain.repository import EstimatorRepository, DataSetRepository, IndexRepository


class MakeIndexUseCase:

    def __init__(self,
                 estimator_repository: EstimatorRepository,
                 dataset_repository: DataSetRepository,
                 index_repository: IndexRepository):
        self.estimator_repository = estimator_repository
        self.dataset_repository = dataset_repository
        self.index_repository = index_repository

    def make(self, name: str, version: float):
        """
        1. 「モデル」を取得する
        2. 「インデックス対象画像」を取得する
        3. 「モデル」に「インデックス対象画像」を入力し、「ベクトル」を出力する
        4. 「ベクトル」を「インデックス」に保存する

        :return:
        """
        estimator = self.estimator_repository.get(name, version)

        dataset = self.dataset_repository.get_trainable_dataset()

        image_vector_arr = estimator.predict(dataset.X())

        vectors = Vectors.of(image_vector_arr)

        self.index_repository.save(vectors)

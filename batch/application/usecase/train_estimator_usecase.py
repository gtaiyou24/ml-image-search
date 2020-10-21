from batch.domain.repository import EstimatorRepository, DataSetRepository


class TrainEstimatorUseCase:

    def __init__(self, estimator_repository: EstimatorRepository, dataset_repository: DataSetRepository):
        self.estimator_repository = estimator_repository
        self.dataset_repository = dataset_repository

    def train(self, name: str, version: float):
        """
        1. 指定したバージョンのモデルを取得する。なければ、モデルを新規作成する。
        2. データセットを取得する
        3. 特徴データに変換する
        4. 学習する
        5. モデルを保存する

        :return:
        """
        # 1. 指定したバージョンのモデルを取得する。なければ、モデルを新規作成する。
        estimator = self.estimator_repository.get_or_create(name, version)

        # 2. データセットを取得する
        dataset = self.dataset_repository.get_trainable_dataset()

        # 3. 学習する
        estimator.fit(dataset.X(), dataset.Y())

        # 4. モデルを保存する
        self.estimator_repository.save(estimator)

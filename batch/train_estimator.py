import argparse
import sys
import os;sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from batch.application.usecase import TrainEstimatorUseCase
from batch.infrastructure.repository.dataset import CIFARDataSetRepository
from batch.infrastructure.repository.estimator import LocalTensorflowEstimatorRepository


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("save_to", help="モデルの保存先ディレクトリを指定してください。", default="./")
    parser.add_argument("name", help="モデル名を指定してください。", default="CNNモデル")
    parser.add_argument("version", help="モデルのバージョンを指定してください。。", default=1.0, type=float)
    args = parser.parse_args()

    TrainEstimatorUseCase(LocalTensorflowEstimatorRepository(args.save_to),
                          CIFARDataSetRepository()).train(args.name, args.version)
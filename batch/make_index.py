import argparse
import sys
import os; sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from batch.application.usecase import MakeIndexUseCase
from batch.infrastructure.repository.dataset import CIFARDataSetRepository
from batch.infrastructure.repository.estimator import LocalTensorflowEstimatorRepository
from batch.infrastructure.repository.index import FaissIndexRepository


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("index_path", help="インデックスファイルのパスを指定してください。", default='./index-of-cifar.index')
    parser.add_argument("dimension", help="ベクトルの次元数を指定してください。", type=int)
    parser.add_argument("load_estimator_from", help="学習済みモデルがあるディレクトリを指定してください。", default="./")
    parser.add_argument("estimator_name", help="学習済みモデル名を指定してください。", default="CNNモデル")
    parser.add_argument("estimator_version", help="学習済みモデルのバージョンを指定してください。。", default=1.0, type=float)
    args = parser.parse_args()

    MakeIndexUseCase(
        LocalTensorflowEstimatorRepository(args.load_estimator_from),
        CIFARDataSetRepository(),
        FaissIndexRepository(args.dimension, args.index_path)
    ).make(args.estimator_name, args.estimator_version)

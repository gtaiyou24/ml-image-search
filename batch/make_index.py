import sys
import os; sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from batch.application.usecase import MakeIndexUseCase
from batch.infrastructure.repository.dataset import CIFARDataSetRepository
from batch.infrastructure.repository.estimator import LocalTensorflowEstimatorRepository
from batch.infrastructure.repository.index import FaissIndexRepository


make_index_usecase = MakeIndexUseCase(
    LocalTensorflowEstimatorRepository("../"),
    CIFARDataSetRepository(),
    FaissIndexRepository(64, "../", "faiss_cifar")
)

if __name__ == "__main__":
    make_index_usecase.make("教師あり_CNN", 1.0)

import sys
import os; sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from batch.application.usecase import TrainEstimatorUseCase
from batch.infrastructure.repository.dataset import CIFARDataSetRepository
from batch.infrastructure.repository.estimator import LocalTensorflowEstimatorRepository


train_estimator_usecase = TrainEstimatorUseCase(
    LocalTensorflowEstimatorRepository("../../"),
    CIFARDataSetRepository()
)

if __name__ == "__main__":
    train_estimator_usecase.train("教師あり_CNN", 1.0)
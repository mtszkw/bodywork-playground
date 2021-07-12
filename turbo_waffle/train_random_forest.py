from loguru import logger
import numpy as np
from sklearn.ensemble import RandomForestClassifier

import sys


def _load_preprocessed_data(X_train_full_path: str, y_train_full_path: str):
    logger.info(f"Reading training data from {X_train_full_path} and {y_train_full_path}...")
    X_train = np.load(X_train_full_path)
    y_train = np.load(y_train_full_path)
    return X_train, y_train


def train_random_forest(X_train, y_train):
    logger.info("Training Random Forest model...")
    clf = RandomForestClassifier(
        verbose=1
    )
    clf.fit(X=X_train, y=y_train)
    logger.info(f"Mean score for training set = {clf.score(X_train, y_train)}")


if __name__ == "__main__":

    if len(sys.argv) != 3:
        raise Exception("2 argument(s) required: X_train_full_path.npy y_train_full_path.npy")

    X_train_full_path = sys.argv[1]
    y_train_full_path = sys.argv[2]

    X_train, y_train = _load_preprocessed_data(X_train_full_path, y_train_full_path)
    train_random_forest(X_train, y_train)
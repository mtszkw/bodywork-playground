from loguru import logger
import numpy as np
from sklearn import datasets

import os
import sys


def _create_dir_if_doesnt_exist(directory: str):
    if not os.path.exists(directory):
        os.makedirs(directory)


def get_breast_cancer_data(
    output_dir: str = "data_files",
    data_filename: str = "breast_cancer_data",
    target_filename: str = "breast_cancer_target"):

    logger.info('Downloading data...')
    bc_data = datasets.load_breast_cancer()

    _create_dir_if_doesnt_exist(output_dir)

    data_full_path = os.path.join(output_dir, data_filename)
    logger.info(f'Saving data to {data_full_path}.npy...')
    np.save(data_full_path, bc_data.data)

    target_full_path = os.path.join(output_dir, target_filename)
    logger.info(f'Saving data to {target_full_path}.npy...')
    np.save(target_full_path, bc_data.target)

if __name__ == "__main__":

    if len(sys.argv) != 4:
        raise Exception("3 argument(s) required: output_dir data_filename target_filename")

    output_dir = sys.argv[1]
    data_filename = sys.argv[2]
    target_filename = sys.argv[3]
    get_breast_cancer_data(output_dir, data_filename, target_filename)

import numpy as np


def get_matix(data_file):
    matrix = []
    with open(data_file) as f:
        for line in f.readlines():
            matrix.append([float(i) for i in line.split(' ')])
    return np.matrix(matrix)
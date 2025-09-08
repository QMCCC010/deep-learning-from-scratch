import numpy as np


def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))

if __name__ == '__main__':
    t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
    
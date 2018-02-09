import numpy as np


def symmetrize(a):
    return a + a.T - np.diag(a.diagonal())


def check_symmetric(a, tol=1e-8):
    return np.allclose(a, a.T, atol=tol)


def random_symmetric_matrix(size=100):
    return symmetrize(np.random.uniform(-1, 1, (size, size)))


def energy(vector, matrix):
    return vector.T.dot(matrix).dot(vector)


def zero_one_to_spin(vector):
    return 2 * vector - 1


def spin_to_zero_one(vector):
    return (vector + 1) / 2

import numpy as np


def symmetrize(a):
    return a + a.T - np.diag(a.diagonal())


def check_symmetric(a, tol=1e-8):
    return np.allclose(a, a.T, atol=tol)


def test_symmetric():
    assert check_symmetric(symmetrize(np.random.rand(100, 100)))


def random_symmetric_matrix(size=100):
    return symmetrize(np.random.rand(size, size))

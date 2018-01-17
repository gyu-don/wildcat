import numpy as np

def symmetrize(a):
    return a + a.T - np.diag(a.diagonal())


def check_symmetric(a, tol=1e-8):
    return np.allclose(a, a.T, atol=tol)

def random_symmetric_matrix(size=100):
    return symmetrize(np.random.uniform(-1, 1, (size, size)))
import numpy as np


def symmetrize(a):
    return a + a.T - np.diag(a.diagonal())


def check_symmetric(a, tol=1e-8):
    return np.allclose(a, a.T, atol=tol)


def random_symmetric_matrix(size=100):
    return symmetrize(np.random.uniform(-1, 1, (size, size)))


def quadratic_form(vector, matrix):
    return vector.T.dot(matrix).dot(vector)


def zero_one_to_spin(vector):
    return 2 * vector - 1


def spin_to_zero_one(vector):
    return (vector + 1) / 2


def quadratic_energy(vector, matrix):
    product = quadratic_form(vector, matrix)
    for i in range(matrix.shape[0]):
        product += matrix[i][i] * vector[i]
    return product / 2


def hamiltonian_energy(spins, hamiltonian):
    J = hamiltonian.copy()
    for i in range(J.shape[0]):
        J[i][i] = 0
    Jsum = quadratic_form(spins, J) / 2
    hsum = 0
    for i in range(J.shape[0]):
        hsum += hamiltonian[i][i] * spins[i]
    return - (Jsum + hsum)

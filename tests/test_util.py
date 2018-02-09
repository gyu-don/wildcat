import numpy as np

from wildcat.util.matrix import check_symmetric, symmetrize, energy, zero_one_to_spin, spin_to_zero_one


def test_symmetric():
    assert check_symmetric(symmetrize(np.random.rand(100, 100)))


def test_energy():
    matrix = symmetrize(np.random.rand(100, 100));
    binary_vector = (np.random.uniform(0, 1, 100) > .5).astype(int)
    e = energy(binary_vector, matrix)
    assert(e > 0)


def test_binary_to_spin_transform():
    binary_vector = (np.random.uniform(0, 1, 100) > .5).astype(int)
    spins = zero_one_to_spin(binary_vector)
    assert ((spins == -1) | (spins == 1)).all()


def test_binary_to_spin_transform():
    spins = np.where(np.random.uniform(-1, 1, 100) > 0, 1, -1)
    binary = spin_to_zero_one(spins)
    assert ((binary == 0) | (binary == 1)).all()

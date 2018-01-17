import numpy as np

from wildcat.util.matrix import check_symmetric, symmetrize


def test_symmetric():
    assert check_symmetric(symmetrize(np.random.rand(100, 100)))


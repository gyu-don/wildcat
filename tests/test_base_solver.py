import numpy as np

from wildcat.solver.base_solver import BaseSolver
from wildcat.util.matrix import check_symmetric, random_symmetric_matrix


def test_qubo_solver_initialization():
    solver = BaseSolver()
    assert not (solver is None)


def test_qubo_solver_initialization_with_qubo():
    solver = BaseSolver()
    solver.qubo = np.ones([100, 100])
    assert np.array_equal(solver.qubo, np.ones([100, 100]))



def test_qubo_solver_ising_interactions_from_qubo_is_symmetric():
    solver = BaseSolver()
    qubo = random_symmetric_matrix()
    solver.qubo = qubo.copy()
    solver.build_ising_interactions()
    ising = solver.ising_interactions.copy()
    assert check_symmetric(ising)

def test_qubo_solver_qubo_from_ising_interactions_is_symmetric():
    solver = BaseSolver()
    ising = random_symmetric_matrix()
    solver.ising_interactions = ising.copy()
    solver.build_qubo()
    qubo = solver.qubo.copy()
    assert check_symmetric(qubo)

def test_qubo_solver_ising_qubo_ising_reconstructs_original():
    solver = BaseSolver()
    ising = random_symmetric_matrix()
    solver.ising_interactions = ising.copy()
    solver.build_qubo()
    solver.build_ising_interactions()
    reconstructed_ising = solver.ising_interactions
    print(ising - reconstructed_ising)
    assert np.allclose(ising, reconstructed_ising)



def test_qubo_solver():
    solver = BaseSolver()
    solver.qubo = np.ones([100, 100])
    solver.build_ising_interactions()
    assert solver.ising_interactions.shape == (100, 100)

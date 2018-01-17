import numpy as np

from wildcat.solver.base_solver import QuboSolver
from tests.test_util import symmetrize, check_symmetric, random_symmetric_matrix


def test_qubo_solver_initialization():
    solver = QuboSolver()


def test_qubo_solver_initialization_with_qubo():
    solver = QuboSolver()
    solver.qubo = np.ones([100, 100])
    assert np.array_equal(solver.qubo, np.ones([100, 100]))



def test_qubo_solver_ising_interactions_from_qubo_is_symmetric():
    solver = QuboSolver()
    qubo = random_symmetric_matrix()
    solver.qubo = qubo.copy()
    solver.build_ising_interactions()
    ising = solver.ising_interactions.copy()
    assert check_symmetric(ising)

def test_qubo_solver_qubo_from_ising_interactions_is_symmetric():
    solver = QuboSolver()
    ising = random_symmetric_matrix()
    solver.ising_interactions = ising.copy()
    solver.build_qubo()
    qubo = solver.qubo.copy()
    assert check_symmetric(qubo)

def test_qubo_solver_ising_qubo_ising_reconstructs_original():
    solver = QuboSolver()
    ising = random_symmetric_matrix()
    solver.ising_interactions = ising.copy()
    solver.build_qubo()
    solver.build_ising_interactions()
    reconstructed_ising = solver.ising_interactions
    print(ising - reconstructed_ising)
    assert np.allclose(ising, reconstructed_ising)



def test_qubo_solver():
    solver = QuboSolver()
    solver.qubo = np.ones([100, 100])
    solver.build_ising_interactions()
    assert solver.ising_interactions.shape == (100, 100)

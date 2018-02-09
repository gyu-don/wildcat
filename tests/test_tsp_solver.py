from wildcat.solver.tsp_solver import TSPSolver
from wildcat.util.matrix import random_symmetric_matrix


def test_initialize_tsp_solver():
    assert not TSPSolver() is None

def test_initialize_tsp_solver_with_distance_builds_hamiltonian():
    solver = TSPSolver(distance=random_symmetric_matrix())
    assert not (solver.ising_interactions is None)

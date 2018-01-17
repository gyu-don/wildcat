from wildcat.solver.ising_hamiltonian_solver import IsingHamiltonianSolver
from wildcat.solver.qubo_solver import QuboSolver
from wildcat.util.matrix import random_symmetric_matrix


def test_ising_hamiltonian_solver():
    Jij = random_symmetric_matrix()
    solver = IsingHamiltonianSolver(ising_interactions=Jij)
    assert not (solver is None)
    assert solver.qubo.shape[0] == Jij.shape[0]

def test_ising_qubo_solver():
    assert not (QuboSolver() is None)
import numpy as np

from wildcat.solver.ising_hamiltonian_solver import IsingHamiltonianSolver
from wildcat.solver.qubo_solver import QuboSolver
from wildcat.util.matrix import random_symmetric_matrix


def test_ising_hamiltonian_solver():
    Jij = random_symmetric_matrix()
    solver = IsingHamiltonianSolver(ising_interactions=Jij)
    assert not (solver is None)
    assert solver.qubo.shape[0] == Jij.shape[0]


def test_qubo_solver():
    qubo = random_symmetric_matrix()
    solver = QuboSolver(qubo=qubo)
    assert not (solver is None)
    assert solver.ising_interactions.shape[0] == qubo.shape[0]


def test_qubo_solver_response_is_binary():
    solver = QuboSolver(qubo=random_symmetric_matrix())

    def callback(result):
        assert not (result is None)
        assert (result >= 0).all() and (result <= 1).all()

    future = solver.solve(callback)
    assert (future.result().status_code == 200)


def test_hamiltonian_solver_response_is_spin():
    solver = QuboSolver(qubo=random_symmetric_matrix())

    def callback(result):
        assert not (result is None)
        assert  ((result == 1) | (result == 0)).all()

    future = solver.solve(callback)
    assert (future.result().status_code == 200)
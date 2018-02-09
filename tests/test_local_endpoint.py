import json
import unittest

import numpy as np

from wildcat.network.local_endpoint import LocalEndpoint
from wildcat.solver.ising_hamiltonian_solver import IsingHamiltonianSolver
from wildcat.solver.qubo_solver import QuboSolver
from wildcat.util.matrix import random_symmetric_matrix, spin_to_zero_one


class TestCase(unittest.TestCase):

    def test_endpoint_initialize(self):
        endpoint = LocalEndpoint()

    def test_dispatch_to_endpoint_without_data_raises(self):
        endpoint = LocalEndpoint()
        solver = QuboSolver()
        self.assertRaises(ValueError, endpoint.dispatch, solver)

    def test_dispatch_success(self):
        endpoint = LocalEndpoint()
        solver = QuboSolver()
        solver.ising_interactions = random_symmetric_matrix()
        endpoint.dispatch(solver)

    def test_solver_solve_success(self):
        solver = QuboSolver()
        solver.ising_interactions = random_symmetric_matrix()
        callback = lambda result: None
        solver.build_qubo()
        solver.solve(callback)

    def test_solver_solve_callback_called(self):
        solver = QuboSolver(qubo=random_symmetric_matrix())

        def callback(result):
            print(result)
            assert not (result is None)
            assert len(result) == solver.qubo.shape[0]


        def iterative_callback(q):
            print(solver.qubo_energy(spin_to_zero_one(q)))
            pass

        future = solver.solve(callback, endpoint=LocalEndpoint(iterative_callback=iterative_callback))
        # future = solver.solve(callback,endpoint=Endpoint(host="http://localhost:3001"))
        response = future.result()

    def test_can_calculate_hamiltonian_energy(self):
        solver = IsingHamiltonianSolver(ising_interactions=random_symmetric_matrix())

        def callback(result):
            e = solver.hamiltonian_energy(result)
            print(e)
            # assert (e > 0)

        future = solver.solve(callback)
        response = future.result()

    def test_can_calculate_qubo_energy(self):
        solver = QuboSolver(qubo=random_symmetric_matrix())

        def callback(result):
            e = solver.qubo_energy(result)
            print(e)
            # assert (e > 0)

        future = solver.solve(callback)
        response = future.result()

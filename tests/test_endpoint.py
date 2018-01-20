import json
import unittest

import numpy as np

from wildcat.network.endpoint import Endpoint
from wildcat.solver.qubo_solver import QuboSolver
from wildcat.util.matrix import random_symmetric_matrix


class TestCase(unittest.TestCase):

    def test_endpoint_initialize(self):
        endpoint = Endpoint()

    def test_dispatch_to_endpoint_without_data_raises(self):
        endpoint = Endpoint()
        solver = QuboSolver()
        self.assertRaises(ValueError, endpoint.dispatch, solver)

    def test_dispatch_success(self):
        endpoint = Endpoint()
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
        solver = QuboSolver(qubo=random_symmetric_matrix(size=1000))
        def callback(result):
            assert not (result is None)
            assert len(result) == solver.qubo.shape[0]

        future = solver.solve(callback)
        # future = solver.solve(callback,endpoint=Endpoint(host="http://localhost:3001"))
        response = future.result()
        self.assertEqual(response.status_code, 200)

    def test_solver_params(self):
        solver = QuboSolver()
        solver.ising_interactions = random_symmetric_matrix()
        j = json.dumps(solver.endpoint._build_matrix_for_params(solver.ising_interactions))
        self.assertIsNotNone(j)
        array = np.array(json.loads(j))
        self.assertTrue(np.allclose(solver.ising_interactions, array))

    def test_solver_strip_params(self):
        solver = QuboSolver()
        solver.ising_interactions = random_symmetric_matrix()
        j = json.dumps(solver.endpoint._build_matrix_for_params(solver.ising_interactions, strip=True))
        self.assertIsNotNone(j)
        list = json.loads(j)
        for i in range(solver.ising_interactions.shape[0]):
            for j in range(len(list[i])):
                self.assertAlmostEqual(list[i][j], solver.ising_interactions[i][i + j])

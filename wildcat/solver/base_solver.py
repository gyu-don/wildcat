import numpy as np

from wildcat.network.endpoint import Endpoint


class BaseSolver:
    def __init__(self):
        self.ising_interactions = np.zeros(0)
        self.qubo = np.zeros(0)
        self.endpoint = Endpoint()

    def solve(self, callback, endpoint=None):
        self.endpoint = endpoint or self.endpoint
        return self.endpoint.dispatch(solver=self, path=Endpoint.ising_solver_path(), callback=callback)

    def build_qubo(self):
        self.qubo = -self.ising_interactions.copy() * 4
        for i in range(self.qubo.shape[0]):
            self.qubo[i][i] = 2 * (self.ising_interactions[i].sum() + self.ising_interactions.sum(axis=0)[i]) - 6 * \
                              self.ising_interactions[i][i]

    def build_ising_interactions(self):
        self.ising_interactions = -self.qubo.copy() / 4.0
        for i in range(self.ising_interactions.shape[0]):
            self.ising_interactions[i][i] = - (self.qubo[i].sum() + self.qubo.sum(axis=0)[i]) / 4.0


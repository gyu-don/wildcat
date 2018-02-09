import numpy as np

from wildcat.network.endpoint import Endpoint
from wildcat.util.matrix import quadratic_energy, hamiltonian_energy


class BaseSolver:
    def __init__(self):
        self.ising_interactions = np.zeros(0)
        self.qubo = np.zeros(0)
        self.endpoint = Endpoint()

    def solve(self, callback, endpoint=None):
        if self.ising_interactions.shape[0] == 0:
            self.qubo()
        if self.qubo.shape[0] == 0:
            self.build_ising_interactions()

        self.endpoint = endpoint or self.endpoint
        return self.endpoint.dispatch(solver=self, callback=callback)

    def build_qubo(self):
        self.qubo = -self.ising_interactions.copy() * 4
        for i in range(self.qubo.shape[0]):
            self.qubo[i][i] = 2 * (self.ising_interactions[i].sum() + self.ising_interactions.sum(axis=0)[i]) - 6 * \
                              self.ising_interactions[i][i]

    def build_ising_interactions(self):
        self.ising_interactions = -self.qubo.copy() / 4.0
        for i in range(self.ising_interactions.shape[0]):
            self.ising_interactions[i][i] = - (self.qubo[i].sum() + self.qubo.sum(axis=0)[i]) / 4.0

    def adjust_solutions_from_ising_spins(self, solutions):
        return solutions

    def hamiltonian_energy(self, spins):
        return hamiltonian_energy(spins, self.ising_interactions)

    def qubo_energy(self, vector):
        return quadratic_energy(vector, self.qubo)

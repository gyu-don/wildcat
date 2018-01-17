from wildcat.solver.base_solver import BaseSolver


class TSPSolver(BaseSolver):

    def __init__(self, distance=None):
        super().__init__()
        self.distance = distance
        if not (self.distance is None):
            self._build_ising_hamiltonian()

    def _build_ising_hamiltonian(self):
        pass

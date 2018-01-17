from wildcat.solver.base_solver import BaseSolver


class IsingHamiltonianSolver(BaseSolver):
    def __init__(self, ising_interactions=None):
        super().__init__()
        if not (ising_interactions is None):
            self.ising_interactions = ising_interactions
        self.build_qubo()

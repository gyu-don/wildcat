from wildcat.solver.base_solver import BaseSolver


class QuboSolver(BaseSolver):
    def __init__(self, qubo=None):
        super().__init__()
        if not (qubo is None):
            self.qubo = qubo
        self.build_ising_interactions()

    def adjust_solutions_from_ising_spins(self, solutions):
        return (solutions + 1) / 2

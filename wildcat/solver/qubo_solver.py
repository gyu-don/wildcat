from wildcat.solver.base_solver import BaseSolver
from wildcat.util.matrix import spin_to_zero_one


class QuboSolver(BaseSolver):
    def __init__(self, qubo=None):
        super().__init__()
        if not (qubo is None):
            self.qubo = qubo
        self.build_ising_interactions()

    def adjust_solutions_from_ising_spins(self, solutions):
        return spin_to_zero_one(solutions)

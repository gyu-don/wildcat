from concurrent.futures import ThreadPoolExecutor

from wildcat.annealer.simulated.simulated_annealer import SimulatedAnnealer


class LocalEndpoint:
    def __init__(self, annealer=SimulatedAnnealer()):
        self.annealer = annealer
        pass

    def anneal(self, solver, callback):
        self.annealer.anneal(solver.ising_interactions)
        q = solver.adjust_solutions_from_ising_spins(self.annealer.q)
        if not (callback is None):
            callback(q)
        return q

    def dispatch(self, solver, callback=None):
        if solver.ising_interactions.shape[0] == 0:
            raise ValueError('No valid qubo nor ising interactions in the solver.')

        with ThreadPoolExecutor(max_workers=1) as executor:
            return executor.submit(self.anneal, solver, callback)

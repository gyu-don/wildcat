import numpy as np

from wildcat.annealer.base_annealer import BaseAnnealer
from wildcat.annealer.simulated.single_spin_flip_strategy import SingleSpinFlipStrategy
from wildcat.annealer.simulated.temperature_schedule import TemperatureSchedule
from wildcat.util.matrix import symmetrize


class SimulatedAnnealer(BaseAnnealer):
    def __init__(self, schedule=None, strategy=SingleSpinFlipStrategy()):
        super().__init__()
        self.temperature_schedule = schedule or TemperatureSchedule()
        self.q = np.zeros(0)
        self.strategy = strategy
        self.dim = None
        self.J = None
        self.h = None

    def anneal(self, hamiltonian):
        self.initialize_annealing(hamiltonian)
        for T in self.temperature_schedule:
            self.strategy.update(self, T)
        return self.q

    def initialize_annealing(self, hamiltonian):
        self.dim = hamiltonian.shape[0]
        self.J = symmetrize(hamiltonian).copy()
        self.h = np.zeros(self.dim)
        for i in range(self.dim):
            self.h[i] = hamiltonian[i][i]
            self.J[i][i] = 0
        self.q = np.where(np.random.uniform(-1, 1, self.dim) > 0, 1, -1)

import numpy as np

from wildcat.annealer.simulated.base_simulated_annealing_strategy import BaseSimulatedAnnealingStrategy


class SingleSpinFlipStrategy(BaseSimulatedAnnealingStrategy):

    def __init__(self, repetition=2000, update_callback=None):
        super().__init__()
        self.repetition = repetition
        self.update_callback = update_callback
        pass

    def update(self, annealer, T):
        for _ in range(self.repetition):
            k = int(np.random.uniform(0, annealer.dim))
            dE = 2 * (annealer.h[k] + annealer.J[k].dot(annealer.q)) * annealer.q[k]
            if dE < 0 or np.exp(- dE / T) > np.random.uniform(0, 1):
                annealer.q[k] *= -1
                if not (self.update_callback is None):
                   self.update_callback(annealer.q)

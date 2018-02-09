import numpy as np


class SingleSpinFlipStrategy:

    def __init__(self, repetition=2000):
        self.repetition = repetition
        pass

    def update(self, annealer, T):
        for _ in range(self.repetition):
            k = int(np.random.uniform(0, annealer.dim))
            dE = 2 * (annealer.h[k] + annealer.J[k].dot(annealer.q)) * annealer.q[k]
            if dE < 0 or np.exp(- dE / T) > np.random.uniform(0, 1):
                annealer.q[k] *= -1
                if not (annealer.callback is None):
                   annealer.callback(annealer.q)

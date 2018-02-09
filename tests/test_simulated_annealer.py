from wildcat.annealer.simulated.simulated_annealer import SimulatedAnnealer
from wildcat.annealer.simulated.single_spin_flip_strategy import SingleSpinFlipStrategy
from wildcat.util.matrix import random_symmetric_matrix, hamiltonian_energy


def test_initialize_simulated_annealer():
    annealer = SimulatedAnnealer()
    assert not (annealer is None)
    assert not (annealer.temperature_schedule is None)


def test_simulated_annealer_annealing():
    annealer = SimulatedAnnealer(strategy=SingleSpinFlipStrategy(repetition=1))
    hamiltonian = random_symmetric_matrix(1000)
    annealer.callback = lambda q: print(hamiltonian_energy(q, hamiltonian))
    annealer.anneal(hamiltonian)
    assert annealer.q.shape[0] == hamiltonian.shape[0]

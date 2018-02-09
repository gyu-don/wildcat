class LocalEndpoint(object):
    pass[![Build Status](https://travis-ci.org/skonb/wildcat_qdk.svg?branch=feature%2Ftravis_ci)](https://travis-ci.org/skonb/wildcat_qdk)

Wildcat Python SDK
===============================

version number: 0.0.7
author: Shumpei Kobayashi

Overview
--------

Wildcat Python SDK to Use Annealers

Installation / Usage
--------------------

To install use pip:

    $ pip install wildcat


Or clone the repo:

    $ git clone https://github.com/mdrft/wildcat_qdk.git
    $ python setup.py install
    
Contributing
------------

TBD

Example
-------

To find an optimal arrangement with wildcat remote server:
```python
from wildcat.util.matrix import random_symmetric_matrix
from wildcat.solver.ising_hamiltonian_solver import IsingHamiltonianSolver

     
Jij = random_symmetric_matrix(size=40)
solver = IsingHamiltonianSolver(ising_interactions=Jij)

def callback(arrangement):
    e = solver.hamiltonian_energy(arrangement)
    print("Energy: ", e)
    print("Spins: ", arrangement)

solver.solve(callback)
```



To find an optimal arrangement with local annealer, specify LocalEndpoint:
```python
from wildcat.network.local_endpoint import LocalEndpoint
     
solver.solve(callback, endpoint=LocalEndpoint())
```

You can adjust annealing strategy:
```python
from wildcat.network.local_endpoint import LocalEndpoint
from wildcat.annealer.simulated.simulated_annealer import SimulatedAnnealer
from wildcat.annealer.simulated.single_spin_flip_strategy import SingleSpinFlipStrategy
from wildcat.annealer.simulated.temperature_schedule import TemperatureSchedule
from wildcat.util.matrix import hamiltonian_energy

def update_callback(q):
    print(q)
    print(hamiltonian_energy(q))
    
schedule = TemperatureSchedule(initial_temperature=10, last_temperature=0.1, scale=0.8)
strategy = SingleSpinFlipStrategy(repetition=10, update_callback=update_callback)
annealer = SimulatedAnnealer(schedule=schedule, strategy=strategy)
local_endpoint = LocalEndpoint(annealer=annealer)

```
QNN Python SDK
===============================

version number: 0.0.1
author: Shumpei Kobayashi

Overview
--------

Wildcat Python SDK to Use Annealers

Installation / Usage
--------------------

To install use pip:

    $ pip install wildcat_qdk


Or clone the repo:

    $ git clone https://github.com/mdrft/wildcat_qdk.git
    $ python setup.py install
    
Contributing
------------

TBD

Example
-------

To find an optimal arrangement:
```python
from wildcat.util.matrix import random_symmetric_matrix
     
Jij = random_symmetric_matrix()
solver = IsingHamiltonianSolver(ising_interactions=Jij)

def callback(arrangement):
    print(arrangement)

solver.solve(callback)
```




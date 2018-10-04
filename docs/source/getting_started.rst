Getting Started
===============

Prerequisites
-------------

- Python3
- numpy
- `blueqat <https://github.com/mdrft/Blueqat>`_ (if you want to use Universal Gate Model.)

Install
-------

.. code-block:: bash

    $ pip3 install wildqat

or 

.. code-block:: bash

    $ git clone https://github.com/mdrft/Wildqat.git
    $ python setup.py install

Ising Model
-----------

Example
^^^^^^^

.. code-block:: python

    import wildqat as wq
    a = wq.opt()
    a.qubo = [[4,-4,-4],[0,4,-4],[0,0,4]]
    a.sa() #=> [1, 1, 1]
    print(a.E[-1]) #=>[0.0]

Parameters
^^^^^^^^^^

Some parameters for simualtion is adjustable

.. code-block:: python

    #for sa
    a.Ts  = 10    #default 5
    a.R   = 0.99  #default 0.95
    a.ite = 10000 #default 1000

    #for sqa
    a.Gs  = 100   #default 10


Energy Function
^^^^^^^^^^^^^^^

Energy function of the calculation is stored in attribute E as an array.

.. code-block:: python
    
    print(a.E[-1]) #=>[0.0]

    #if you want to check the time evolution
    a.plot()


Universal Gate Model
--------------------

Example
^^^^^^^

It is convertible to the universal gate model pauli operator for qaoa simulations

.. code-block:: python

    wq.pauli(wq.sel(2,1))
    # => -0.5*I + 0.5*Z[0]*Z[1]
    
With blueqat, you can easily simulate combinatorial optimization problem on Universal Gate Model link:Blueqat

.. code-block:: python

    import wildqat as wq
    from blueqat import vqe

    qubo = wq.pauli(wq.sel(4,1))
    step = 4
    result = vqe.Vqe(vqe.QaoaAnsatz(qubo,step)).run()
    print(result.most_common(5))

    # => (((0, 0, 1, 0), 0.24650337773427797), ((1, 0, 0, 0), 0.24650337773427794), ((0, 0, 0, 1), 0.24650337773427788), ((0, 1, 0, 0), 0.24650337773427783), ((0, 0, 0, 0), 0.0034271782738342416))


.. _intro:

Introducing Wildcat
===================
Wildcat is a Python SDK to develop apps for solving Ising problems. It is installable on your PC so that you can quickly start solving them.
Currently, the SDK includes local Simulated Annealing solver, but you can connect our server to use solvers/resources out there.


What is Ising model
-------------------

Real Quantum Annealing(QA) machines are built upon physical model called Ising model, which can be computationally
simulated on our PCs with algorithms called Simulated Annealing(SA) or Simulated Quantum Annealing(SQA).
1-dimensional Ising model is a 1D array of quantum bits (qubits), each of them has a ‘spin’ of +1(up) or -1(down).
2-dimensional Ising model is similar, it consists of a plainer lattice and has more adjacent qubits than 1D.
Although the complex physics may be overwhelming to you, Wildcat let you easily calculate the model without knowing much about them.



Combinatorial Optimization problem and Simulated Annealing
----------------------------------------------------------

Simulated Annealing(SA) can be used to solve combinatorial optimization problems of some forms, and Ising model is one of them.
Metropolis sampling based Monte-Carlo methods are used in such procedures.


Hamiltonian
-----------

To solve Ising model with SA, we have to set Jij/hi which describes how strong a pair of qubits are coupled, and how strong a qubit is biased, respectively.



Simulated Annealing and Simulated Quantum Annealing
---------------------------------------------------

We also have algorithm called Simulated Quantum Annealing(SQA) to solve Ising problems, in which quantum effects are taken into account.
The effect of quantum superposition is approximated by the parallel execution of different world-line,
by which we can effectively simulate wilder quantum nature. Technically, path-integral
methods based on Suzuki-Trotter matrix decomposition are used in the algorithm.



QUBO
----

Ising model problems are represented by Quadratic Unconstrained Optimization (QUBO) problems.
Although variables in combinatorial optimization problems are of {0, 1}, quantum spins above are represented by {-1, 1},
so we have to transform their representation. Wildcat can automatically handle them, so you do not have to know about {-1, 1} things.



Checking and Verifying solutions
--------------------------------

We can calculate how good (or bad) a solution is by calculating ‘Energy’ of the solution, which can be done by a Wildcat one-liner.
Repeatedly solving Ising model, comparing that energy may let you know which is the best, or better answer to the problem.
If the problem is of NP, then checking whether the constraints are fulfilled can also be calculated in polynomial time.
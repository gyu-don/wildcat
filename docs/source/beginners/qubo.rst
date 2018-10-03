What's QUBO
===========

QUBO is used to model and solve numerous categories of optimization problems.

Let's learn more about QUBO here.

Now there are three boxes labeled :math:`x_{0}, x_{1}, x_{2}` and we think the problem to choose some boxes from them.

First, we define the box's value = 1 when the box is chosen, and value = 0 otherwise. 
For example when you choose :math:`x_{0}`, box's values are :math:`x_{0} = 1, x_{1} = 0, x_{2} = 0`.
This can be represented as computer friendly array format [1, 0, 0].

Next, we define the problem we want to solve "choose two from three boxes."
We must think of a function E(x) for the problem, which takes minimum value when the problem is solved.
We use the following function:

.. math::
   E(x) = (x_{0} + x_{1} + x_{2} - 2) ^ 2

Let's check the results:

- If you choose :math:`x_{0}` alone, :math:`E(x) = (1 + 0 + 0 - 2) ^ 2 = (-1) ^ 2 = 1`
- If you choose :math:`x_{0}` and :math:`x_{1}`, :math:`E(x) = (1 + 1 + 0 - 2) ^ 2 = (0) ^ 2 = 0`
- If you choose all, :math:`E(x) = (1 + 1 + 1 - 2) ^ 2 = (1) ^ 2 = 1`

The minimum value of E(x) is 0 when you choose two of three, so you can confirm the E(x) above is the appropriate function for solving this problem.
Let's expand this E(x) as the following:

.. math::

   E(x) &= (x_{0} + x_{1} + x_{2} - 2) ^ 2 \\
        &= (x_{0} + x_{1} + x_{2} - 2) (x_{0} + x_{1} + x_{2} - 2) \\
        &= x_{0} ^ 2 + x_{1} ^ 2 + x_{2} ^ 2 + 2 x_{0} x_{1} + 2 x_{0} x_{2} + 2 x_{1} x_{2} - 4 x_{0} - 4 x_{1} - 4 x_{2} + 4

Remember that :math:`x` takes 0 or 1.
So we can use the equation :math:`x = x ^ 2 = x x`. Apply it to E(x).

.. math::

   E(x) &= x_{0} ^ 2 + x_{1} ^ 2 + x_{2} ^ 2 + 2 x_{0} x_{1} + 2 x_{0} x_{2} + 2 x_{1} x_{2} - 4 x_{0} - 4 x_{1} - 4 x_{2} + 4 \\
        &= x_{0} ^ 2 + x_{1} ^ 2 + x_{2} ^ 2 + 2 x_{0} x_{1} + 2 x_{0} x_{2} + 2 x_{1} x_{2} - 4 x_{0} x_{0} - 4 x_{1} x_{1} - 4 x_{2} x_{2} + 4 \\
        &= -3 x_{0} x_{0} −3 x_{1} x_{1} -3 x_{2} x_{2} + 2 x_{0} x_{1} + 2 x_{0} x_{2} + 2 x_{1} x_{2} + 4
     
Next, we want to convert function E(x) to a matrix which shapes like the following.

.. csv-table::
   :header: , :math:`x_{0}`, :math:`x_{1}`, :math:`x_{2}`
   :widths: 3, 2, 2, 2

   :math:`x_{0}`, , ,
   :math:`x_{1}`, , ,
   :math:`x_{2}`, , ,

The first term of the last line of E(x) above multiplys :math:`x_{0}` and :math:`x_{0}`, then multiplys the product and -3. 
So put -3 in the intersection cell of :math:`x_{0}` and :math:`x_{0}` like this:

.. csv-table::
   :header: , :math:`x_{0}`, :math:`x_{1}`, :math:`x_{2}`
   :widths: 3, 2, 2, 2

   :math:`x_{0}`, -3, ,
   :math:`x_{1}`, , ,
   :math:`x_{2}`, , ,

For the second and third term, put -3 in the intersection cell of :math:`x_{1}` and :math:`x_{1}`, :math:`x_{2}` and :math:`x_{2}`.

.. csv-table::
   :header: , :math:`x_{0}`, :math:`x_{1}`, :math:`x_{2}`
   :widths: 3, 2, 2, 2

   :math:`x_{0}`, -3, ,
   :math:`x_{1}`, ,-3,
   :math:`x_{2}`, , , -3

The next term multiplys :math:`x_{0}` and :math:`x_{1}`, then multiplys the product and 2. 
So put 2 in the intersection cell of :math:`x_{0}` and :math:`x_{1}`.

.. csv-table::
   :header: , :math:`x_{0}`, :math:`x_{1}`, :math:`x_{2}`
   :widths: 3, 2, 2, 2

   :math:`x_{0}`, -3, 2,
   :math:`x_{1}`, ,-3,
   :math:`x_{2}`, , , -3

For the next two terms, put 2 in the intersection cell of :math:`x_{0}` and :math:`x_{2}`, :math:`x_{1}` and :math:`x_{2}`.
And we can ignore the last term 4, because it is not affect to find the minimum value of E(x) with the combination of :math:`x_{i}`.

As a result of the steps above, the matrix is finally the following shape. This is the QUBO to solve "choose two from three boxes."

.. csv-table::
   :header: , :math:`x_{0}`, :math:`x_{1}`, :math:`x_{2}`
   :widths: 3, 2, 2, 2

   :math:`x_{0}`, -3, 2, 2
   :math:`x_{1}`, ,-3, 2
   :math:`x_{2}`, , , -3

Use Simulated Annealing of Wildqat to solve this problem:

.. code-block:: python

    import wildqat as wq
    a = wq.opt()
    a.qubo = [[-3,2,2], [0,-3,2], [0,0,-3]]
    answer = a.sa() 
    print(answer)

Run the program and you will get the result [1, 1, 0]. This means :math:`x_{0}, x_{1}` are chosen. 
You will find the problem is solved correctly.


Recap The Procedure
-------------------
Steps to solve the QUBO problem is:

1. Define E(x) that takes minimum value when the problem is solved.

2. Convert E(x) to QUBO matrix.

3. Supply the QUBO matrix to Wildqat and solve the problem with Simulated Annealing (SA).

The most difficult step is 1., but you can find many useful examples in our :doc:`../tutorial`.


Further Understanding QUBO
--------------------------

Define the row number of QUBO matrix as :math:`i` and the column number as :math:`j`, and each cell value as :math:`Q_{ij}`.
So the E(x) can be represented as:

.. math::

   E(x) = \sum_{i} \sum_{j} Q_{ij} x_{i} x_{j}

Actually this :math:`Q_{ij}` is QUBO. You can find the last equation calculating E(x) above shapes this form. 

See also `Wikipedia <https://en.wikipedia.org/wiki/Quadratic_unconstrained_binary_optimization>`_.






Wildqat Python SDK
--------
Python Framework for Ising Model

Install
--------------------

```
$ pip3 install wildqat
```

or

```
$ git clone https://github.com/mdrft/Wildqat.git
$ python setup.py install
```

Example
-------

```python
import wildqat as wq
a = wq.anneal()
a.J = wq.q2i([[4,-4,-4],[0,4,-4],[0,0,4]]) #QUBO matrix and converted to Jij matrix
a.sa() #=> array([1, 1, 1])
```

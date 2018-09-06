Wildqat Python SDK
--------
Python Framework for Ising Model

Install
--------------------

    $ git clone https://github.com/mdrft/wildcat.git
    $ python setup.py install

Example
-------

```python
import wildqat as wq
a = wq.anneal()
a.J = [[0,-1,-1],[0,0,-1],[0,0,0]]
a.sa()
```

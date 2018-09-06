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
a.J = wq.q2i([[4,-4,-4],[0,4,-4],[0,0,4]])
a.sa() #=> array([1, 1, 1])
```

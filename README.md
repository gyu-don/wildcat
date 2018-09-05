Wildqat Python SDK
===============================

Overview
--------

Python Framework for Ising Model

Installation / Usage
--------------------

clone the repo:

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

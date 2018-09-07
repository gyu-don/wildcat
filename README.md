Wildqat Python SDK
--------
Python Framework for QUBO 

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
a = wq.opt()
a.qubo = [[4,-4,-4],[0,4,-4],[0,0,4]]
a.sa() #=> [1, 1, 1]
```

Tutorial
----------

日本語
https://github.com/mdrft/Wildqat/tree/master/examples



Wildqat Python SDK
--------
Python Framework for QUBO 

Version
--------
0.4.4

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
print(a.E[-1]) #=>[0.0]
```

Functions
-------
sel(N,K)  
Automatically create QUBO which select K qubits from N qubits
```python
print(wq.sel(5,2))
#=>
[[-3  2  2  2  2]
 [ 0 -3  2  2  2]
 [ 0  0 -3  2  2]
 [ 0  0  0 -3  2]
 [ 0  0  0  0 -3]]
```


Tutorial
----------

日本語  
https://github.com/mdrft/Wildqat/tree/master/examples_ja

Authors
----------
<a href="https://github.com/minatoyuichiro">Yuichiro Minato</a>(MDR), <a href="https://github.com/Morning777">Asa Eagle</a>(MDR), [Satoshi Takezawa](https://github.com/takebozu)(TerraSky), [Seiya Sugo](https://github.com/seiya-sugo)(TerraSky)

Disclaimer
----------
Copyright 2018 The Wildqat Developers.


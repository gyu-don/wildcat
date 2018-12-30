![wildqat](MDR_Wildqat.png)

Wildqat Python SDK
--------
Python Framework for QUBO 

Version
--------
1.1.5

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
from wildqat import *
a = opt()
a.qubo = [[4,-4,-4],[0,4,-4],[0,0,4]]
a.run() #=> [1, 1, 1]
print(a.E[-1]) #=>[0.0]
```

Parameters
-------
Some parameters for simualtion is adjustable
```python
#for sa
a.Ts  = 10    #default 5
a.R   = 0.99  #default 0.95
a.ite = 10000 #default 1000
```

Energy Function
-------
Energy function of the calculation is stored in attribute E as an array.
```python

print(a.E[-1]) #=>[0.0]

#if you want to check the time evolution
a.plot()
```

Sampling
-------
Sampling and counter function with number of shots.
```python

result = a.run(shots=100,sampler="fast")

print(result)

[[0, 1, 0],
 [0, 0, 1],
 [0, 1, 0],
 [0, 0, 1],
 [0, 1, 0],
 ...
 
 counter(result) # => Counter({'001': 37, '010': 25, '100': 38})

```

Universal Gate Model Operator
-------
With blueqat, you can easily simulate combinatorial optimization problem on Universal Gate Model
link:<a href="https://github.com/mdrft/Blueqat">Blueqat</a>
```python
from wildqat import *
from blueqat import vqe

qubo = pauli(sel(4,1)) # =>  0.5*Z[0]*Z[1] + 1.0*I - Z[2] - Z[0] + 0.5*Z[0]*Z[2] - Z[3] + 0.5*Z[0]*Z[3] - Z[1] + 0.5*Z[1]*Z[2] + 0.5*Z[1]*Z[3] + 0.5*Z[2]*Z[3]
step = 4
result = vqe.Vqe(vqe.QaoaAnsatz(qubo,step)).run()
print(result.most_common(5))

# => (((0, 0, 1, 0), 0.24650337773427797), ((1, 0, 0, 0), 0.24650337773427794), ((0, 0, 0, 1), 0.24650337773427788), ((0, 1, 0, 0), 0.24650337773427783), ((0, 0, 0, 0), 0.0034271782738342416))
```

Connection to D-Wave cloud
-------
Direct connection to D-Wave machine with apitoken  
https://github.com/dwavesystems/dwave-cloud-client is required
```python
from wildqat import *
a = opt()
a.dwavetoken = "YOUR TOKEN HERE"
a.qubo = [[0,0,0,0,-4],[0,2,0,0,-4],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,4]] 
a.dw()

# => [1,1,-1,1,1,0,0,0,0,0,0]
```



Functions
-------

sel(N,K,array)  
Automatically create QUBO which select K qubits from N qubits
```python
print(sel(5,2))
#=>
[[-3  2  2  2  2]
 [ 0 -3  2  2  2]
 [ 0  0 -3  2  2]
 [ 0  0  0 -3  2]
 [ 0  0  0  0 -3]]
```

if you set array on the 3rd params, the result likely to choose the nth qubit in the array
```python
print(sel(5,2,[0,2]))
#=>
[[-3.5  2.   2.   2.   2. ]
 [ 0.  -3.   2.   2.   2. ]
 [ 0.   0.  -3.5  2.   2. ]
 [ 0.   0.   0.  -3.   2. ]
 [ 0.   0.   0.   0.  -3. ]]
```

net(arr,N)  
Automatically create QUBO which has value 1 for all connectivity defined by array of edges and graph size N
```python
print(net([[0,1],[1,2]],4))
#=>
[[0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
```
this create 4*4 QUBO and put value 1 on connection between 0th and 1st qubit, 1st and 2nd qubit  

zeros(N)
Create QUBO with all element value as 0  
```python
print(zeros(3))
#=>
[[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]
```

diag(list)
Create QUBO with diag from list  
```python
print(diag([1,2,1]))
#=>
[[1 0 0]
 [0 2 0]
 [0 0 1]]
```

Document
----------
English  
https://wildqat.readthedocs.io/en/latest/

日本語  
https://wildqat.readthedocs.io/ja/latest/

Tutorial
----------
English  
https://github.com/mdrft/Wildqat/tree/master/examples_en  

日本語  
https://github.com/mdrft/Wildqat/tree/master/examples_ja

Authors
----------
[Yuichiro Minato](https://github.com/minatoyuichiro)(MDR), [Asa Eagle](https://github.com/Morning777)(MDR), [Satoshi Takezawa](https://github.com/takebozu)(TerraSky), [Seiya Sugo](https://github.com/seiya-sugo)(TerraSky)

Disclaimer
----------
Copyright 2018 The Wildqat Developers.


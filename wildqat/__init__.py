import numpy as np
import time
  
def reJ(j2):
	j2 = np.triu(j2) + np.triu(j2, k=1).T
	return j2

def Ei(q3,j3):
	EE = 0
	for i in range(len(q3)):
		EE += q3[i]*j3[i][i]
		EE += sum(q3[i]*q3[i+1:]*j3[i][i+1:])
	return EE

def q2i(j4):
	nn = len(j4)
	for i in range(nn):
		for j in range(i+1,nn):
			j4[i][j] *= 0.25

	j4 = np.triu(j4)+np.triu(j4,k=1).T

	for i in range(nn):
		sum = 0
		for j in range(nn):
			if i == j:
				sum += j4[i][i]*0.5
			else:
				sum += j4[i][j]
		j4[i][i] = sum

	return np.triu(j4)

class anneal:
	def __init__(self):
		self.Ts = 5
		self.Tf = 0.02

		self.Gs = 10
		self.Gf = 0.02
		self.tro = 8

		self.R = 0.95
		self.ite = 1000
		self.qubo = [[4,-4,-4],[0,4,-4],[0,0,4]]
		self.J = [[0,-1,-1],[0,0,-1],[0,0,0]]

	def sa(self):
		start = time.time()
		T = self.Ts
		J = reJ(self.J)
		N = len(J)
		q = np.random.choice([-1,1],N)
		while T>self.Tf:
			x_list = np.random.randint(0, N, self.ite)
			for x in x_list:
				q2 = np.ones(N)*q[x]
				q2[x] = 1
				dE = -2*sum(q*q2*J[:,x])

				if dE < 0 or np.exp(-dE/T) > np.random.random_sample():
					q[x] *= -1
			T *= self.R
		print(time.time() - start)
		return q

	def sqa(self):
		G = self.Gs
		J = reJ(self.J)
		N = len(J)
		q = [np.random.choice([-1,1],N) for j in range(self.tro)]
		for i in range(self.tro):
			q[i] = np.random.choice([-1,1],N)
		while G>self.Gf:
			for i in range(self.ite*self.tro):
				x = np.random.randint(N)
				y = np.random.randint(self.tro)
				dE = 0

				for j in range(N):
					if j == x:
						dE += -2*q[y][x]*J[x][x]
					else:
						dE += -2*q[y][j]*q[y][x]*J[j][x]

				dE += q[y][x]*(q[(self.tro+y-1)%self.tro][x]+q[(y+1)%self.tro][x])*np.log(1/np.tanh(G/self.Tf/self.tro))/self.Tf;

				if dE < 0 or np.exp(-dE/self.Tf) > np.random.random_sample():
					q[y][x] *= -1
			G *= self.R
		return q

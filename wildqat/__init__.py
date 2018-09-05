import numpy as np
  
def reJ(jj):
	jj = np.triu(jj) + np.triu(jj, k=1).T
	return jj

def Ei(qq,jj):
	EE = 0
	for i in range(len(qq)):
		EE += qq[i]*jj[i][i]
		EE += sum(qq[i]*qq[i+1:]*jj[i][i+1:])
	return EE

class anneal:
	def __init__(self):
		self.Ts = 5
		self.Tf = 0.02
		self.R = 0.95
		self.ite = 1000
		self.J = [[0,-1,-1,-1],[0,0,-1,-1],[0,0,0,-1],[0,0,0,0]]

	def sa(self):
		T = self.Ts
		J = reJ(self.J)
		N = len(J)
		q = np.random.choice([-1,1],N)
		while T>self.Tf:
			for i in range(self.ite):
				x = np.random.randint(N)
				dE = 0

				for j in range(N):
					if j == x:
						dE += -2*q[x]*J[x][x]
					else:
						dE += -2*q[j]*q[x]*J[j][x]

				if dE < 0 or np.exp(-dE/T) > np.random.random_sample():
					q[x] *= -1
			T *= self.R
		return q

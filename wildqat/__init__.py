import numpy as np
import time
  
#def Ei(q3,j3):
#	EE = 0
#	for i in range(len(q3)):
#		EE += q3[i]*j3[i][i]
#		EE += sum(q3[i]*q3[i+1:]*j3[i][i+1:])
#	return EE+self.ep

class anneal:
	def __init__(self):
		self.Ts = 5
		self.Tf = 0.02

		self.Gs = 10
		self.Gf = 0.02
		self.tro = 8

		self.R = 0.95
		self.ite = 1000
		self.qubo = []
		self.J = []

		self.ep = 0

	def reJ(self):
        	return np.triu(self.J) + np.triu(self.J, k=1).T
		

	def qi(self):
		nn = len(self.qubo)
		self.J = [np.random.choice([1.,1.],nn) for j in range(nn)]
		for i in range(nn):
			for j in range(i+1,nn):
				self.J[i][j] = self.qubo[i][j]/4

		self.J = np.triu(self.J)+np.triu(self.J,k=1).T

		for i in range(nn):
			sum = 0
			for j in range(nn):
				if i == j:
					sum += self.qubo[i][i]*0.5
				else:
					sum += self.J[i][j]
			self.J[i][i] = sum

		self.ep = 0

		for i in range(nn):
			self.ep += self.J[i][i]
			for j in range(i+1,nn):
				self.ep -= self.J[i][j]

		self.J = np.triu(self.J)

	def sa(self):
		start = time.time()
		T = self.Ts
		if self.qubo != []:
			self.qi()
		J = self.reJ()
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
		qq = [int((i+1)/2) for i in q]
		return qq

	def sqa(self):
		G = self.Gs
		if self.qubo != []:
			self.qi()
		J = self.reJ()
		N = len(J)
		q = [np.random.choice([-1,1],N) for j in range(self.tro)]
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

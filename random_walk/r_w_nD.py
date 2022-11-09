import random
import matplotlib.pyplot as plt

n = 4
N = 7
x =[0] * n
for i in range (n):
	x[i] = [0] * N
	
for j in range (n):
	for i in range(N-1):
		dice = random.random()
		if dice > 0.5:
			x[j][i+1] = x[j][i]+1
		else:
			x[j][i+1] = x[j][i]-1
print(x)
#m = plt.subplot(1,1,1,projection = "3d")
#m.plot(x[0], x[1], x[2])
#plt.show()

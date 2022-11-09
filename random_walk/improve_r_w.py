import random
import matplotlib.pyplot as plt

N = 10000
x = [0] * N
y = [0] * N

for i in range(N-1):
    dice = random.random()
    if dice > 0.5:
    	z = x
    	w = y
    else:
       	z = y
       	w = x
    dice = random.random()
    if dice > 0.5:
       	z[i+1] = z[i]+1
       	w[i+1] = w[i]
    else:
       	z[i+1] = z[i]-1
       	w[i+1] = w[i]
plt.plot(y,x)
plt.show()

import random
import matplotlib.pyplot as plt

class RW:
	def __init__(self,n,N):
		#The number of steps
		self.steps = N+1
		#The number of dimensions
		self.dimensions = n
		#The coordinate system
		self.rw = self.init_coordinates()
				
	#Initialize the coordinate system	
	def init_coordinates(self):
		rw =[0]*self.dimensions
		for i in range (self.dimensions):
			rw[i] = [0]*self.steps
		return rw
		
	#The main function that perform the random-walk
	def fill_coordinates(self):
		for i in range (self.steps-1):
			dimchange = random.randint(0, self.dimensions-1)
			for j in range(self.dimensions):
				if j != dimchange:
					self.dont_move(j,i)
				else:
					self.choose_direction(j,i)
		return self.rw
	
	
	#The two function of steps
	def dont_move(self,j,i):
		self.rw[j][i+1] = self.rw[j][i]
		return
	
	def choose_direction(self, j, i):
		dice = random.random()
		if dice > 0.5:
			self.rw[j][i+1] = self.rw[j][i]+1
		else:
			self.rw[j][i+1] = self.rw[j][i]-1
			
	
	#Displaying steps according to the number dimensions selected
	def display(self):
		if self.dimensions == 1:
			plt.plot(list(range (self.steps)), self.rw[0])
			plt.show()
		elif self.dimensions == 2:
			plt.plot(self.rw[0],self.rw[1])
			plt.show()
		elif self.dimensions == 3:
			m = plt.subplot(111,projection = "3d")
			m.plot(self.rw[0], self.rw[1], self.rw[2])
			plt.show()
		elif self.dimensions>3:	
			for i in range(self.steps):
				print("step" , str(i+1).zfill(3), end = " is: ")
				res = []
				for j in range(self.dimensions):
					res.append(str(self.rw[j][i]).zfill(2))
				res = '[' + ', '.join(res) + ']'
				print(res)		

#The main function				
def main():
	dim = int(input("Enter number of dimensions: "))
	steps = int(input("Enter number of steps: "))
	if dim < 1:
		return
	random_walk = RW(dim, steps)
	random_walk.fill_coordinates()
	random_walk.display()
	
if __name__ == "__main__":
    main()
    
    

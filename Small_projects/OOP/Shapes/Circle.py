class Circle:

	def __init__(self, radius):
		self.radius = radius
		
	def area(self):
		return 3.14 * self.radius **2
	
	def circumference(self):
		return 2 * 3.14 * self.radius
	

class Rectangle:
	
	def __init__(self, height, width):
		self.height = height
		self.width = width
	
	
	def area(self):
		return self.height * self.width
	
	def circumference(self):
		return self.height * 2 + self.width * 2
	
class square(Rectangle):
	
	def __init__(self, width):
		Rectangle.__init__(self, width, width)

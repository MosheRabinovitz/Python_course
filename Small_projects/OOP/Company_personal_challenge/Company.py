class Company:

	def __init__(self, dictionary = {}):
		self.company = dictionary
		
	def __repr__(self):
		return f'{self.company}'
	
	def adding(self, dictionary):
		self.company.update(dictionary)
	
	def remove(self, string):
		self.company.pop(string, None)
	
	def update(self, dictionary):
		for key in dictionary:
			self.company[key] = dictionary[key] #self.company.get(key, None) + dictionary[key]
		



import random

class CEO:
	
	def __init__(self, name, employees = {}):
		self.name = name
	
	def __repr__(self):
		return self.name
	

	def adding(self, dictionary, Company):
		if name == 'CEO':
			Company.adding(dictionary)
		elif random.randint(0,2) == 1:
			Company.adding(dictionary)
			print(f'CEO confirmed, the addition is complete')
		else:
			print(f'the operation has not been added, premission denied')
		

	
	def remove(program, Company, name = 'CEO'):
		if name == 'CEO':
			Company.remove(program)
		elif random.randint(0,2) == 1:
			Company.remove(program)
			print(f'CEO confirmed, the removal is complete')
		else:
			print(f'the operation has not been removed, premission denied')
	
	
	def edit(dictionary, Company, name = 'CEO'):
		if name == 'CEO':
			Company.update(dictionary)
		elif random.randint(0,2) == 1:
			Company.update(dictionary)
			print(f'CEO confirmed, the editing is complete')
		else:
			print(f'the operation for edition not complete, premission denied')
	


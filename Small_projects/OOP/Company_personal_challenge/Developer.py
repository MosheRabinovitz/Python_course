from CEO import CEO
from Company import Company
from TeamLeader import TeamLeader

class Developer:

	def __init__(self, name, team_leader):
		TeamLeader.__init__(self, name)
		self.team_leader = team_leader
		self.team_leader.add_team_member(name)
		

	 
	def adding(self, program, Company):
		self.team_leader.adding(program, Company, self.name)
	
	def remove(self, program, company):
		if company.company[program] == self.name: # or self.team_leader.get_premissions(string, company) == 1:
			company.remove(program)
		else:
			self.team_leader.remove(program, company, self.name)
			
			
	def edit(self, program, company):
		if company.company[program] == self.name:
			self.team_leader.adding(program, Company, self.name)
		else:	
			self.team_leader.edit(program, company)

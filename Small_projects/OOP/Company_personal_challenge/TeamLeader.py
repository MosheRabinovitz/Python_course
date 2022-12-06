import random
from CEO import CEO
from Company import Company


class TeamLeader:
	
	def __init__(self, name, team_members = []):
		CEO.__init__(self, name)
		self.team_members = team_members
		self.team_members.append(self.name)
	
	
	def adding(self, program, company, member_name = 'TeamLeader'):
		if member_name =='TeamLeader':
			member_name = self.name
		dictionary = {program : member_name}
		
		if member_name in self.team_members:	
			company.adding(dictionary)
		else:
			CEO.adding(dictionary, company, member_name)
	
	
	def remove(self, program, company, member_name = 'TeamLeader'):
		if member_name =='TeamLeader':
			member_name = self.name
			
		if company.company[program] in self.team_members:
			company.remove(program)
		else:
			CEO.remove(program, company, member_name)
				
	def edit(self, program, company, member_name = 'TeamLeader'):
		if member_name =='TeamLeader':
			member_name = self.name
		dictionary = {program : member_name}
	
		if company.company[program] in self.team_members:
			company.update(dictionary)
		else:
			CEO.edit(dictionary, company, member_name)
	
	
	def add_team_member(self, team_member):
		self.team_members.append(team_member)
	
		
	def remove_team_member(self,team_member):
		self.team_members.remove(team_member)
	

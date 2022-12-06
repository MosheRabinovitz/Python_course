class Clip:

	def __init__(self, name, year):
		self.name = name
		self.year = year
		self.is_played = False
		
	def __repr__(self):
		return f'{self.name}:{self.year}'
	
	
	def play(self):
		self.is_played = True
	
	def stop(self):
		self.is_played = False

class ArtClip(Clip):

	def __init__(self, name, year, time):
		Clip.__init__(self, name, year)
		self.time = time
	
	def __repr__(self):
		return f'{Clip.__repr__(self)} ({self.time})'
	
	def is_valid_for_euro(self):
		return self.time <= 3

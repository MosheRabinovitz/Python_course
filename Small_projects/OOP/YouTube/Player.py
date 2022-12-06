import random
from Clip import Clip
from ArtClip import ArtClip

class Player:
	
	def __init__(self, clips):
		self.clips = clips
		self.current = -1
		for clip in clips:
			clip.stop()
	
	def __next__(self):
		if not self.clips:
			raise ValueError
		if self.current != -1:
			self.clips[self.current].stop()
		if self.current < len(self.clips) -1:
			self.current += 1 
		else:
			self.current = 0
		self.clips[self.current].play()
	
	
	def shuffle(self):
		clips_random = []
		while len(clips_random) < len(self.clips):
			i = random.randint(0, len(self.clips)-1)
			if not self.clips[i] in clips_random:
				clips_random.append(self.clips[i])
		self.clips = clips_random

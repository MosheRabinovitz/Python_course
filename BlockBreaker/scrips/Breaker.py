import pygame, settings

class Breaker(pygame.sprite.Sprite):
	
	
	def __init__(self):
		super(Breaker, self).__init__()
		# Initialize the form of the spaceship
		#self.image = pygame.image.load(settings.packmen)
		self.image = pygame.Surface((settings.width_size_breaker, settings.hieght_size_breaker))
		self.image.fill(settings.breaker_color)
		self.location = {'midbottom' : (settings.SCREEN_WIDTH/2, settings.SCREEN_HEIGHT-5)}
		self.rect = self.image.get_rect(**self.location)
		
		
	
	# Update the movement acording to the pressed keys of the player
	def update(self, pressed_keys):
		if pressed_keys[pygame.K_LEFT]:
			self.rect.move_ip(-settings.breaker_speed, 0)
		if pressed_keys[pygame.K_RIGHT]:
			self.rect.move_ip(settings.breaker_speed, 0)

		# Determine the limit movement to screen size
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.right > settings.SCREEN_WIDTH:
			self.rect.right = settings.SCREEN_WIDTH
	
	def reposition(self):
		self.rect = self.image.get_rect(**self.location)

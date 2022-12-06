import pygame, settings, random

class Ball(pygame.sprite.Sprite):
	
	def __init__(self	):
		super(Ball, self).__init__()
		self.speed_direction = -settings.ball_speed_direction
		self.hieght_direction = -settings.ball_speed_direction
		#self.image = pygame.draw.circle(settings.screen, settings.ball_color, self.pos, settings.ball_radius)
		self.image = pygame.Surface(settings.ball_radius)
		self.image.fill(settings.ball_color)
		self.rect = self.image.get_rect(center=(settings.ball_center))
		#self.image.fill(settings.color_block)
		#self.rect = self.image.get_rect(center=(coordinates))
	
	def update(self, blocks, breaker, score):
		list_of_blocks_collidets = pygame.sprite.spritecollide(self, blocks, True)
		list_of_breaker_collidets = pygame.sprite.spritecollide(self, breaker, False)
		if list_of_blocks_collidets or list_of_breaker_collidets:
			self.hieght_direction = -self.hieght_direction
			score += settings.score * len(list_of_blocks_collidets)
		if self.rect.left <= 0 or self.rect.right >= settings.SCREEN_WIDTH:
			self.speed_direction = -self.speed_direction
		if self.rect.top <= 0:
			self.hieght_direction = -self.hieght_direction
		if self.rect.bottom >= settings.SCREEN_HEIGHT:
			return True, score
		self.rect.move_ip(self.speed_direction, self.hieght_direction)
		return False, score
	
	def reposition(self):
		self.rect = self.image.get_rect(center=(settings.ball_center))

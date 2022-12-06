import pygame, random, settings

# Class of all Blocks
class Blocks(pygame.sprite.Sprite):
	
	def __init__(self):
		super(Blocks, self).__init__()
		# Get/set the speed of the axis
		self.speed = settings.blocks_speed_movement
		self.hieght_direction = 0
		# Creation the invaders in diffrent locations and colors
		self.__blocks = []

		for i in range(10, settings.SCREEN_HEIGHT//2, 20):
			for j in range(30, settings.SCREEN_WIDTH-10, 55):
				new_block = Block((j, i), random.choice(settings.block_color))
				self.__blocks.append(new_block)
	
	# Update the movement of the invaders
	def update(self):
		change_height = False
		# Checing if need to change direction in the axis
		for block in self.__blocks:
			if block.rect.left <= 0 or block.rect.right >= settings.SCREEN_WIDTH:
				self.speed = -self.speed
				self.hieght_direction = settings.blocks_hieght_direction
				change_height = True
				break
				
		if not change_height:
			self.hieght_direction = 0
		
		# Call to function of the movement of each invader
		for block in self.__blocks:
			block.update(self.speed, self.hieght_direction)
	
	# Adding each invader to the groups 
	def add_groups(self, blocks, all_sprites):
		for block in self.__blocks:
			all_sprites.add(block)
			blocks.add(block)

	
	# Kill the invader after collision
	def kill_in_collide(self, list_of_collidets):
		for block in list_of_collidets:
			self.__blocks.remove(block)
			block.kill()

	def out_of_screen(self):
		for block in self.__blocks:
			if block.rect.bottom >= settings.SCREEN_HEIGHT:
				return True
		return False



class Block(pygame.sprite.Sprite):
	
	def __init__(self, coordinates, color):
		super(Block, self).__init__()
		self.image = pygame.Surface((settings.width_size_block, settings.hieght_size_block))
		self.image.fill(color)
		self.rect = self.image.get_rect(center=(coordinates))
	
	
	# Update the movement of the invader
	def update(self, speed, hieght_direction):
		self.rect.move_ip(speed, hieght_direction)
		
			
			
			
			

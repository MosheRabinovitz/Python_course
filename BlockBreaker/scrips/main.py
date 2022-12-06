import pygame, Tools, settings

def main():
	
	'''
	pygame.init()
	clock = pygame.time.Clock()
	pygame.display.set_caption('Block Breaker')
	'''
	clock, LIVES, score, start_ticks = Tools.initilaize()
	
	'''
	breakers = pygame.sprite.Group()
	blocks = pygame.sprite.Group()
	all_sprites = pygame.sprite.Group()
	
	all_blocks = Blocks()
	breaker = Breaker()
	ball = Ball()
	all_sprites.add(breaker)
	all_sprites.add(ball)
	breakers.add(breaker)
	
	all_blocks.add_groups(blocks, all_sprites)
	'''
	
	breakers, blocks, ball, breaker, all_blocks, all_sprites = Tools.initilaize_objects_and_groups()
	
	'''
	screen = settings.screen
	all_sprites.draw(screen)
	pygame.display.update()
	'''
	
	Tools.start_the_game(all_sprites)
	
	running = True
	while running:
		
		'''
		for event in pygame.event.get():
		# Check if the player close the game
			if event.type == pygame.QUIT:
				running = False
		'''
		
		running = Tools.chack_events(running)
		
		loss, score = Tools.update(breakers, blocks, breaker, ball, score)
		if loss:
			LIVES, running = Tools.loss(LIVES, breaker, ball, running)
			
			if running:
				Tools.start_the_game(all_sprites)
		'''	
		screen.fill((0,0,0))
		ball.update(blocks, breakers)
		#all_blocks.update()
		pressed_keys = pygame.key.get_pressed()
		breaker.update(pressed_keys)
		if pressed_keys[pygame.K_ESCAPE]:
			running = False
		
		all_sprites.draw(screen)
		
		pygame.display.update()
		'''
		Tools.display(all_sprites, LIVES, score, start_ticks)
		
		clock.tick(30)


if __name__ == '__main__':
	main()

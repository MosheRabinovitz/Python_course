from Blocks import Blocks
from Breaker import Breaker
from Ball import Ball
import pygame, settings

def initilaize():
	pygame.init()
	clock = pygame.time.Clock()
	pygame.display.set_caption('Block Breaker')
	LIVES = settings.LIVES
	score = 0
	start_ticks = pygame.time.get_ticks()
	return clock, LIVES, score, start_ticks


def initilaize_objects_and_groups():
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
	
	return breakers, blocks, ball, breaker, all_blocks, all_sprites


def start_the_game(all_sprites):
	all_sprites.draw(settings.screen)
	pygame.display.update()
	massage('To start press space', pygame.K_SPACE)
	

def chack_events(running):		
	for event in pygame.event.get():
	# Check if the player close the game
		if event.type == pygame.QUIT:
			running = False
		if pygame.key.get_pressed()[pygame.K_ESCAPE]:
			running = False
	return running

	
def update(breakers, blocks, breaker, ball, score):
	loss, score =  ball.update(blocks, breakers, score)
	pressed_keys = pygame.key.get_pressed()
	breaker.update(pressed_keys)
	return loss, score


def loss(LIVES, breaker, ball, running):
	LIVES -=1
	running = game_status(LIVES, running)
	if running:
		massage('Let\'s try agisn', pygame.K_KP_ENTER)
	breaker.reposition()
	ball.reposition()
	settings.screen.fill((0,0,0))
	return LIVES, running

	
def game_status(LIVES, running):
	if LIVES <= 0:
		massage('Game Over', pygame.K_KP_ENTER)
		running = False
	return running
	

def display(all_sprites, LIVES, score, start_ticks):
	messages_group = []
	settings.screen.fill((0,0,0))
	all_sprites.draw(settings.screen)
	
	seconds = (pygame.time.get_ticks() - start_ticks)//1000
	show_in_game(f'Time of the game: {seconds}', (20, 20), settings.dinamic_massage_font, settings.dinamic_massage_size, messages_group)
	show_in_game(f'Lives: {LIVES}', (20, 55), settings.dinamic_massage_font, settings.dinamic_massage_size, messages_group)
	show_in_game(f'Score: {score}', (20, 90), settings.dinamic_massage_font, settings.dinamic_massage_size, messages_group)
	
	[settings.screen.blit(surf[0], surf[1]) for surf in messages_group]
	
	pygame.display.update()
	

def massage(massage, key_press):
	pressed_keys = pygame.key.get_pressed() 
	while not pressed_keys[key_press]:
		for event in pygame.event.get():
			pressed_keys = pygame.key.get_pressed() 
			font = pygame.font.Font(settings.screen_massage_font, settings.screen_massage_size)
			text = font.render(massage, True, (0, 200, 0))
			textRect = text.get_rect()
			textRect.center = (settings.SCREEN_WIDTH // 2, settings.SCREEN_HEIGHT // 2)
			settings.screen.blit(text, textRect)
			pygame.display.flip()


# Dinamic massage on the screeen 
def show_in_game(massege, location, font, size, messages_group):
	font = pygame.font.Font(font, size)
	text = font.render(massege, True, (0, 220, 0))
	textRect = text.get_rect(topleft = location)
	messages_group.append((text, textRect))

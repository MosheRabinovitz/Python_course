import pygame, random

# Size of the screen
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

# Quantity of the lives
LIVES = 3
score = 10

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

blocks_hieght_direction = 10
blocks_speed_movement = 1
block_color = [(0,0,255), (255,0,255), (0,255,0), (0,255,255)]
width_size_block = 50
hieght_size_block = 15


width_size_breaker = 100
hieght_size_breaker = 15
breaker_color = (255,0,255)
breaker_speed = 10

ball_color = (0,255,0)
ball_center = [SCREEN_WIDTH/2, SCREEN_HEIGHT-30]
ball_radius = (15,15)
ball_speed_direction = 5

# Set massages settings
screen_massage_font = '../fonts/games/Games-Italic.ttf'
dinamic_massage_font = '../fonts/game_over/game_over.ttf'
score_massage_font = '../fonts/gameplay/Gameplay.ttf'
screen_massage_size = 80
dinamic_massage_size = 100
score_massage_size = 30

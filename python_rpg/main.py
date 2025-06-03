import pygame
import sys
import config
from engine.player import Player

pygame.init()
screen = pygame.display.set_mode((config.screen_width, config.screen_height))
pygame.display.set_caption("2D RPG")
clock = pygame.time.Clock()

player = Player(100,100)

running = True
while running:
    dt = clock.tick(config.FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    keys = pygame.key.get_pressed()
    player.handle_keys(keys)
    
    screen.fill((config.white))
    player.draw(screen)
    
    pygame.display.flip()
    
pygame.quit()
sys.exit()


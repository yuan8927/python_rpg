import pygame
import sys
import config
from engine.player import Player
import map


pygame.init()
map.load_tiles()
screen = pygame.display.set_mode((config.screen_width, config.screen_height))
pygame.display.set_caption("2D RPG")
clock = pygame.time.Clock()

player = Player(100,100)

running = True
while running:
    screen.fill((config.white))
    dt = clock.tick(config.FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    keys = pygame.key.get_pressed()
    player.handle_keys(keys)
    map.draw_map(screen)
    player.draw(screen)
    
    pygame.display.flip()
    
pygame.quit()
sys.exit()


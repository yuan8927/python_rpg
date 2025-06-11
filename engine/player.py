import pygame
import config

class Player:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/characters/hero.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = config.player_speed
     
    def handle_keys(self,keys):
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed
        
    def draw(self, surface):
        surface.blit(self.image, self.rect)
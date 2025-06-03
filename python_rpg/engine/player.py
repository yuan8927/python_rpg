import pygame
import config

class Player:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/characters/hero.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = config.plyer_speed
     
    def handle_keys(self,keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        
    def draw(self, surface):
        surface.blit(self.image, self.rect)
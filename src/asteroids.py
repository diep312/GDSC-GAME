import pygame.sprite
from random import randint
from settings import Settings


class Asteroid(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        self.type = type

        if self.type == 1:
            astroid_surface = pygame.image.load('assets/obstacles/asteroid.png').convert_alpha()
        else:
            astroid_surface = pygame.image.load('assets/obstacles/asteroid_3.png').convert_alpha()

        self.image = astroid_surface
        self.rect = self.image.get_rect(midbottom=(randint(35, Settings.SCREEN_WIDTH - 35), 0))

    def update(self):
        if(self.type == 1):
            self.rect.y += Settings.DEFAULT_ASTROID_SPEED
        else:
            self.rect.y += Settings.DEFAULT_ASTROID_SPEED*2

        if self.rect.top >= Settings.SCREEN_HEIGHT:
            self.kill()
import pygame.sprite
import pygame
from settings import Settings
from src.util import Utilities

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_idle = pygame.image.load('assets/player/idle.png').convert_alpha()
        player_left = pygame.image.load('assets/player/left.png').convert_alpha()
        player_right = pygame.image.load('assets/player/right.png').convert_alpha()
        self.state_index = 1
        self.player_state = [player_left, player_idle, player_right]

        self.image = self.player_state[self.state_index]
        self.rect = self.image.get_rect(midbottom =(Settings.SCREEN_WIDTH*0.5, Settings.SCREEN_HEIGHT*0.75))
        self.dir = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.dir = -Settings.MOVEMENT_SPEED
        if keys[pygame.K_d]:
            self.dir = Settings.MOVEMENT_SPEED


    def apply_direction(self):
        self.rect.x += self.dir
        if self.rect.right >= Settings.SCREEN_WIDTH: self.rect.right = Settings.SCREEN_WIDTH
        if self.rect.left <= 0: self.rect.left = 0

    def update(self):
        self.rect.y = Utilities.sine(100.0, 1280, 20.0, Settings.SCREEN_HEIGHT*0.75)
        self.player_input()
        self.apply_direction()
        self.animationState()

    def animationState(self):
        if self.dir == 0:
            self.state_index = 1
            self.image = self.player_state[self.state_index]
        elif self.dir < 0:
            if self.state_index >= 0:
                self.state_index -= 0.3
            self.image = self.player_state[int(self.state_index)]
        else:
            if self.state_index <= 2:
                self.state_index += 0.3
            self.image = self.player_state[int(self.state_index)]


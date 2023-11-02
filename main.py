import pygame
from sys import exit
from random import choice
from src.player import Player
from src.asteroids import Asteroid
from settings import Settings
import time

pygame.init()

# GLOBAL VARIABLES
isGameRunning = True
isPlayerLost = False
start_time = 0

# DISPLAY AND ASSET INFO
bg_music = pygame.mixer.Sound('assets/sound/bg.mp3')
bg_music.set_volume(0.5)
hit_sound = pygame.mixer.Sound('assets/sound/hit.mp3')

custom_font_48 = pygame.font.Font("assets/fonts/VCR_OSD_MONO_1.001.ttf", 48)
custom_font_24 = pygame.font.Font("assets/fonts/VCR_OSD_MONO_1.001.ttf", 24)
display_surface = pygame.display.set_mode((Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT))
pygame.display.set_caption("Dashtroid")
clock = pygame.time.Clock()

#--------SURFACES------------
#BACKGROUND
bg_surface = pygame.image.load('assets/background/bg.jpg').convert()
font_surface = custom_font_48.render("My game", False, 'White').convert_alpha()
gameover_text = custom_font_48.render("GAME OVER!", False, 'White').convert_alpha()
tryagain_text = custom_font_24.render("Press any key to try again!", False, 'White').convert_alpha()


#PLAYERS SPRITE
player = pygame.sprite.GroupSingle()
player.add(Player())

#ASTEROIDS SPRITE
obstacle_group = pygame.sprite.Group()

#SPAWN TIMER
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 900)
ostacle_rect_list = []

#DISPLAY SCORES
def displayScore():
    cur_time = int((pygame.time.get_ticks() - start_time) / 1000)
    score_surface = custom_font_48.render(f'Time: {cur_time}s', False, "White")
    score_rect = score_surface.get_rect(topright=(Settings.SCREEN_WIDTH - 30, 20))
    display_surface.blit(score_surface, score_rect)

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        bg_music.stop()
        hit_sound.play()
        obstacle_group.empty()
        return True
    else: return False


while isGameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isGameRunning = False
            exit()
        if event.type == pygame.KEYDOWN:
            if isPlayerLost:
                isPlayerLost = False
                start_time = pygame.time.get_ticks()
        if event.type == obstacle_timer and not isPlayerLost:
            obstacle_group.add(Asteroid(choice([1, 1, 1, 2])))
        if event.type == pygame.KEYUP:
            pass

    if not isPlayerLost:
        bg_music.play(loops=-1, fade_ms=3)
        display_surface.blit(bg_surface, (0, 0))

        player.draw(display_surface)
        player.update()

        obstacle_group.draw(display_surface)
        obstacle_group.update()

        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.circle(display_surface, (0, 64, 0), mouse_pos, 10)

        displayScore()
        isPlayerLost = collision_sprite()
    else:
        time.sleep(2)
        gameover_rec = gameover_text.get_rect(center=(Settings.SCREEN_WIDTH*0.5, Settings.SCREEN_HEIGHT*0.2))
        tryagain_rec = tryagain_text.get_rect(center=(Settings.SCREEN_WIDTH*0.5, Settings.SCREEN_HEIGHT*0.8))
        display_surface.fill("Black")
        display_surface.blit(gameover_text, gameover_rec)
        display_surface.blit(tryagain_text, tryagain_rec)

    pygame.display.update()
    clock.tick(60)


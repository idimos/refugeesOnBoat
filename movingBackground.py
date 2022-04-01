import pygame, os
from pygame import mixer
from config import *

pygame.init()
clock = pygame.time.Clock()

bgImg = pygame.image.load('assets/sea44.jpg')
screen = pygame.display.set_mode(bgImg.get_size())
pygame.display.set_caption("Refugees Game")

# background music
if BGMusicOnStartUp == True:
    mixer.music.load(os.path.join('assets/sounds','background.wav'))
    mixer.music.play(-1)

bgX = 0
bgX2 = -bgImg.get_width()

def reDrawGameWindow():
    screen.blit(bgImg, (bgX, 0))
    screen.blit(bgImg, (bgX2, 0))
    pygame.display.update()

pygame.time.set_timer(pygame.USEREVENT+1, 500) # Sets the timer for 0.5 seconds
# This should go above the game loop

while True:
    clock.tick(FPS)

    bgX += 1.4
    bgX2 += 1.4
    if bgX > bgImg.get_width() :  # If our bg is at the -width then reset its position
        bgX = bgImg.get_width()*-1

    if bgX2 > bgImg.get_width():
        bgX2 = bgImg.get_width()*-1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.USEREVENT + 1:  # Checks if timer goes off
            FPS += 1  # Increases speed

    reDrawGameWindow()

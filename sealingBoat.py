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

pygame.time.set_timer(pygame.USEREVENT+1, 500) # Sets the timer for 0.5 seconds
# This should go above the game loop

class Boat():
    sail = [pygame.image.load(os.path.join('assets', '{}.png'.format(x))) for x in range(1, 9)]

    def __init__(self,x,y):
        self.x, self.y= x, y
        self.sailing = False
        self.frames = 0
        self.w = self.sail[0].get_width()
        self.h = self.sail[0].get_height()
        self.rect = self.sail[0].get_rect()
        self.rect.center = (self.x + self.w//2,self.y+self.h//2)

    def draw(self):
        if self.frames >= 56:
            self.frames = 0
        screen.blit(self.sail[self.frames // 7], (self.x, self.y))
        self.frames += 1
        pygame.draw.rect(screen,(255,0,0),self.rect,1)

def reDrawGameWindow():
    screen.blit(bgImg, (bgX, 0))
    screen.blit(bgImg, (bgX2, 0))
    boat.draw()
    pygame.display.update()

boat = Boat(bgImg.get_width()*2//3, bgImg.get_height()*2//3)

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


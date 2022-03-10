import pygame, os
from pygame import mixer
from config import *

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
pygame.display.set_caption("Refugees Game")

if BGMusicOnStartUp == True:
    mixer.music.load(os.path.join('assets/sounds','background.wav'))
    mixer.music.play(-1)

# load images
bgImageName = os.path.join('assets','boat1.png')
bgImage = pygame.image.load(bgImageName)
bgImage = pygame.transform.scale(bgImage,(SCREEN_WIDTH,SCREEN_HEIGHT)).convert_alpha()
bgX = 0
bgX2 = bgImage.get_width()

class Boat():
    def __init__(self,x,y,img):
        self.x = x
        self.y = y
        self.img = img
        self.boatImg = pygame.image.load(self.img).convert_alpha()
        self.rect = self.boatImg.get_rect()
        self.rect.center = (self.x,self.y)
        self.step = self.rect.height*4//100
        # self.boatImg = pygame.transform.scale(self.boatImg,)

    def show(self):
        # screen.blit(self.boatImg,(self.rect.x,self.rect.y))
        screen.blit(pygame.transform.flip(self.boatImg, True, False), (self.rect.x, self.rect.y))

    def move(self):
        dy = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            dy = -self.step

        if keys[pygame.K_DOWN]:
            dy = self.step

        self.rect.y += dy

myboat = Boat(SCREEN_WIDTH-SCREEN_WIDTH//6,SCREEN_HEIGHT//2,os.path.join('assets','Ship.png'))
run = [pygame.image.load(os.path.join('assets','{}.png'.format(x))) for x in range(1,9)]
delay = 0

def reDrawGameWindow():
    global delay

    screen.blit(bgImage, (0, 0))
    if delay+1 >=56:
        delay = 0
    delay += 1
    screen.blit(run[delay//7],(0,0))
    pygame.display.update()

while True:
    clock.tick(FPS)
    bgX -= -1.4
    bgX2 -= -1.4

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    myboat.show()
    myboat.move()

    reDrawGameWindow()
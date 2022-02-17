from config import *
import pygame, os, sys

class Scene():
    id = 0
    def __init__(self, bgImage):
        App.scenes.append(self)
        self.id = Scene.id
        Scene.id += 1
        self.nodes = []
        self.bg = bgImage
        print("Scene {} created".format(self.id))

    def draw(self):
        App.screen.blit(self.bg,(0,0))
        for node in self.nodes:
            node.move()
            node.draw()
        pygame.display.flip()

class Actor():
    def __init__(self,x,y,img):
        self.x = x
        self.y = y
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.flip = False
        App.scene.nodes.append(self)

    def draw(self):
        App.screen.blit( pygame.transform.flip(self.image,self.flip,False) ,(self.rect.x,self.rect.y))

    def move(self):
        dx = 0
        dy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            dx = -14
            self.flip = True
        if keys[pygame.K_RIGHT]:
            dx = 14
            self.flip = False

        # check screen's limits
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > SCREEN_WIDTH:
            dx = SCREEN_WIDTH - self.rect.right

        self.rect.x += dx
        self.rect.y += dy

class App():
    def __init__(self):
        # set pygame frames per second - FPS
        self.clock = pygame.time.Clock()
        pygame.init()
        App.flags = pygame.RESIZABLE
        App.screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT],self.flags)
        pygame.display.set_caption("Refugees Game")
        App.scenes = []

        # load images
        self.scene1Bg = pygame.image.load(os.path.join("assets","testBg.jpg"))
        size = App.screen.get_size()
        self.scene1Bg = pygame.transform.smoothscale(self.scene1Bg,size)

        self.scene2Bg = pygame.image.load(os.path.join("assets", "scene2.png")).convert_alpha()
        size = App.screen.get_size()
        self.scene2Bg = pygame.transform.smoothscale(self.scene2Bg,size)

        self.actorImg = pygame.image.load(os.path.join("assets", "actor2.png")).convert_alpha()
        self.actorImg = pygame.transform.smoothscale(self.actorImg,(50,80))
        self.scene1 = Scene(self.scene1Bg)
        App.scene = self.scene1
        self.scene2 = Scene(self.scene2Bg)
        self.actor = Actor(SCREEN_WIDTH//2,SCREEN_HEIGHT-100,self.actorImg)

    def run(self):
        while True:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            App.scene.draw()

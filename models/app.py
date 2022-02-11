from config import *
import pygame

class Scene():
    id = 0
    bg = GRAY
    def __init__(self, *args):
        App.scenes.append(self)
        App.scene = self
        self.id = Scene.id
        Scene.id += 1
        self.nodes = []
        self.bg = Scene.bg

    def draw(self):
        App.screen.fill(self.bg)
        for node in self.nodes:
            node.draw()
        pygame.display.flip()

class App():
    def __init__(self):
        pygame.init()
        App.flags = pygame.RESIZABLE
        App.screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT],self.flags)
        App.scenes = []
        App.running = True

    def run(self):
        while App.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    App.running = False

            App.screen.fill(GRAY)
            pygame.display.flip()
        pygame.quit()
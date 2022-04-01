import pygame, os
from pygame import mixer
from gameSettings import *

class SceneBase:
    def __init__(self,screen):
        self.next = self
        self.screen = screen
        self.panel = Panel(screen)

    def ProcessInput(self, events, pressed_keys):
        pass

    def Update(self):
        pass

    def Render(self):
        # screen.blit(self.panelHeader,self.panelHeaderRect)
        pass

    def SwitchToScene(self, next_scene):
        self.next = next_scene

    def Terminate(self):
        self.SwitchToScene(None)

class TitleScene(SceneBase):
    def __init__(self,screen):
        SceneBase.__init__(self,screen)
        self.bg = pygame.image.load('assets/TitleScene_0_Bg-01.png').convert_alpha()
        self.bg = pygame.transform.scale(self.bg,(SCR_W,SCR_H-100))
        mixer.music.load('assets/sounds/background.wav')
        mixer.music.play(-1)

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                self.SwitchToScene(AegeanScene(self.screen))

    def Update(self):
        self.panel.update("Press ENTER to Start...")

    def Render(self):
        self.screen.blit(self.bg, (0,0))

class AegeanScene(SceneBase):
    def __init__(self,screen):
        SceneBase.__init__(self,screen)
        self.bg = pygame.image.load('assets/sea44.jpg').convert_alpha()
        self.bg = pygame.transform.scale(self.bg,(SCR_W,SCR_H-100))
        self.bgX = 0
        self.bgX2 = -self.bg.get_width()
        self.boat = Boat(500,240,self.screen)
        self.face = Face(SCR_W-120,0,self.screen)
        mixer.music.load('assets/sounds/gentle-ocean-waves-breaking-on-beach-d-9333.wav')
        mixer.music.play(-1)

    def ProcessInput(self, events, pressed_keys):
        pass

    def Update(self):
        self.bgX += 1.4
        self.bgX2 += 1.4
        if self.bgX > self.bg.get_width() :  # If our bg is at the -width then reset its position
            self.bgX = self.bg.get_width()*-1

        if self.bgX2 > self.bg.get_width():
            self.bgX2 = self.bg.get_width()*-1

        self.panel.update("The boat full of refugges is sailing to Greece...")

    def Render(self):
        self.screen.blit(self.bg, (self.bgX, 0))
        self.screen.blit(self.bg, (self.bgX2, 0))
        self.boat.draw()
        # self.face.draw()

class Panel:
    def __init__(self,screen):
        self.screen = screen
        self.infoPanelRect = pygame.Rect(0,500,SCR_W,100)
        self.BASICFONT = pygame.font.Font('assets/fonts/Franky-Outline.ttf', BASICFONTSIZE)
        self.MSGFONT = pygame.font.Font('assets/fonts/Altona-Sans.ttf', BASICFONTSIZE - 12)

    def update(self,msg):
        pygame.draw.rect(self.screen, GRAY, self.infoPanelRect, 0)
        self.screen.blit(self.BASICFONT.render("Refugees Stories",True,RED),(10,510))
        self.screen.blit(self.MSGFONT.render(msg,True,RED),(10,550))

class Boat():
    sail = [pygame.image.load(os.path.join('assets', 'AegeanSceneBoat{}.png'.format(x))) for x in range(1, 4)]
    for i in range(3):
        sail[i] = pygame.transform.scale(sail[i],(160,120))

    def __init__(self,x,y,scr):
        self.x, self.y= x, y
        self.screen = scr
        self.sailing = False
        self.frames = 0
        self.w = self.sail[0].get_width()
        self.h = self.sail[0].get_height()
        self.rect = self.sail[0].get_rect()
        self.rect.center = (self.x + self.w//2,self.y+self.h//2)

    def draw(self):
        if self.frames >= 24:
            self.frames = 0
        self.screen.blit(self.sail[self.frames // 8], (self.x, self.y))
        self.frames += 1
        pygame.draw.rect(self.screen,(255,0,0),self.rect,1)

class Face:
    faces = [pygame.image.load(os.path.join('assets', 'Face{}.png'.format(x))) for x in range(1, 3)]
    for i in range(2):
        faces[i] = pygame.transform.scale(faces[i], (120, 120))

    def __init__(self, x, y, scr):
        self.x, self.y = x, y
        self.screen = scr
        self.speaking = False
        self.frames = 0
        self.w = self.faces[0].get_width()
        self.h = self.faces[0].get_height()
        self.rect = self.faces[0].get_rect()
        print(self.rect)
        self.rect.center = (self.x + self.w // 2, self.y + self.h // 2)

    def draw(self):
        if self.frames >= 16:
            self.frames = 0
        self.screen.blit(self.faces[self.frames // 8], (self.x, self.y))
        self.frames += 1
        pygame.draw.rect(self.screen, (255, 0, 0), self.rect, 1)
        if not self.speaking:
            self.speaking = True
            facestory = mixer.Sound('assets/sounds/yannisvoice.wav')
            facestory.play()
            self.speaking = False


class Game:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode( (SCR_W,SCR_H))
        pygame.display.set_caption("Ιστορίες προσφυγιάς")
        self.active_scene = TitleScene(self.screen)

    def run(self):
        self.pressed_keys = pygame.key.get_pressed()
        self.filtered_events = []
        while self.active_scene != None:
            for event in pygame.event.get():
                self.want_to_exit = False
                if event.type == pygame.QUIT or \
                        (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self.want_to_exit = True

            if self.want_to_exit:
                self.active_scene.Terminate()
            else:
                self.filtered_events.append(event)

            self.active_scene.ProcessInput(self.filtered_events, self.pressed_keys)
            self.active_scene.Update()
            self.active_scene.Render()

            self.active_scene = self.active_scene.next

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()
        exit()

if __name__ == '__main__':
    Game().run()
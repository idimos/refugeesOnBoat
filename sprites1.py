import pygame, random
from gameSettings import *

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode( (SCR_W,SCR_H))
playerImage = pygame.image.load('assets/p1_front.png').convert()
bgImage = pygame.image.load('assets/seaSimple.jpg').convert( )
bgImage = pygame.transform.scale(bgImage,(SCR_W,SCR_H))
activeColor = GRAY

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50) )
        # self.image.fill(GREEN)
        self.image = playerImage
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.centerx = SCR_W//2
        self.rect.bottom = SCR_H - 10
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx

        if self.rect.right > SCR_W:
            self.rect.right = SCR_W
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        sprites.add(bullet)
        bullets.add(bullet)

class Peirates(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCR_W - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > SCR_H + 10 or self.rect.left < -25 or self.rect.right > SCR_W + 20:
            self.rect.x = random.randrange(SCR_W - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()


sprites = pygame.sprite.Group()
peirates = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player()
sprites.add(player)
for i in range(8):
    p = Peirates()
    sprites.add(p)
    peirates.add(p)

while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    sprites.update()

    screen.fill(activeColor)
    screen.blit(bgImage,(0,0))
    sprites.draw(screen)

    pygame.display.update()

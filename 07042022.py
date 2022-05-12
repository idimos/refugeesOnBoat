import random
import pygame
from pygame import mixer

pygame.init()
res = (1200,900)
topRect = pygame.Rect(0,0,res[0],50)
screen = pygame.display.set_mode( (res) )
pygame.display.set_caption("Refugees Game")
clock = pygame.time.Clock()

# φορτώνω τους ήχους. Ο πρώτος παίζει στο background ενώ ο δεύτερος όταν
# χτυπάω ένα αντικείμενο
mixer.music.load('assets/sounds/gentle-ocean-waves-breaking-on-beach-d-9333.wav')
mixer.music.play(-1)
explSound = pygame.mixer.Sound('assets/sounds/explosion.wav')

# φορτώνω όλα τα γραφικά
bgImg = pygame.image.load('assets/mygame-01.png').convert()
yellowDiamond = pygame.image.load('assets/gemYellow.png').convert()
greenDiamond = pygame.image.load('assets/gemGreen.png').convert()
redDiamond = pygame.image.load('assets/gemRed.png').convert()
playerImg = pygame.image.load('assets/p1_front.png').convert()

# τα 2 σημεία αναφοράς για να φτιάξω το κινούμενο background
bgX = 0
bgX2 = -bgImg.get_width()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface( (50,50))
        self.image = playerImg
        self.image.set_colorkey((0,0,0))
        # self.image.fill( (255,0,0))
        self.rect = self.image.get_rect()
        self.rect.centerx = res[0] // 2
        self.rect.bottom = res[1]
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx

        if self.rect.right > res[0]:
            self.rect.right = res[0]
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        sprites.add(bullet)
        bullets.add(bullet)

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,25))
        self.image.fill( (120,120,120))
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = 5

    def update(self):
        self.rect.y -= self.speedy
        if self.rect.bottom < 0:
            self.kill()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,30))
        # self.image.fill((0,0,125))
        self.image = yellowDiamond
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(self.rect.width,res[0]-self.rect.width)
        self.rect.y = random.randint(-self.rect.height,self.rect.height)
        self.speedy = random.randint(1,4)
        self.speedx = 0

    def update(self):
        self.rect.top += self.speedy
        if self.rect.bottom > res[1]:
            self.rect.x = random.randint(self.rect.width, res[0] - self.rect.width)
            self.rect.y = random.randint(-self.rect.height, self.rect.height)

class Enemy1(Enemy):
    def __init__(self):
        Enemy.__init__(self)
        self.image = greenDiamond
        self.image.set_colorkey((0,0,0))

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, (0,0,0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

player = Player()
sprites = pygame.sprite.Group()
sprites.add(player)
bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()
enemies1 = pygame.sprite.Group()

for _ in range(5):
    enem = Enemy()
    sprites.add(enem)
    enemies.add(enem)
    enem1 = Enemy1()
    sprites.add(enem1)
    enemies1.add(enem1)
score = 0

while True:
    clock.tick(60)

    bgX += 1.4
    bgX2 += 1.4
    if bgX > bgImg.get_width() :
        bgX = bgImg.get_width()*-1

    if bgX2 > bgImg.get_width():
        bgX2 = bgImg.get_width()*-1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    # screen.fill( (0,255,0) )
    screen.blit(bgImg, (bgX, 0))
    screen.blit(bgImg, (bgX2, 0))

    sprites.update()
    hits = pygame.sprite.groupcollide(enemies,bullets,True,True)
    for _ in hits:
        enem = Enemy()
        sprites.add(enem)
        enemies.add(enem)
        score += 1
        explSound.set_volume(2.0)
        pygame.mixer.Sound.play(explSound)

    sprites.draw(screen)
    pygame.draw.rect(screen,(255,255,255),topRect,0)
    draw_text(screen,'Score: {}'.format(score),28,90,10)
    screen.blit(yellowDiamond,(1000,0))
    screen.blit(greenDiamond, (1050,0))
    screen.blit(redDiamond, (1100, 0))
    redDiamond.set_colorkey((0,0,0))

    pygame.display.update()

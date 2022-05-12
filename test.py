import pygame

pygame.init()
res = (1200,900)
screen = pygame.display.set_mode( (res) )
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface( (50,50))
        self.image.fill( (255,0,0))
        self.rect = self.image.get_rect()
        self.rect.centerx = res[0] // 2
        self.rect.bottom = res[1] - 10
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
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = 5

    def update(self):
        self.rect.y -= self.speedy
        if self.rect.bottom < 0:
            self.kill()

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, (255,255,255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

player = Player()
sprites = pygame.sprite.Group()
sprites.add(player)
bullets = pygame.sprite.Group()
score = 0

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    screen.fill( (0,255,0) )
    sprites.update()
    sprites.draw(screen)
    draw_text(screen,str(score),32,50,res[1]-80)

    pygame.display.update()

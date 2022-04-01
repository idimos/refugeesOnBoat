import pygame
from pygame import mixer

pygame.init()
clock = pygame.time.Clock()

RED = (255,0,0)
GREEN = (0,255,0)
PINK = (255,153,255)
YELLOW = (255,255,0)

screen = pygame.display.set_mode((600,400))
activeColor = GREEN
screen.fill(activeColor)

myrect = pygame.Rect(screen.get_rect())
myrect.inflate_ip(-300,-200)

ON_BOX = pygame.USEREVENT + 1
PLAY_SOUND = pygame.USEREVENT + 2
grow = True
pygame.time.set_timer(PLAY_SOUND,2000)

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == ON_BOX:
            if grow :
                myrect.inflate_ip(3,3)
                grow = myrect.width < 350
            else:
                myrect.inflate_ip(-3,-3)
                grow = myrect.width < 300

        if event.type == PLAY_SOUND:
            soundFile = mixer.Sound('assets/sounds/laser.wav')
            soundFile.play()
            if activeColor == GREEN:
                screen.fill(PINK)
                activeColor = PINK
            elif activeColor == PINK:
                screen.fill(GREEN)
                activeColor = GREEN

    if myrect.collidepoint(pygame.mouse.get_pos()):
        pygame.event.post(pygame.event.Event(ON_BOX))

    pygame.draw.rect(screen, YELLOW, myrect, 0)
    pygame.display.update()
    clock.tick(60)

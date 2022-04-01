import pygame

pygame.init()
clock = pygame.time.Clock()
RED = (255,0,0)
GREEN = (0,255,0)
YELLOW = (255,255,0)

screen = pygame.display.set_mode( (620,480))
activeColor = YELLOW
CHANGE_BG_COLOR = pygame.USEREVENT + 1
ON_BOX = pygame.USEREVENT + 2
ON_BOX2 = pygame.USEREVENT + 3

pygame.time.set_timer(CHANGE_BG_COLOR, 500)
myrect = pygame.Rect(20,20, 100,100)
myrect2 = pygame.Rect(120,120, 100,100)

while True:
    screen.fill(activeColor)
    pygame.draw.rect(screen,GREEN,myrect,0)
    pygame.draw.rect(screen, (255,153,128), myrect2, 0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == CHANGE_BG_COLOR:
            if activeColor == RED:
                activeColor = YELLOW
            elif activeColor == YELLOW:
                activeColor = RED

        if event.type == ON_BOX:
            print("Mouse over Green Box...")

        if event.type == ON_BOX2:
            print("Mouse over Green Box2...")

    if myrect.collidepoint(pygame.mouse.get_pos()) :
        pygame.event.post( pygame.event.Event(ON_BOX))
    if myrect2.collidepoint(pygame.mouse.get_pos()) :
        pygame.event.post( pygame.event.Event(ON_BOX2))

    pygame.display.update()
    clock.tick(30)
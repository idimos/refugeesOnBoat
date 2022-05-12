import pygame

pygame.init()
clock = pygame.time.Clock()
RED = (255,0,0)
GREEN = (0,255,0)
YELLOW = (255,255,0)

screen = pygame.display.set_mode( (620,480))
activeColor = YELLOW

myrect = pygame.Rect(20,20, 100,100)

def button(screen, position, text):
    font = pygame.font.SysFont("Arial", 30)
    text_render = font.render(text, 1, (255, 0, 0))
    x, y, w , h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w , y), 5)
    pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
    pygame.draw.rect(screen, (100, 100, 100), (x, y, w , h))
    return screen.blit(text_render, (x, y))

def start():
    print("Ok, let's go")

def quit():
    pygame.quit()
    exit()

screen.fill(activeColor)
b1 = button(screen, (400, 300), "Quit")
b2 = button(screen, (500, 300), "Start")
while True:

    pygame.draw.rect(screen,GREEN,myrect,0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if b1.collidepoint(pygame.mouse.get_pos()):
                quit()
            elif b2.collidepoint(pygame.mouse.get_pos()):
                start()

    pygame.display.update()
    clock.tick(30)
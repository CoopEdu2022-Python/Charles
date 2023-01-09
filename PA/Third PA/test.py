import pygame
import sys
from data import *
from end import *

pygame.init()
screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()
end_png = pygame.image.load("resources/images/ending/restart-1.png")
end = End(end_png, SCREENSIZE)
while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    end.draw(screen)

    screen.fill(BACKGROUND_COLOR)
    pygame.display.update()
    clock.tick(FPS)

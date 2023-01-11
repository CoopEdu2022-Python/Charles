import pygame
from pygame import locals
import sys


def trick_video():
    pygame.init()
    screen = pygame.display.set_mode((1400, 600))
    FPS = pygame.time.Clock()
    pygame.mixer.music.load("resources/audios/trick audio/trick video/Rick Astley - Never Gonna Give You Up (7_ Mix).flac")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()
    i = 0
    for n in range(3067):
        for event in pygame.event.get():
            if event. type == locals. QUIT:
                pygame. quit()
                sys. exit()

        background = pygame.image.load("resources/audios/trick audio/trick video/trick.mp4_%d.jpg" % i)
        screen.blit(background, (250, 70))
        i += 1
        pygame.display.update()
        FPS. tick(25)

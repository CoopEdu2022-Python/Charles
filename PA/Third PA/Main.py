import pygame
import sys
import random
from Ground import *
from Cloud import *
from Cactus import *
"""Settings"""
FPS = 60
TITLE = 'Chrome Dino'
BACKGROUND_COLOR = (235, 235, 235)
SCREENSIZE = (700, 300)
IMAGE_PATHS = {
    'ground': 'ground.png',
    'cloud': 'cloud.png',
}
pygame.init()
screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

"""Ground"""
ground_png = pygame.image.load("ground.png")
ground = Ground(ground_png)

"""Clouds"""
cloud_png = pygame.image.load("cloud.png")
clouds = pygame.sprite.Group()

"""Cactus"""
cactus_list = [pygame.image.load("pictures\Cactus1.png"),
               pygame.image.load("pictures\Cactus2.png"),
               pygame.image.load("pictures\Cactus3.png"),
               pygame.image.load("pictures\Cactus4.png"),
               pygame.image.load("pictures\Cactus5.png"),
               pygame.image.load("pictures\Cactus6.png")]
cactus = pygame.sprite.Group()


"""Main"""
timer = 0
a = 90
rand_num = random.randint(0, 30)
print(rand_num)
while True:
    if timer % a == 0:
        rand_num = random.randint(0, 30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(BACKGROUND_COLOR)

    """ground"""
    ground.update()
    ground.draw(screen)

    """clouds"""
    if timer % 128 == 0 or timer % 200 == 0:
        clouds.add(Cloud(cloud_png))
    clouds.update()
    clouds.draw(screen)

    """cactus"""
    if int(timer % a) == rand_num:
        print(timer % a)
        cactus.add(Cactus(cactus_list[random.randint(0, 5)]))
    cactus.update()
    cactus.draw(screen)

    pygame.display.update()
    clock.tick(FPS)
    timer += 1


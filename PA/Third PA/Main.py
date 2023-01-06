import pygame
import sys
import random
from data import *
from Ground import *
from Cloud import *
from Cactus import *
from Ptera import *
from Dinosaur import *


"""Settings"""
pygame.init()
screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

"""Ground"""
ground_png = pygame.image.load("resources\images\ground\ground.png")
ground = Ground(ground_png, SCREENSIZE)

"""Clouds"""
cloud_png = pygame.image.load("resources/images/cloud/cloud.png")
clouds = pygame.sprite.Group()

"""Cactus"""
cactus_png = [pygame.image.load("resources\images\cactus\cactus-1.png"),
              pygame.image.load("resources\images\cactus\cactus-2.png"),
              pygame.image.load("resources\images\cactus\cactus-3.png"),
              pygame.image.load("resources\images\cactus\cactus-4.png"),
              pygame.image.load("resources\images\cactus\cactus-5.png"),
              pygame.image.load("resources\images\cactus\cactus-6.png")]
cactus = pygame.sprite.Group()
a = 120
rand_num = random.randint(0, 60)

"""Ptera"""
ptera_png = [pygame.image.load("resources\images\pterodactyl\pterodactyl-1.png"),
             pygame.image.load("resources\images\pterodactyl\pterodactyl-2.png")]
ptera = pygame.sprite.Group()

"""Dino"""
dino_png = [pygame.image.load("resources\images\dinosaur\dinosaur-start.png"),
            pygame.image.load("resources\images\dinosaur\dinosaur-jump.png"),
            pygame.image.load("resources\images\dinosaur\dinosaur-run-1.png"),
            pygame.image.load("resources\images\dinosaur\dinosaur-run-2.png"),
            pygame.image.load("resources\images\dinosaur\dinosaur-duck-1.png"),
            pygame.image.load("resources\images\dinosaur\dinosaur-duck-2.png"),
            pygame.image.load("resources\images\dinosaur\dinosaur-die-1.png"),
            pygame.image.load("resources\images\dinosaur\dinosaur-die-2.png"),
            pygame.image.load("resources\images\dinosaur\dinosaur-unknown-1.png")]
dino = Dinosaur(dino_png, SCREENSIZE)
dino_status = "still alive"


i = 0
while i == 0:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_SPACE, pygame.K_UP):
                i = 1
                break


"""Main"""
timer = 0
jump = 0
while True:
    if timer % a == 0:
        rand_num = random.randint(0, 30)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_SPACE, pygame.K_UP):
                pygame.mixer.Sound('resources/audios/jump.mp3').play()
                dino.jump()
            elif event.key == pygame.K_DOWN:
                dino.duck()
        elif event.type == pygame.KEYUP and dino.status == 4:
            dino.unduck()

    screen.fill(BACKGROUND_COLOR)

    """ground"""
    ground.update()
    ground.draw(screen)

    """clouds"""
    if timer % 128 == 0 or timer % 200 == 0:
        clouds.add(Cloud(cloud_png, SCREENSIZE))
    clouds.update()
    clouds.draw(screen)

    """barrier: cactus, ptera"""
    if int(timer % a) == rand_num:
        if random.sample([0, 0, 0, 1, 1, 1, 1, 1, 1, 1], 1)[0] == 1:
            cactus.add(Cactus(cactus_png[random.randint(0, 5)], SCREENSIZE))
        else:
            ptera.add(Ptera(ptera_png, SCREENSIZE))
    ptera.update()
    ptera.draw(screen)
    cactus.update()
    cactus.draw(screen)

    """main character"""
    if dino_status == "still alive":
        dino.update()
        dino.draw(screen)

    pygame.display.update()
    clock.tick(FPS)
    timer += 1
    # print(dino.status, "<-----------")

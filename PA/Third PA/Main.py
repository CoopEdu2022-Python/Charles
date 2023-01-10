import pygame
import sys
import random
from config import *
from Ground import *
from Cloud import *
from Cactus import *
from Ptera import *
from Dinosaur import *
from ScoreBoard import *
from end import *

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

"""ScoreBoard"""
s_b_pngs = [pygame.image.load("resources/images/scoreboard/scoreboard-0.png"),
            pygame.image.load("resources/images/scoreboard/scoreboard-1.png"),
            pygame.image.load("resources/images/scoreboard/scoreboard-2.png"),
            pygame.image.load("resources/images/scoreboard/scoreboard-3.png"),
            pygame.image.load("resources/images/scoreboard/scoreboard-4.png"),
            pygame.image.load("resources/images/scoreboard/scoreboard-5.png"),
            pygame.image.load("resources/images/scoreboard/scoreboard-6.png"),
            pygame.image.load("resources/images/scoreboard/scoreboard-7.png"),
            pygame.image.load("resources/images/scoreboard/scoreboard-8.png"),
            pygame.image.load("resources/images/scoreboard/scoreboard-9.png"),
            pygame.image.load("resources/images/scoreboard/scoreboard-10.png")]
score_board = Scoreboard(s_b_pngs, SCREENSIZE)
if score_board.high_score == 0:
    first = 0
else:
    first = 1


"""comic for ending"""
end_pngs = [pygame.image.load("resources/images/ending/game-over.png"),
            pygame.image.load("resources/images/ending/restart-1.png"),
            pygame.image.load("resources/images/ending/restart-2.png"),
            pygame.image.load("resources/images/ending/restart-3.png"),
            pygame.image.load("resources/images/ending/restart-4.png"),
            pygame.image.load("resources/images/ending/restart-5.png"),
            pygame.image.load("resources/images/ending/restart-6.png"),
            pygame.image.load("resources/images/ending/restart-7.png"),
            pygame.image.load("resources/images/ending/restart-8.png")]
end = End(end_pngs, SCREENSIZE)


"""start"""
i = 0
while i == 0:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(BACKGROUND_COLOR)
    # dino.update()
    dino.start(screen)
    # ground.update()
    ground.start(screen)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_SPACE, pygame.K_UP):
                dino.jump()
                i = 1
                break
    pygame.display.update()

"""run"""
while 1:
    """main"""
    timer = 0
    while dino.status != 6 or 7:
        current_score = timer // 6
        if timer % a == 0:
            rand_num = random.randint(0, 30)

        """window close"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            """keyboard enter capture"""
            Key_pressed = pygame.key.get_pressed()  # this is something I searched online to realize the long press
            if (Key_pressed[pygame.K_SPACE] or Key_pressed[pygame.K_UP]) and dino.rect.bottom == dino.y:
                pygame.mixer.Sound('resources/audios/jump.mp3').play()
                dino.jump()

            if Key_pressed[pygame.K_DOWN] and dino.rect.bottom != dino.y:  # duck while not touching the ground
                dino.t = 1  # reset the timer that calculates the movement of dino
                dino.speed_down()
            elif Key_pressed[pygame.K_DOWN]:
                dino.duck()

            if event.type == pygame.KEYUP and dino.status == 4:
                dino.unduck()

        screen.fill(BACKGROUND_COLOR)  # fill in the background color

        """environment: ground, clouds"""
        if timer % 128 == 0 or timer % 200 == 0:
            clouds.add(Cloud(cloud_png, SCREENSIZE))
        ground.update()
        ground.draw(screen)
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

        """Score Board"""

        score_board.update(current_score, first)
        score_board.draw(screen)
        if current_score // 200 == 0 and current_score < 1000:
            MOVING_SPEED *= 3
            current_score *= 1.3

        """collide detection"""
        for _ in ptera:
            if pygame.sprite.collide_mask(dino, _):
                dino.die("day")  # self.status = 'die'
                break
        for _ in cactus:
            if pygame.sprite.collide_mask(dino, _):
                dino.die("day")  # self.status = 'die'
                break

        # print(dino.status)
        if dino.status != 6 and 7:
            """main character: dino"""
            dino.update()
            dino.draw(screen)
            timer += 1
            pygame.display.update()
            clock.tick(FPS)
        else:
            dino.refresh()  # change image when dinosaur dies
            dino.draw(screen)  # show the image that dino dies
            first = 1
            score_board.update(current_score, first)
            i = 1
            pygame.display.update()
            break
        # print(dino.status, "<-----------")
    # print(111111)
    """end"""
    while i == 1:

        """ending fiction"""
        end.update()
        end.draw(screen)

        """record the high score"""
        with open("data/high-score", "w") as f:
            f.write(str(score_board.high_score))

        for event in pygame.event.get():

            """window close"""
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            """restart the game"""
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_SPACE, pygame.K_UP):
                    dino.jump()
                    for _ in cactus:
                        _.kill()
                    for _ in ptera:
                        _.kill()

                    pygame.display.update()
                    i = 0
                    break

        pygame.display.update()
        clock.tick(FPS)

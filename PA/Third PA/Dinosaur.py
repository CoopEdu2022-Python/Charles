import pygame
from config import *


class Dinosaur(pygame.sprite.Sprite):
    def __init__(self, images, screen_size):
        pygame.sprite.Sprite.__init__(self)

        self.x, self.y = screen_size[0], screen_size[1]
        """
        start = images[0]
        jump = images[1]
        run_1 = images[2]
        run_2 = images[3]
        duck_1 = images[4]
        duck_2 = images[5]
        die_1_white_edge = images[6]
        die_2 = images[7]
        unknown = images[8]
        """
        self.images = images
        self.image = self.images[0]  # start position for the dinosaur
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.bottom = (0.06 * self.x + 3, self.y)
        self.mask = pygame.mask.from_surface(self.image)
        self.status = 2

        self.g = GRAVITY
        self.t = TIME_t
        self.x1 = START_x1
        self.x2 = START_x2
        self.t_max = self.x2

        self.refresh_rate = REFRESHING_RATE // 2
        self.refresh_counter = 0

    def start(self, screen):
        self.rect.bottom = self.y
        screen.blit(self.image, self.rect)
        # self.rect.bottom = self.y

    def jump(self):
        self.status = 1

    def duck(self):
        self.status = 4

    def unduck(self):
        self.status = 2

    def speed_fall(self):
        self.status = -2
        self.update()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def die(self, DIN):
        if DIN == "day":
            self.status = 6
        else:
            self.status = 7
        self.refresh()

    def refresh(self):
        if self.status == 1 or self.status == -2:  # only show one picture when dino jump and speed fall
            self.image = self.images[1]
            pass
        elif self.image == self.images[self.status]:
            self.image = self.images[self.status + 1]
        else:
            self.image = self.images[self.status]

        if self.status == 6:
            self.image = self.images[6]
        elif self.status == 7:
            self.image = self.images[7]

        """
        This function as the outer shell of the collision mask
        It's cool but I don't understand how it works, it just worked~
        """
        if self.status == 4:
            width = int(self.image.get_size()[0] * 0.7)
            height = self.image.get_size()[1]
            image = pygame.transform.scale(self.image, (width, height))
            self.mask = pygame.mask.from_surface(image)
            return
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        # print(self.rect.bottom)
        pass
        """normal run & jump"""
        if self.status == 2 or self.status == 4:  # run during day and night
            if self.refresh_counter == self.refresh_rate:
                self.refresh()
                self.refresh_counter = 0
            self.refresh_counter += 1

        elif self.status == 1:  # jump
            self.rect.bottom = self.y + self.g * (self.t - self.x1) * (self.t - self.x2)
            if self.t < self.t_max:
                self.t += INCREASING_RATE_t
            elif self.t == self.t_max:
                self.status = 2
                self.t = 0
            self.refresh()
            # print(self.rect.bottom)

        """speed fall"""
        if self.status == -2:
            if self.rect.bottom != self.y:
                self.rect.bottom -= (-4 * self.t)
                # print(self.rect.bottom, "!!!!!!!!!!")
                if self.rect.bottom < self.y:
                    self.t += INCREASING_RATE_t
                elif self.rect.bottom + (4 * self.t) >= self.y:
                    self.rect.bottom = self.y
                    self.t = 0
                    self.status = 4  # automatically duck after speed down
                self.refresh()
                # print(self.rect.bottom, "?????????")



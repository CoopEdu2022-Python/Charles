import pygame
import random
from data import *


class Ptera(pygame.sprite.Sprite):
    def __init__(self, images, screen_size):
        pygame.sprite.Sprite.__init__(self)

        x, y = screen_size[0], screen_size[1]
        self.images = images
        self.image = self.images[0]
        self.rect = self.image.get_rect()  # get the rectangular position for the object
        self.rect.left, self.rect.bottom = (x, random.sample([y, y - 60, y - 100], 1)[0])  # 3 random position for ptera

        self.mask = pygame.mask.from_surface(self.image)  # create mask for collied detection
        # speed setting for ptera
        self.v = MOVING_SPEED
        self.v1 = self.v * 1.15
        self.v2 = self.v * 0.85
        self.speed = random.sample([self.v1, self.v, self.v2], 1)[0]

        self.refresh_rate = REFRESHING_RATE
        self.refresh_counter = 0

    def refresh(self):
        if self.image == self.images[0]:
            self.image = self.images[1]
        else:
            self.image = self.images[0]
        self.mask = pygame.mask.from_surface(self.image)  # refresh mask for collied detection

    def update(self):
        "define how fast the ptera flip its wings"""
        if self.refresh_counter == self.refresh_rate:
            self.refresh()               # refresh the movement
            if self.speed == self.v1:                           # if speed is fast
                self.refresh_counter = (REFRESHING_RATE * 0.5)  # the wings will flap faster
            elif self.speed == self.v:      # if speed is normal
                self.refresh_counter = 0    # the wings will flap in normal speed
            elif self.speed == self.v2:                          # if speed is fast
                self.refresh_counter = -(REFRESHING_RATE * 0.5)  # the wings will flap slower
        self.refresh_counter += 1

        """if out, delete"""
        self.rect.left += self.speed
        if self.rect.right < 0:
            self.kill()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

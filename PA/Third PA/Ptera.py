import pygame
import random
from data import *

v = MOVING_SPEED
class Ptera(pygame.sprite.Sprite):
    def __init__(self, images, screen_size):
        pygame.sprite.Sprite.__init__(self)

        x, y = screen_size[0], screen_size[1]
        self.images = images
        self.image = self.images[0]
        self.rect = self.image.get_rect()  # get the rectangular position for the object
        self.rect.left, self.rect.bottom = (x, random.sample([y, y - 50, y - 100], 1)[0])  # 3 random position for ptera

        self.mask = pygame.mask.from_surface(self.image)  # create mask for collied detection

        self.speed = random.sample([v + 1, v, v - 1], 1)[0]

        self.refresh_rate = REFRESHING_RATE
        self.refresh_counter = 0

    def refresh(self):
        if self.image == self.images[0]:
            self.image = self.images[1]
        else:
            self.image = self.images[0]
        self.mask = pygame.mask.from_surface(self.image)  # refresh mask for collied detection

    def update(self):
        """define how fast the ptera flip its wings"""
        if self.refresh_counter == self.refresh_rate:
            self.refresh()  # refresh the movement
            if self.speed == v + 1:
                self.refresh_counter = -(REFRESHING_RATE * 0.5)
            elif self.speed == v:
                self.refresh_counter = 0
            elif self.speed == v - 1:
                self.refresh_counter = REFRESHING_RATE * 0.5
        self.refresh_counter += 1

        """if out, delete"""
        self.rect.left += self.speed
        if self.rect.right < 0:
            self.kill()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

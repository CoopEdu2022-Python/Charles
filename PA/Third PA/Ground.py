import pygame
from config import *


class Ground(pygame.sprite.Sprite):
    def __init__(self, image, screen_size):
        pygame.sprite.Sprite.__init__(self)

        # two same pictures
        y = screen_size[1]
        self.image_0 = image
        self.rect_0 = self.image_0.get_rect()
        # make sure the ground will always stick at the bottom of the screen
        self.rect_0.left, self.rect_0.bottom = (0, y)

        self.image_1 = image
        self.rect_1 = self.image_1.get_rect()
        self.rect_1.left, self.rect_1.bottom = self.rect_0.right, self.rect_0.bottom

        # pixels move each frame
        self.speed = MOVING_SPEED
        self.new_speed = self.speed

    def speed_up(self):
        self.new_speed *= 1.3

    # calculate position
    def update(self):
        self.rect_0.left += self.speed
        self.rect_1.left += self.speed
        if self.rect_0.right < 0:
            self.rect_0.left = self.rect_1.right
            self.rect_0, self.rect_1 = self.rect_1, self.rect_0  # stick two picture together

        """increase the speed"""
        if self.speed != self.new_speed:
            self.speed -= 0.01


    # draw to screen
    def draw(self, screen):
        screen.blit(self.image_0, self.rect_0)
        screen.blit(self.image_1, self.rect_1)

    def start(self, screen):
        screen.blit(self.image_0, self.rect_0)
        screen.blit(self.image_1, self.rect_1)

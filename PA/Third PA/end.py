import pygame
from config import *


class End(pygame.sprite.Sprite):
    def __init__(self, images, screen_size=None):
        pygame.sprite.Sprite.__init__(self)

        self.t = 1

        self.x, self.y = screen_size[0], screen_size[1]
        self.images = images
        self.image_fiction = self.images[1]
        self.rect = self.image_fiction.get_rect()
        self.rect.left, self.rect.bottom = ((self.x / 2) - 30, self.y / 2 + 50)
        self.image_over = self.images[0]
        self.rect_over = self.image_over.get_rect()
        self.rect_over.left, self.rect_over.bottom = ((self.x / 2) - 185, (self.y / 2) - 50)

        self.refresh_rate = REFRESHING_RATE
        self.refresh_counter = 0
        self.hold_counter = REFRESHING_RATE * 2

    def update(self):
        self.image_fiction = self.images[self.t]
        self.refresh_counter += 1

        if self.refresh_counter == self.refresh_rate and self.t < 8:
            self.t += 1
            self.refresh_counter = 0

    def draw(self, screen):
        screen.blit(self.image_fiction, self.rect)
        screen.blit(self.image_over, self.rect_over)




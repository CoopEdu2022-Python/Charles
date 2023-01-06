import pygame
import random
from data import *


class Cloud(pygame.sprite.Sprite):
    def __init__(self, image, screen_size):
        pygame.sprite.Sprite.__init__(self)

        x, y = screen_size[0], screen_size[1]
        self.image = image
        self.rect = self.image.get_rect()
        # set the relationship between the position of the cloud and the screen size
        self.rect.left, self.rect.bottom = (x, random.randint(y // 6, y // 5))

        self.speed = MOVING_SPEED * 0.3

    def update(self):
        self.rect.left += self.speed
        if self.rect.right < 0:
            self.kill()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
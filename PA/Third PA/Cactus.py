import pygame
from config import *


class Cactus(pygame.sprite.Sprite):
    def __init__(self, image, screen_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.bottom = screen_size

        self.mask = pygame.mask.from_surface(self.image)

        self.speed = MOVING_SPEED
        self.new_speed = self.speed

    def speed_up(self):
        self.speed -= 1

    def update(self):
        self.rect.left += self.speed
        if self.rect.right < 0:
            self.kill()
        #
        # if self.speed >= self.new_speed:
        #     self.speed -= 0.01


    def draw(self, screen):
        screen.blit(self.image, self.rect)

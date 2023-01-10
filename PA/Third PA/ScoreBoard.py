import pygame
from config import *


class Scoreboard(pygame.sprite.Sprite):
    def __init__(self, images, screen_size):
        pygame.sprite.Sprite.__init__(self)

        self.x, self.y = screen_size

        self.score = 0
        with open("data/high-score") as f:
            high_score = int(f.read())
        self.high_score = high_score

        self.images = images

        self.image_score = pygame.Surface((20 * 5, 31))
        self.rect_score = self.image_score.get_rect()

        self.image_high_score = pygame.Surface((60 + 20 * 5, 31))
        self.rect_high_score = self.image_high_score.get_rect()

        self.rect_score.right, self.rect_score.top = (self.x * 0.95, self.y * 0.1)
        self.rect_high_score.right, self.rect_high_score.top = self.rect_score.left - 20, self.rect_score.top

        self.refresh_rate = REFRESHING_RATE / 2
        self.refresh_count = 0

    def update(self, current_score, first_time):
        self.score = int(current_score)
        # stitch current score image
        self.image_score.fill((235, 235, 235))
        for i, _ in enumerate(str(self.score).zfill(5)):  # current score images
            self.image_score.blit(self.images[int(_)], (20 * i, 0))

        if self.score % 100 < 20 and self.score // 100 >= 1:

            if self.refresh_count == self.refresh_rate:
                print(1111111111111)
                self.image_score.set_alpha(255)
                self.refresh_count = 0
            self.refresh_count += 1

        # stitch high score image
        self.image_high_score.fill((235, 235, 235))
        self.image_high_score.set_alpha(190)
        if first_time == 1:
            if self.high_score <= self.score:
                self.high_score = self.score
            self.image_high_score.blit(self.images[-1], (0, 0))
            for i, _ in enumerate(str(self.high_score).zfill(5)):  # highest score images
                self.image_high_score.blit(self.images[int(_)], (60 + 20 * i, 0))

    def draw(self, screen):
        screen.blit(self.image_score, self.rect_score)
        screen.blit(self.image_high_score, self.rect_high_score)

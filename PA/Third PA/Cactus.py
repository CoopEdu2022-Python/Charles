import pygame


class Cactus(pygame.sprite.Sprite):
    def __init__(self, image, screen_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.bottom = screen_size

        self.mask = pygame.mask.from_surface(self.image)

        self.speed = -5

    def update(self):
        self.rect.left += self.speed
        if self.rect.right < 0:
            self.kill()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

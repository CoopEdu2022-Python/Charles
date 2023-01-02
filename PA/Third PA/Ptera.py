import pygame


class Ptera(pygame.sprite.Sprite):
    def __init__(self, image, p_position):
        pygame.sprite.Sprite.__init__(self)

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.bottom = (700, p_position)

        self.speed = -5

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)


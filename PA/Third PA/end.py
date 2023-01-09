import pygame


class End(pygame.sprite.Sprite):
    def __init__(self, image, screen_size=None):
        pygame.sprite.Sprite.__init__(self)

        self.x, self.y = screen_size[0], screen_size[1]
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.bottom = (self.x/2, self.y/2)

    def draw(self, screen):
        screen.blit(self.image, self.rect)




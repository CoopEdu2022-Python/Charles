import pygame


class Dinosaur(pygame.sprite.Sprite):
    def __init__(self, images, screen_size):
        pygame.sprite.Sprite.__init__(self)

        self.x, self.y = screen_size[0], screen_size[1]
        """
        start = images[0]
        jump = images[1]
        run_1 = images[2]
        run_2 = images[3]
        duck_1 = images[4]
        duck_2 = images[5]
        die_1_white_edge = images[6]
        die_2 = images[7]
        unknown = images[8]
        """
        self.images = images
        self.image = self.images[0]  # start position for the dinosaur
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.bottom = (0.06 * self.x, self.y)
        self.mask = pygame.mask.from_surface(self.image)
        self.status = 2

        self.refresh_rate = 5
        self.refresh_counter = 0

    def jump(self):
        self.status = 1

    def duck(self):
        self.status = 4

    def unduck(self):
        self.status = 2

    def refresh(self):
        if self.status == 1:  # only show one picture when dino jump
            self.image = self.images[self.status]
            pass
        elif self.image == self.images[self.status]:
            self.image = self.images[self.status + 1]
        else:
            self.image = self.images[self.status]
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        g = 9.8
        t = 0
        if self.status == 2 or 4:  # run
            if self.refresh_counter == self.refresh_rate:
                self.refresh()
                self.refresh_counter = 0
            self.refresh_counter += 1
        elif self.status == 1:  # jump
            self.rect.bottom = self.y + (9.8 * t - 1 / 2 * g * (t ** 2))
            if t < 2:
                t += 0.1
            elif t == 2:
                self.status = 2
            self.refresh()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def die(self, DIN):
        if DIN == "day":
            self.status = 6
        else:
            self.status = 7

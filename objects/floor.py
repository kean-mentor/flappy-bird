import pygame

import assets
import configs
from layer import Layer


class Floor(pygame.sprite.Sprite):
    def __init__(self, index, *groups):
        super().__init__()
        self.layer = Layer.FLOOR
        self.add(*groups)

        self.image = assets.get_sprite("floor")
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(
            bottomleft=(index * configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT)
        )

    def update(self):
        self.rect.x -= 2
        if self.rect.right <= 0:
            self.rect.x = configs.SCREEN_WIDTH

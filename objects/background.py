import pygame

import assets
import configs
from layer import Layer


class Background(pygame.sprite.Sprite):
    def __init__(self, index, *groups):
        super().__init__()
        self.layer = Layer.BACKGROUND
        self.add(*groups)

        self.image = assets.get_sprite("background")
        self.rect = self.image.get_rect(topleft=(index * configs.SCREEN_WIDTH, 0))

    def update(self):
        self.rect.x -= 1
        if self.rect.right <= 0:
            self.rect.x = configs.SCREEN_WIDTH

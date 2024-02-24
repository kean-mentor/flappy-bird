import pygame

import assets
import configs
from layer import Layer


class GameStartMessage(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__()
        self.layer = Layer.UI
        self.add(*groups)

        self.image = assets.get_sprite("message")
        self.rect = self.image.get_rect(
            center=(configs.SCREEN_WIDTH / 2, configs.SCREEN_HEIGHT / 2)
        )

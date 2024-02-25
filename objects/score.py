import pygame

import assets
import configs
from layer import Layer


class Score(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__()
        self.layer = Layer.UI
        self.add(*groups)
        self.value = -1
        self.last_value = self.value

        self.sprites = [assets.get_sprite(str(i)) for i in range(10)]
        self.image = pygame.surface.Surface((0, 0), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(configs.SCREEN_WIDTH / 2, 50))

        self.number_width = self.sprites[0].get_width()
        self.number_height = self.sprites[0].get_height()
        self.number_gap = 1

    def increase_score(self, increment=1):
        self.value += increment

    def update(self):
        # Don't update it `config.FPS` times per second, update only when score is changed
        if self.value != self.last_value:
            self.last_value = self.value

            digits = len(str(self.value))
            width = digits * self.number_width + (digits - 1) * self.number_gap
            self.image = pygame.surface.Surface((width, self.number_height), pygame.SRCALPHA)

            pos_x = 0
            for idx, number in enumerate(str(self.value)):
                number_sprite = self.sprites[int(number)]
                self.image.blit(number_sprite, (pos_x + idx * self.number_gap, 0))
                self.rect = self.image.get_rect(center=(configs.SCREEN_WIDTH / 2, 50))
                pos_x += number_sprite.get_width()

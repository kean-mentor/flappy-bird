import random

import pygame

import assets
import configs
from layer import Layer


class Column(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__()
        self.layer = Layer.COLUMN
        self.add(*groups)

        self.gap = configs.GAP
        self.sprite = assets.get_sprite("pipe-green")
        self.sprite_rect = self.sprite.get_rect()

        self.pipe_top = pygame.transform.flip(self.sprite, False, True)
        self.pipe_top_rect = self.sprite.get_rect(topleft=(0, 0))

        self.pipe_bottom = self.sprite
        self.pipe_bottom_rect = self.sprite.get_rect(
            topleft=(0, self.sprite_rect.height + self.gap)
        )

        min_y = 100
        max_y = 300
        self.image = pygame.surface.Surface(
            (self.sprite_rect.width, 2 * self.sprite_rect.height + self.gap), pygame.SRCALPHA
        )
        self.image.blit(self.pipe_top, self.pipe_top_rect)
        self.image.blit(self.pipe_bottom, self.pipe_bottom_rect)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(
            midleft=(configs.SCREEN_WIDTH, random.uniform(min_y, max_y))
        )

        self.is_passed = False

    def update(self):
        self.rect.x -= 2
        if self.rect.right <= 0:
            self.kill()

    def check_passed(self) -> bool:
        if self.rect.right < configs.BIRD_POS + 1 and not self.is_passed:
            self.is_passed = True
            return True
        return False

import pygame.sprite

import assets
import configs
from layer import Layer
from objects.column import Column
from objects.floor import Floor


class Bird(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__()
        self.layer = Layer.PLAYER
        self.add(*groups)

        self.last_update = 0
        self.images = [
            assets.get_sprite("redbird-downflap"),
            assets.get_sprite("redbird-midflap"),
            assets.get_sprite("redbird-upflap"),
        ]
        self.mask = pygame.mask.from_surface(self.images[1])
        self.frame_index = 0
        self.delta_y = 0

        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect(topleft=(-50, 0))

    def update(self):
        self._calculate_frame_index()
        self.image = self.images[self.frame_index]

        self.delta_y += configs.GRAVITY
        self.rect.y += self.delta_y

        if self.rect.x < configs.BIRD_POS:
            self.rect.x += 3

        if self.rect.top <= 0:
            self.rect.top = 0

    def flap(self, event):
        self.delta_y = 0
        self.delta_y -= 6
        assets.play_sound("wing")

    def _calculate_frame_index(self):
        if pygame.time.get_ticks() - self.last_update > 40:
            self.frame_index += 1
            if self.frame_index >= len(self.images):
                self.frame_index = 0
            self.last_update = pygame.time.get_ticks()

    def check_collision(self, sprites):
        for sprite in sprites:
            if isinstance(sprite, (Column, Floor)) and pygame.sprite.collide_mask(self, sprite):
                return True
        return False

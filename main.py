import pygame

import assets
import configs
from objects.background import Background
from objects.bird import Bird
from objects.column import Column
from objects.floor import Floor

pygame.init()
screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))
clock = pygame.time.Clock()
CREATE_COLUMN = pygame.USEREVENT + 1
running = True

assets.load_sprites()

sprites = pygame.sprite.LayeredUpdates()

Background(0, sprites)
Background(1, sprites)

Floor(0, sprites)
Floor(1, sprites)

bird = Bird(sprites)

pygame.time.set_timer(CREATE_COLUMN, 2000)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == CREATE_COLUMN:
            Column(sprites)

        bird.handle_events(event)

    sprites.draw(screen)
    sprites.update()

    pygame.display.flip()
    clock.tick(configs.FPS)

pygame.quit()
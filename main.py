import pygame

import assets
import configs
from objects.background import Background
from objects.bird import Bird
from objects.column import Column
from objects.floor import Floor
from objects.game_start_message import GameStartMessage

pygame.init()
screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))
clock = pygame.time.Clock()
CREATE_COLUMN = pygame.USEREVENT + 1
running = True
game_stared = False
game_over = False
score = 0

assets.load_sprites()

sprites = pygame.sprite.LayeredUpdates()

Background(0, sprites)
Background(1, sprites)

Floor(0, sprites)
Floor(1, sprites)

bird = Bird(sprites)

game_start_message = GameStartMessage(sprites)

pygame.time.set_timer(CREATE_COLUMN, 2000)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == CREATE_COLUMN and game_stared:
            Column(sprites)
        if (
            event.type == pygame.KEYDOWN
            and event.key == pygame.K_SPACE
            or event.type == pygame.MOUSEBUTTONDOWN
        ):
            if not game_stared:
                game_stared = True
                game_start_message.kill()
            bird.flap(event)

    sprites.draw(screen)
    if game_stared and not game_over:
        sprites.update()

        for sprite in sprites:
            if isinstance(sprite, Column) and sprite.check_passed():
                score += 1

        if bird.check_collision(sprites):
            game_over = True
            print(f"Score: {score}")

    pygame.display.flip()
    clock.tick(configs.FPS)

pygame.quit()

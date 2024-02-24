import pygame

import assets
import configs
from objects.background import Background
from objects.bird import Bird
from objects.column import Column
from objects.floor import Floor
from objects.game_over_message import GameOverMessage
from objects.game_start_message import GameStartMessage

pygame.init()
pygame.display.set_caption("Droppy Bird!")
screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))
clock = pygame.time.Clock()
CREATE_COLUMN = pygame.USEREVENT + 1
running = True  # Main loop is running
game_stared = False  # Bird is flying
game_over = False  # Bird hits a column or floor -> show game over screen
score = 0

assets.load_sprites()
sprites = pygame.sprite.LayeredUpdates()


def create_sprites():
    Background(0, sprites)
    Background(1, sprites)
    Floor(0, sprites)
    Floor(1, sprites)
    return Bird(sprites)


bird = create_sprites()
game_start_message = GameStartMessage(sprites)
pygame.time.set_timer(CREATE_COLUMN, 2000)

while running:
    # Process input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == CREATE_COLUMN and game_stared:
            Column(sprites)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                if not game_stared:
                    game_stared = True
                    game_start_message.kill()
                else:
                    bird.flap(event)

            if event.key == pygame.K_ESCAPE:  # Reset game
                for sprite in sprites:
                    sprite.kill()

                game_over = False
                bird = create_sprites()
                game_stared = True

    # Update (if needed)
    if game_stared:
        sprites.update()

        for sprite in sprites:
            if isinstance(sprite, Column) and sprite.check_passed():
                score += 1

        if bird.check_collision(sprites):
            game_over = True
            game_stared = False
            GameOverMessage(sprites)
            print(f"Score: {score}")
            score = 0

    # Render
    sprites.draw(screen)
    pygame.display.flip()

    clock.tick(configs.FPS)

pygame.quit()

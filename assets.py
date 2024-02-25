import os

import pygame

sprites = {}
audios = {}


def load_sprites():
    print("loading sprites")
    path = os.path.join("assets", "sprites")
    for file in os.listdir(path):
        sprites[file.split(".")[0]] = pygame.image.load(os.path.join(path, file)).convert_alpha()


def get_sprite(name):
    return sprites[name]


def load_sounds():
    path = os.path.join("assets", "audios")
    for file in os.listdir(path):
        audios[file.split(".")[0]] = pygame.mixer.Sound(os.path.join(path, file))


def play_sound(name):
    audios[name].play()

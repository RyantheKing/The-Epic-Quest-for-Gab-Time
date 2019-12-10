import pygame
from sprites import *
from sprites import *

def checkKeys(sprite_names):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        sprite_names["player"].image = Player.image["left"]
        sprite_names["player"].rect.x -= Player.info["velocity"]

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        sprite_names["player"].image = Player.image["right"]
        sprite_names["player"].rect.x += Player.info["velocity"]

    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        sprite_names["player"].rect.y += Player.info["velocity"]
        
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        sprite_names["player"].rect.y -= Player.info["velocity"]

def checkAll(sprite_names):
    checkKeys()

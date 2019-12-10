# Initializing pygame + some important variables 

import pygame
import events
from display import *
from sprites import *
from colors import *

pygame.init()

# Launching the window, setting it to the dimensions of the `display` dictionary.

win = pygame.display.set_mode((display["width"], display["height"]))

all_sprites_list = pygame.sprite.Group()

# use "player" when referring to the sprite
# use "Player" when referring to sprite details
player = Player()
player.image = Player.image["right"]
all_sprites_list.add(player)

sprite_names = {
    "player": player,
}

# The Main game loop
while True:
    pygame.time.delay(30)
    win.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

    #all_sprites_list.update()

    events.checkKeys(sprite_names)
        
    all_sprites_list.draw(win)
    pygame.display.update()

pygame.quit()

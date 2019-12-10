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

background = pygame.image.load("background.png").convert() #background image
background = pygame.transform.scale(background, (display["width"], display['height'])) #scaling up to display size

sprite_names = {
    "player": player,
}

# The Main game loop
while True:
    pygame.time.delay(33) #30 fps lock
    win.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
    win.blit(background, [0, 0]) #display background
    #all_sprites_list.update()

    events.checkKeys(sprite_names)
        
    all_sprites_list.draw(win)
    pygame.display.update()

pygame.quit()

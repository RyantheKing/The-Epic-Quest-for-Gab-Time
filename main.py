# Initializing pygame + some important variables 

import pygame
import math

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

class Player(pygame.sprite.Sprite):
    """
    This class represents the player
    It derives from the "Sprite" class in Pygame
    """
    info = {
        "y": 200,
        "x": 200,
        "velocity": 5,
        "width": 10,
        "height": 27
    }

    image = {
        "up": None,
        "down": None,
        "left": None,
        "right": None,
    }

    def __init__(self):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
        # Call the parent class (Sprite) constructor
        super().__init__()
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        Player.image["right"] = pygame.image.load("sprites/player_right.png").convert()
        Player.image["right"].set_colorkey(BLACK)
        Player.image["right"] = pygame.transform.scale(Player.image["right"], (scale*Player.info["width"], scale*Player.info["height"]))

        Player.image["left"] = pygame.image.load("sprites/player_left.png").convert()
        Player.image["left"].set_colorkey(BLACK)
        Player.image["left"] = pygame.transform.scale(Player.image["left"], (scale*Player.info["width"], scale*Player.info["height"]))

        self.rect = Player.image["right"].get_rect()
        self.rect.y = 300
        self.rect.x = 400
        self.image = Player.image["right"]

pygame.init()

display = {
    "width": 800,
    "height": 600,
    "gwidth": 256,
    "gheight": 192
}
scale = math.floor(display["width"]/display["gwidth"])

# Launching the window, setting it to the dimensions of the `display` dictionary.

win = pygame.display.set_mode((display["width"], display["height"]))

all_sprites_list = pygame.sprite.Group()

# use "player" when referring to the sprite
# use "Player" when referring to sprite details
player = Player()
player.image = Player.image["right"]
all_sprites_list.add(player)

# The Main game loop
while True:
    pygame.time.delay(30)
    win.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

    #all_sprites_list.update()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.image = Player.image["left"]
        player.rect.x -= Player.info["velocity"]

    if keys[pygame.K_RIGHT]:
        player.image = Player.image["right"]
        player.rect.x += Player.info["velocity"]

    if keys[pygame.K_DOWN]:
        player.rect.y += Player.info["velocity"]
        

    if keys[pygame.K_UP]:
        player.rect.y -= Player.info["velocity"]
        
    all_sprites_list.draw(win)
    
    pygame.display.update()

pygame.quit()

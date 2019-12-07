# Initializing pygame + some important variables 

import pygame
import random
import math

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

class Block(pygame.sprite.Sprite):
    """
    This class represents the ball
    It derives from the "Sprite" class in Pygame
    """
    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.image.load("sprites/player.png").convert()
        self.image.set_colorkey(BLACK)
        self.image = pygame.transform.scale(self.image, (width, height))

        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
 
    def update(self):
        """ Called each frame. """
 
        # If block is too far down, reset to top of screen.
           # Move block down one pixel
 
        # If block is too far down, reset to top of screen.
    

class Player(Block):
    """ The player class derives from Block, but overrides the 'update'
    functionality with new a movement function that will move the block
    with the mouse. """
    def update(self):
        # Get the current mouse position. This returns the position
        # as a list of two numbers.
 
        # Fetch the x and y out of the list,
        # just like we'd fetch letters out of a string.
        # Set the player object to the mouse location
        self.rect.y = character["y"]
        self.rect.x = character["x"]

pygame.init()

score = 0
total = 0

myfont = pygame.font.SysFont('monospace', 50)

# Making dictionaries with settings for everything.

display = {
    "width": 800,
    "height": 600,
    "gwidth": 256,
    "gheight": 192
}

scale = math.floor(display["width"]/display["gwidth"])

character = {
    "y": 450,
    "x": 800,
    "velocity": 5,
    "size": 10
}

# Launching the window, setting it to the dimensions of the `display` dictionary.

win = pygame.display.set_mode((display["width"], display["height"]))

block_list = pygame.sprite.Group()

all_sprites_list = pygame.sprite.Group()

block = Block(BLACK, 10*scale, 27*scale)
block.rect.y = 200
block.rect.x = 200

block_list.add(block)
all_sprites_list.add(block)

player = Player(WHITE, 20, 15)
all_sprites_list.add(player)

# The Main game loop

while True:
    pygame.time.delay(30)
    win.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

    all_sprites_list.update()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        block.rect.x -= character["velocity"]

    if keys[pygame.K_RIGHT]:
        block.rect.x += character["velocity"]

    if keys[pygame.K_DOWN]:
        block.rect.y += character["velocity"]
        

    if keys[pygame.K_UP]:
        block.rect.y -= character["velocity"]
        

    all_sprites_list.draw(win)
    textsurface = myfont.render("score: {0}/{1}".format(score, total), False, (0, 0, 0))
    win.blit(textsurface, (10, 10))
    
    pygame.display.update()

pygame.quit()

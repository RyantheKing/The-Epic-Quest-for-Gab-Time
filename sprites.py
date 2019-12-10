import pygame
from display import *
from colors import *

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
        Player.image["right"] = pygame.transform.scale(Player.image["right"], (display["scale"]*Player.info["width"], display["scale"]*Player.info["height"]))

        Player.image["left"] = pygame.image.load("sprites/player_left.png").convert()
        Player.image["left"].set_colorkey(BLACK)
        Player.image["left"] = pygame.transform.scale(Player.image["left"], (display["scale"]*Player.info["width"], display["scale"]*Player.info["height"]))

        self.rect = Player.image["right"].get_rect()
        self.rect.y = 300
        self.rect.x = 400
        self.image = Player.image["right"]

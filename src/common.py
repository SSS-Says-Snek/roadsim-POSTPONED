"""
Some common variables used many times throughout the game code
=============================  U S A G E  =============================
>>> from src.common import *
>>> # Use the variables here
"""

__version__ = "-5.0.0"

import pygame
from pathlib import Path

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = (800, 600)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

TITLE = "Roadsim"

PATH = Path('.')
FONT_PATH = PATH / "src/Assets/Fonts"

node_size = 10
rows = 800 // node_size
cols = 600 // node_size

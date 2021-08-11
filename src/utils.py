import pygame

from functools import lru_cache
from src import common


@lru_cache(1000)
def load_font(size, text_font="ThaleahFat"):
    """Loads a font with a given size and an optional parameter for the font name"""
    return pygame.font.Font(common.FONT_PATH / f"{text_font}.ttf", size)


def pos_to_tile_coord(pos):
    y, x = pos
    return y // common.node_size, x // common.node_size

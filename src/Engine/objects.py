import enum
import pygame
import warnings
from src import common


class NoneTypeWarning(Warning):
    pass


class NodeType(enum.Enum):
    EMPTY = (255, 255, 255)
    ROAD = (20, 20, 20)

    def nodetype_str_to_nodetype(nodestr):
        conversion_dict = {
            "Road": NodeType.ROAD
        }

        if conversion_dict.get(nodestr, None) is None:
            warnings.warn(
                NoneTypeWarning(
                    f"Node string \"{nodestr}\" not found in conversion dict, returning None..."
                )
            )
        return conversion_dict.get(nodestr, None)


class Node:
    def __init__(self, row, col, width, total_rows, total_cols, screen=common.SCREEN):
        self.row = row
        self.col = col
        self.width = width
        self.x = self.row * width
        self.y = self.col * width

        self.total_rows = total_rows
        self.total_cols = total_cols

        self.type = NodeType.EMPTY
        self.extra_content = None

        self.screen = screen

    def draw(self, surf=None):
        pygame.draw.rect(surf or self.screen, self.type.value, [self.x, self.y, self.width, self.width])


class GameData:
    game_state = None

game_data = GameData()

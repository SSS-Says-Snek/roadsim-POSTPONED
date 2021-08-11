import enum
import pygame
from src import common


class NodeType(enum.Enum):
    EMPTY = (255, 255, 255)
    ROAD = (20, 20, 20)


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

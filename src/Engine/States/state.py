"""
This file contains all state machines used in the game.
Basically, state machines allow us to easily transition from "state" to "state", like from
    a Main Menu to a Settings state
This is mainly used in game.py, though of course, there are exceptions
    (E.g wanting to access a state attribute in a different file)
The basic structure of state machines is:
    - XState.draw()
    - XState.handle_events(event) (Don't ask why it's with an s)
    - XState.constant_run() (Optional, but highly recommended)

=============================  U S A G E  =============================
>>> from src.Engine.States.state import *
>>> MenuState().draw()
"""
import functools

import pygame

from src import common
from src.Engine.objects import Node
from src.Engine.base import BaseState, DummyState


class MenuState(DummyState):
    pass


class GameState(BaseState):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.grid = self.make_grid(common.rows, common.cols)

    def draw(self):
        surf_to_blit = self.draw_grid()
        self.screen.blit(surf_to_blit, (0, 0))

    def handle_events(self, event):
        pass

    @staticmethod
    def make_grid(rows, cols):
        grid = []

        for i in range(rows):
            grid.append([])
            for j in range(cols):
                spot = Node(i, j, common.node_size, rows, cols)
                grid[i].append(spot)

        return grid

    @functools.lru_cache(100)
    def draw_grid(self):
        surf_to_draw = pygame.Surface((int(common.WIDTH), int(common.HEIGHT)))
        surf_to_draw.fill((245, 245, 245))
        for i in range(common.rows):
            # pygame.draw.line(surf_to_draw, (128, 128, 128), (0, i * common.node_size), (common.WIDTH, i * common.node_size))

            for j in range(common.cols):
                # pygame.draw.line(surf_to_draw, (128, 128, 128), (j * common.node_size, 0), (j * common.node_size, common.WIDTH))
                pygame.draw.rect(surf_to_draw, (128, 128, 128), [i * common.node_size, j * common.node_size, common.node_size, common.node_size], 1)
                self.grid[i][j].draw(surf_to_draw)
        return surf_to_draw
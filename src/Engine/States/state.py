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

from src import common, utils
from src.Engine.Reusable.dropdowns import DropDown
from src.Engine.objects import Node, NodeType
from src.Engine.base import BaseState, DummyState


class MenuState(DummyState):
    pass


class GameState(BaseState):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.grid = self.make_grid(common.rows, common.cols)

        self.nodetype_select = DropDown((common.GRID_WIDTH + 10, 10), 150, 40, ["Test"], (128, 128, 128),
                                        "Road", 19, (0, 0, 0), (128, 128, 128), (140, 140, 140), (150, 150, 150),
                                        (100, 100, 100), 5)
        self.nodetype_select.bind_on_selection(self.on_nodetype_select_selection)
        self.node_to_draw = NodeType.ROAD

    def draw(self):
        surf_to_blit = self.draw_grid()
        self.screen.blit(surf_to_blit, (0, 0))

        self.nodetype_select.draw()

    def handle_events(self, event):
        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] and 0 < mouse_pos[0] < common.GRID_WIDTH and 0 < mouse_pos[1] < common.GRID_HEIGHT:
            tile_coord = utils.pos_to_tile_coord(pygame.mouse.get_pos())
            print(tile_coord)
            self.grid[tile_coord[0]][tile_coord[1]].type = self.node_to_draw

        self.nodetype_select.handle_event(event)

    @staticmethod
    def make_grid(rows, cols):
        grid = []

        for i in range(rows):
            grid.append([])
            for j in range(cols):
                spot = Node(i, j, common.node_size, rows, cols)
                grid[i].append(spot)

        return grid

    # @functools.lru_cache(100)
    def draw_grid(self):
        surf_to_draw = pygame.Surface((int(common.GRID_WIDTH), int(common.GRID_HEIGHT)))

        for i in range(common.rows):
            for j in range(common.cols):
                self.grid[i][j].draw(surf_to_draw)
                pygame.draw.rect(surf_to_draw, (128, 128, 128), [i * common.node_size, j * common.node_size, common.node_size, common.node_size], 1)

        return surf_to_draw

    def on_nodetype_select_selection(self):
        node_got = NodeType.nodetype_str_to_nodetype(self.nodetype_select.get_selected_text())
        self.node_to_draw = node_got

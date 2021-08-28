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
# import functools

import pygame

from src import common, utils
from src.Engine.Reusable.button import Button
from src.Engine.States.sidebars import DefaultSidebar, NodeInfoSidebar
from src.Engine.objects import Node, NodeType, game_data
from src.Engine.base import BaseState, DummyState


class MenuState(DummyState):
    pass


class GameState(BaseState):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.grid = self.make_grid(common.rows, common.cols)

        self.node_to_draw = NodeType.ROAD

        game_data.game_state = self
        self.sidebar = DefaultSidebar()

        self.settings_button = Button(common.SCREEN, (common.TOTAL_WIDTH - 50, 10, 40, 40), None,
                                      (128, 128, 128), "Settings", (0, 0, 0), 10, True, (100, 100, 100), 3, (150, 150, 150),
                                      False)

    def draw(self):
        surf_to_blit = self.draw_grid()
        self.screen.blit(surf_to_blit, (0, 0))

        self.sidebar.draw()
        self.settings_button.draw()

    def handle_events(self, event):
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed(3)[2]:
                tile_coord = utils.pos_to_tile_coord(pygame.mouse.get_pos())
                self.sidebar.change_sidebar(NodeInfoSidebar, self.grid[tile_coord[0]][tile_coord[1]], node_pos=tile_coord)

        if pygame.mouse.get_pressed(3)[0] and (0 < mouse_pos[0] < common.GRID_WIDTH and
                                               0 < mouse_pos[1] < common.GRID_HEIGHT):
            tile_coord = utils.pos_to_tile_coord(pygame.mouse.get_pos())
            print(tile_coord)
            self.grid[tile_coord[0]][tile_coord[1]].type = self.node_to_draw

        self.sidebar.handle_events(event)
        self.settings_button.handle_event(event)

    def constant_run(self):
        if self.sidebar.__class__ != self.sidebar.next_sidebar[0]:
            args = self.sidebar.next_sidebar[1] or {}
            kwargs = self.sidebar.next_sidebar[2] or {}
            self.sidebar = self.sidebar.next_sidebar[0](common.SCREEN, *args, **kwargs)

    @staticmethod
    def make_grid(rows, cols):
        grid = []

        for i in range(rows):
            grid.append([])
            for j in range(cols):
                spot = Node(i, j, common.node_size, rows, cols)
                grid[i].append(spot)

        return grid

    def draw_grid(self):
        surf_to_draw = pygame.Surface((int(common.GRID_WIDTH), int(common.GRID_HEIGHT)))  # lgtm [py/call/wrong-arguments]

        for i in range(common.rows):
            for j in range(common.cols):
                self.grid[i][j].draw(surf_to_draw)
                pygame.draw.rect(
                    surf_to_draw, (
                        128, 128, 128
                    ), [
                        i * common.node_size,
                        j * common.node_size,
                        common.node_size,
                        common.node_size
                    ], 1
                )

        return surf_to_draw

    def on_nodetype_select_selection(self):
        node_got = NodeType.nodetype_str_to_nodetype(self.sidebar.nodetype_select.get_selected_text())
        self.node_to_draw = node_got

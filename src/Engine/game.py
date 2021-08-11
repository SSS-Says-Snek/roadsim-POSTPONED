"""
This file stores the actual game class, used to run the game in main.py
=============================  U S A G E  =============================
>>> from src.Engine.game import GameLoop
>>> game_loop = GameLoop()
>>> game_loop.run()

Note that GameLoop should ONLY be run inside main.py, and no where else. I just wanna make main.py look cool
Cool as in, "My main.py has only 4 lines of code."
"""
import sys
import pygame

from src import common
from src import utils
from src.Engine.States.state import GameState
from src.Engine.Reusable.dropdowns import *


class GameLoop:
    def __init__(self, screen=common.SCREEN):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.font = utils.load_font(60)
        self.running = True

        self.state = GameState(self)
        self.fps_setting = 60

        self.test = DropDown((200, 200), 250, 50, ["Sus Chungus", "AEAEAEAEAEAE", "Potat Sus"], (128, 128, 128), "Sussus Amogus", 24, (0, 0, 0), hover_color=(150, 150, 150),
                             border_color=(100, 100, 100), border_width=3, selection_rect_hover_color=(140, 140, 140))

        pygame.display.set_caption(common.TITLE)

    def run(self):
        while self.running:
            self.screen.fill((245, 245, 245))

            # Handles state methods
            self.state.constant_run()
            self.handle_events()
            self.state.draw()

            self.screen.blit(utils.load_font(30).render(f"FPS: {round(self.clock.get_fps(), 1)}", True, (0, 0, 0)), (0, 0))

            # self.test.draw()

            pygame.display.update()

            self.clock.tick(60)

        pygame.quit()
        sys.exit()

    def handle_events(self):
        """Function used to handle the game loop's events"""
        for game_event in pygame.event.get():
            # Handle state events
            self.state.handle_events(game_event)

            if game_event.type == pygame.QUIT:
                self.running = False
            # self.test.handle_event(game_event)

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


class GameLoop:
    def __init__(self, screen=common.SCREEN):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.font = utils.load_font(60)
        self.running = True

        self.state = GameState(self)
        self.fps_setting = 60

        pygame.display.set_caption(common.TITLE)

    def run(self):
        while self.running:
            dt = self.clock.tick(self.fps_setting) / 1000

            self.screen.fill((245, 245, 245))

            # Handles state methods
            self.state.constant_run()
            self.handle_events()
            self.state.draw()

            pygame.display.update()

        pygame.quit()
        sys.exit()

    def handle_events(self):
        """Function used to handle the game loop's events"""
        for game_event in pygame.event.get():
            # Handle state events
            self.state.handle_events(game_event)

            if game_event.type == pygame.QUIT:
                self.running = False

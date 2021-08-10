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

import pygame

from src import common
from src.Engine.base import BaseState, DummyState


class MenuState(DummyState):
    pass


class GameState(DummyState):
    pass

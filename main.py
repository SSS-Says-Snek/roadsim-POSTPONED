"""
===================================================================================
|                   R O A D   S I M U L A T O R  (v-5.0.0)                        |
|       a "game" that simulates roads and traffic networks with pathfinding       |
|                 algorithms like A*, Breadth First, and more                     |
|                                                                                 |
| ++-=========================================================================-++ |
|                           I N F O R M A T I O N                                 |
|                                                                                 |
|                    Date created: 8/9/2021, at 8:11 PM                           |
|                                                                                 |
===================================================================================
"""
from src.Engine.game import GameLoop

if __name__ == "__main__":
    game_loop = GameLoop()
    game_loop.run()

from src import common
from src.Engine.Reusable.dropdowns import DropDown
from src.Engine.objects import game_data


class DefaultSideBar:
    def __init__(self, screen=common.SCREEN):
        self.screen = screen

        self.nodetype_select = DropDown((common.GRID_WIDTH + 10, 10), 150, 40, ["Test"], (128, 128, 128),
                                        "Road", 19, (0, 0, 0), (128, 128, 128), (140, 140, 140), (150, 150, 150),
                                        (100, 100, 100), 5)
        self.nodetype_select.bind_on_selection(game_data.game_state.on_nodetype_select_selection)

    def handle_events(self, event):
        self.nodetype_select.handle_event(event)

    def draw(self):
        self.nodetype_select.draw()

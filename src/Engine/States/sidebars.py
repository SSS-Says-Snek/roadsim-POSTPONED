from src import common, utils
from src.Engine.Reusable.button import Button
from src.Engine.Reusable.dropdowns import DropDown
from src.Engine.objects import game_data
from src.Engine.base import BaseSidebar


class DefaultSidebar(BaseSidebar):
    def __init__(self, screen=common.SCREEN):
        super().__init__(screen)

        self.nodetype_select = DropDown((common.GRID_WIDTH + 10, 80), 150, 40, ["Test", "Worn Down Road"], (128, 128, 128),
                                        "Road", 19, (0, 0, 0), (128, 128, 128), (140, 140, 140), (150, 150, 150),
                                        (100, 100, 100), 5)
        self.nodetype_select.bind_on_selection(game_data.game_state.on_nodetype_select_selection)

    def handle_events(self, event):
        self.nodetype_select.handle_event(event)

    def draw(self):
        self.nodetype_select.draw()


class NodeInfoSidebar(BaseSidebar):
    def __init__(self, screen=common.SCREEN, *args, **kwargs):
        super().__init__(screen)

        if 'node_pos' in kwargs:
            self.node_pos = kwargs['node_pos']
        self.node = args[0]

        self.exit_button = Button(
            self.screen, (common.GRID_WIDTH + 10, common.GRID_HEIGHT - 50, 180, 40),
            lambda: self.change_sidebar(DefaultSidebar),
            (128, 128, 128), "Exit Properties", (0, 0, 0), 15, False, (100, 100, 100), 5,
            (150, 150, 150), False
        )

    def handle_events(self, event):
        self.exit_button.handle_event(event)

    def draw(self):
        title_txt = utils.load_font(15).render(f"Properties of Node {self.node_pos}:", True, (0, 0, 0))
        self.screen.blit(
            title_txt, (common.GRID_WIDTH + 10, 80)
        )

        traffic_txt = utils.load_font(20).render(
            f"Traffic: {f'None' if self.node.properties['traffic'] is None else ''}",
            True, (0, 0, 0)
        )
        self.screen.blit(
            traffic_txt, (common.GRID_WIDTH + 10, 120)
        )

        type_txt = utils.load_font(20).render(
            f"Node Type: {self.node.type.name.replace('_', ' ')}",
            True, (0, 0, 0)
        )
        self.screen.blit(
            type_txt, (common.GRID_WIDTH + 10, 150)
        )

        self.exit_button.draw()

import pygame
from src import common, utils


class Slider:
    # pylint: disable=too-many-instance-attributes
    # Well, whaddya expect, there needs to be a lot to customize the slider

    def __init__(
        self,
        coord,
        color,
        length,
        width,
        min_val,
        max_val,
        default_val=None,
        screen=common.SCREEN,
        num_spaces=-1,
        slide_color=None,
        show_value=True,
    ):
        self.coord = coord
        self.color = color
        self.length = length
        self.width = width
        self.min_val = min_val
        self.max_val = max_val
        self.screen = screen
        self.num_spaces = num_spaces
        self.show_value = show_value

        if default_val is None:
            self.default_val = self.min_val
        else:
            self.default_val = default_val

        if slide_color is None:
            self.slide_color = self.color
        else:
            self.slide_color = slide_color
        self.rect_coord = self.coord + (
            self.length,
            self.width,
        )
        self.rect = pygame.Rect(self.rect_coord)
        self.font = utils.load_font(self.width)
        self.is_holding_mouse = False
        self.slide_coord = (
            self.coord[0]
            + (self.default_val - self.min_val) / self.max_val * self.length,
            self.coord[1] - width // 2,
        )
        self.current_val = self.default_val

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.rect(self.screen, self.color, self.rect_coord)
        min_val_txt = self.font.render(str(self.min_val), True, (0, 0, 0))
        min_val_txt_rect = min_val_txt.get_rect(
            topright=(self.coord[0] - (self.length // 30), self.coord[1])
        )
        self.screen.blit(min_val_txt, min_val_txt_rect)

        max_val_txt = self.font.render(str(self.max_val), True, (0, 0, 0))
        self.screen.blit(
            max_val_txt,
            (self.coord[0] + self.length + self.length // 30, self.coord[1]),
        )

        current_rect = pygame.draw.rect(
            self.screen, self.slide_color, self.slide_coord + (20, self.width * 2)
        )
        if self.show_value:
            current_val_txt = self.font.render(str(self.current_val), True, (0, 0, 0))
            current_val_txt_rect = current_val_txt.get_rect(
                center=(current_rect.midbottom[0], current_rect.centery - self.width)
            )
            self.screen.blit(current_val_txt, current_val_txt_rect)
        if (
            self.is_holding_mouse
            and self.coord[0] <= mouse_pos[0] <= self.coord[0] + self.length
        ):
            # if self.is_holding_mouse and distance(mouse_pos[0], current_rect.centerx, mouse_pos[1], current_rect.centery) < 100:
            self.slide_coord = (mouse_pos[0], self.slide_coord[1])
            self.current_val = (
                mouse_pos[0] - self.coord[0]
            ) / self.length * self.max_val + self.default_val
            if self.current_val > self.max_val:
                self.current_val = self.max_val
            self.current_val = round(self.current_val)

    def handle_events(self, event):
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(mouse_pos):
            self.is_holding_mouse = True
        if event.type == pygame.MOUSEBUTTONUP:
            self.is_holding_mouse = False

    def get_slide_value(self):
        return self.current_val

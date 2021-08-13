import pygame
from src import common, utils

pygame.init()


class DropDown:
    def __init__(self, pos, width, height, items, rect_color, default_text, font_size, font_color,
                 selection_rect_color=None, selection_rect_hover_color=None,
                 hover_color=None, border_color=None, border_width=None, screen=common.SCREEN):
        self.pos = pos
        self.width = width
        self.height = height
        self.items = [default_text] + items
        self.rect_color = rect_color
        self.default_text = default_text
        self.font_size = font_size
        self.font_color = font_color
        self.hover_color = hover_color
        self.border_color = border_color
        self.border_width = border_width

        self.main_rect = pygame.Rect(self.pos[0], self.pos[1], self.width, self.height)
        self.selected_idx = 0
        self.font = utils.load_font(self.font_size)

        self.screen = screen

        self.in_selection_screen = False
        self.selection_rect = pygame.Rect(self.pos[0], self.pos[1] + self.height, self.width, self.height * (len(self.items) + 1))
        self.selection_rect_color = selection_rect_color or self.rect_color
        self.selection_rect_hover_color = selection_rect_hover_color

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.main_rect.collidepoint(event.pos) and not self.in_selection_screen:
                if not self.in_selection_screen:
                    self.in_selection_screen = True
            elif self.in_selection_screen:
                if self.selection_rect.collidepoint(event.pos):
                    idx_clicked = (event.pos[1] - self.pos[1]) // self.height - 1
                    self.selected_idx = idx_clicked
                self.in_selection_screen = False

    def draw(self, mouse_pos=None):
        mouse_pos = mouse_pos or pygame.mouse.get_pos()

        if self.hover_color and self.main_rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, self.hover_color, self.main_rect)
        else:
            pygame.draw.rect(self.screen, self.rect_color, self.main_rect)

        if self.border_color is not None and self.border_width is not None:
            pygame.draw.rect(
                self.screen, self.border_color, self.main_rect, width=self.border_width
            )

        if self.selected_idx or self.default_text:
            txt = self.font.render(self.items[self.selected_idx] or self.default_text, True, self.font_color)
            txt_pos = txt.get_rect(midleft=(self.pos[0] + self.width // 60, self.pos[1] + self.height // 2))
            self.screen.blit(txt, txt_pos)

        if self.in_selection_screen:
            for i, text in enumerate(self.items):
                rect = pygame.Rect(self.pos[0], self.pos[1] + (i + 1) * self.height, self.width, self.height)

                if not rect.collidepoint(mouse_pos):
                    pygame.draw.rect(self.screen, self.selection_rect_color, rect)
                else:
                    pygame.draw.rect(self.screen, self.selection_rect_hover_color, rect)

                sel_txt = self.font.render(text, True, self.font_color)
                sel_txt_pos = sel_txt.get_rect(
                    midleft=(
                        self.pos[0] + self.width // 60,
                        self.pos[1] + (i + 1) * self.height + self.height // 2
                    )
                )

                self.screen.blit(sel_txt, sel_txt_pos)
            if self.border_color is not None and self.border_width is not None:
                pygame.draw.line(
                    self.screen, self.border_color, (
                        self.pos[0],
                        self.pos[1] + self.height
                    ),
                    (
                        self.pos[0],
                        self.pos[1] + (i + 2) * self.height
                    ), width=self.border_width
                )
                pygame.draw.line(
                    self.screen, self.border_color, (
                        self.pos[0],
                        self.pos[1] + (i + 2) * self.height
                    ),
                    (
                        self.pos[0] + self.width,
                        self.pos[1] + (i + 2) * self.height
                    ), width=self.border_width
                )
                pygame.draw.line(
                    self.screen, self.border_color, (
                        self.pos[0] + self.width - self.border_width // 2,
                        self.pos[1] + self.height
                    ),
                    (
                        self.pos[0] + self.width - self.border_width // 2,
                        self.pos[1] + (i + 2) * self.height
                    ),
                    width=self.border_width
                )

        if not self.in_selection_screen:
            pygame.draw.polygon(
                self.screen, (0, 0, 0), [
                    (self.pos[0] + 7 * self.width // 9, self.pos[1] + self.height // 3),
                    (self.pos[0] + 8 * self.width // 9, self.pos[1] + self.height // 3),
                    (self.pos[0] + 15 * self.width / 18, self.pos[1] + 4 * self.height // 5)
                ]
            )
        else:
            pygame.draw.polygon(
                self.screen, (0, 0, 0), [
                    (self.pos[0] + 15 * self.width // 18, self.pos[1] + self.height // 3),
                    (self.pos[0] + 7 * self.width // 9, self.pos[1] + 4 * self.height // 5),
                    (self.pos[0] + 8 * self.width // 9, self.pos[1] + 4 * self.height // 5)
                ]
            )

    def get_selected(self):
        return self.items[self.selected_idx], self.selected_idx

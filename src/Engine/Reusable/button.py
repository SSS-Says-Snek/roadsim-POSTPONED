import pygame
from src.utils import load_font


class Button:
    """Subset of Button, MenuButton adds features suitable for Menu Buttons"""

    def __init__(
            self,
            surface,
            coordinates: tuple,
            func_when_clicked,
            rect_color=(255, 255, 255),
            text=None,
            text_color=(0, 0, 0),
            font_size=None,
            rounded=False,
            border_color=None,
            border_width=None,
            hover_color=None,
            center=False
    ):
        self.screen = surface
        self.coords = coordinates
        self.rect_color = rect_color
        self.text = text
        self.text_color = text_color
        self.font_size = font_size
        self.rounded = rounded
        self.func_when_clicked = func_when_clicked
        self.border_color = border_color
        self.border_width = border_width
        self.hover_color = hover_color
        self.center = center

        self.rect = pygame.Rect(self.coords)
        if self.center:
            self.rect.center = (self.coords[0], self.coords[1])

    def draw(self, mouse_pos=None):
        """Draws the button onto previously inputted screen"""
        mouse_pos = mouse_pos or pygame.mouse.get_pos()
        if self.hover_color and self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, self.hover_color, self.rect)
        else:
            pygame.draw.rect(self.screen, self.rect_color, self.rect)

        if self.border_width and self.border_color:
            pygame.draw.rect(self.screen, self.border_color, self.rect, self.border_width)
        if self.text:
            if self.font_size is None:
                # Doesn't work but ok
                self.font_size = (
                    self.coords[3] // len(self.text)
                    if len(self.coords) == 4
                    else self.coords[1][0] // len(self.text)
                )
            font_different_size = load_font(self.font_size)
            text_surf = font_different_size.render(self.text, True, self.text_color)
            self.screen.blit(
                text_surf,
                (
                    self.rect.centerx - text_surf.get_width() // 2,
                    self.rect.centery - text_surf.get_height() // 2,
                ),
            )

    def handle_event(self, event, mouse_pos=None):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            if mouse_pos is not None:
                pos = mouse_pos
            if self.rect.collidepoint(pos):
                if self.func_when_clicked is not None:
                    self.func_when_clicked()


class ImageButton:
    def __init__(
            self,
            surface,
            image,
            coordinates: tuple,
            func_when_clicked,
            rect_color=(255, 255, 255),
            text=None,
            text_color=(0, 0, 0),
            font_size=None,
            rounded=False,
            border_color=None,
            border_width=None,
            hover_color=None,
            center=False
    ):
        self.screen = surface
        self.image = image
        self.coords = coordinates
        self.rect_color = rect_color
        self.text = text
        self.text_color = text_color
        self.font_size = font_size
        self.rounded = rounded
        self.func_when_clicked = func_when_clicked
        self.border_color = border_color
        self.border_width = border_width
        self.hover_color = hover_color
        self.center = center

        self.rect = self.image.get_rect(topleft=self.coords)

    def draw(self, mouse_pos=None):
        mouse_pos = mouse_pos or pygame.mouse.get_pos()

        self.screen.blit(self.image, self.coords)

    def handle_event(self, event, mouse_pos=None):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            if mouse_pos is not None:
                pos = mouse_pos
            if self.rect.collidepoint(pos):
                if self.func_when_clicked is not None:
                    self.func_when_clicked()

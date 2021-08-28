from src import common

import pygame

pygame.init()


class TextMessage:
    def __init__(
            self,
            pos,
            width,
            height,
            rect_color,
            text,
            font,
            font_color=(0, 0, 0),
            border_color=None,
            border_width=None,
            instant_blit=True,
            screen=common.SCREEN,
    ):
        """This class can be used to display text"""
        self.pos = pos
        self.width = width
        self.height = height
        self.rect_color = rect_color
        self.text = text
        self.font = font
        self.font_color = font_color
        self.border_color = border_color
        self.border_width = border_width
        self.instant_blit = instant_blit
        self.screen = screen

        self.text_rect = pygame.Rect(self.pos[0], self.pos[1], self.width, self.height)
        self.split_text = self.wrap_text(
            self.text, self.width - (self.border_width or 0), self.font
        )

        if not self.instant_blit:
            self.blitted_chars = ["" for _ in self.split_text]
            self.char_blit_line = 0
            self.blit_line_idx = 0
            self.prev_line_text = ""

    def draw(self):
        pygame.draw.rect(self.screen, self.rect_color, self.text_rect)

        if self.border_color is not None and self.border_width is not None:
            pygame.draw.rect(
                self.screen, self.border_color, self.text_rect, width=self.border_width
            )

        if self.instant_blit:
            for i, text in enumerate(self.split_text):
                rendered_text = self.font.render(text, True, self.font_color)
                self.screen.blit(
                    rendered_text,
                    (
                        self.pos[0] + (self.border_width or 0),
                        self.pos[1] + i * self.font.get_height(),
                    ),
                )

        else:
            self.char_blit_line += 1

            prev_text = self.split_text[self.blit_line_idx][: self.char_blit_line]
            self.blitted_chars[self.blit_line_idx] = self.split_text[
                                                         self.blit_line_idx
                                                     ][: self.char_blit_line]

            if self.blitted_chars[self.blit_line_idx] == self.prev_line_text:
                if self.blit_line_idx + 1 < len(self.split_text):
                    self.char_blit_line = 0
                    self.blit_line_idx += 1

            for i, text in enumerate(self.blitted_chars):
                rendered_text = self.font.render(text, True, self.font_color)
                self.screen.blit(
                    rendered_text,
                    (
                        self.pos[0] + (self.border_width or 0),
                        self.pos[1] + i * self.font.get_height(),
                    ),
                )

            self.prev_line_text = prev_text

    def handle_events(self, event):
        if (
                event.type == pygame.KEYDOWN
                and not self.instant_blit
                and self.blitted_chars != self.split_text
        ):
            self.blitted_chars = self.split_text[:]
            self.blit_line_idx = len(self.blitted_chars) - 1
            self.char_blit_line = len(self.blitted_chars[-1])

    def reset_current_text(self):
        """Only applies for non-instant blit textboxes"""
        self.blitted_chars = ["" for _ in self.split_text]
        self.char_blit_line = 0
        self.blit_line_idx = 0
        self.prev_line_text = ""

    @staticmethod
    def wrap_text(text, width, font):
        """Wrap text to fit inside a given width when rendered.
        :param text: The text to be wrapped.
        :param font: The font the text will be rendered in.
        :param width: The width to wrap to.
        """
        text_lines = text.replace("\t", "    ").split("\n")
        if width is None or width == 0:
            return text_lines

        wrapped_lines = []
        for line in text_lines:
            line = line.rstrip() + " "
            if line == " ":
                wrapped_lines.append(line)
                continue

            # Get the leftmost space ignoring leading whitespace
            start = len(line) - len(line.lstrip())
            start = line.index(" ", start)
            while start + 1 < len(line):
                # Get the next potential splitting point
                next_splitting_point = line.index(" ", start + 1)
                if font.size(line[:next_splitting_point])[0] <= width:
                    start = next_splitting_point
                else:
                    wrapped_lines.append(line[:start])
                    line = line[start + 1:]
                    start = line.index(" ")
            line = line[:-1]
            if line:
                wrapped_lines.append(line)
        return wrapped_lines

    @property
    def is_finished(self):
        if not self.instant_blit and self.blitted_chars != self.split_text:
            print("bruv")
            return False
        return True
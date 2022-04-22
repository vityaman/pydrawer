from typing import List

import pygame

from .figure.value import Color, Point
from .figure import Circle, Rectangle
from .draw import Draw


class PyDraw(Draw):
    def __init__(self, surface: pygame.Surface, color: Color = None):
        self.__surface = surface
        if color is None:
            color = Color(0, 0, 0)
        self.__color = pygame.Color(tuple(color))

    def color(self, color: Color) -> 'PyDraw':
        return PyDraw(self.__surface, color)

    def rect(self, rectangle: Rectangle, width: int = 0) -> 'PyDraw':
        pygame.draw.rect(self.__surface, self.__color,
            pygame.Rect(
                rectangle.left, rectangle.bottom,
                rectangle.width, rectangle.height
            ),
            width
        )
        return self

    def polygon(self, points: List[Point], width: int = 0) -> 'PyDraw':
        pygame.draw.polygon(self.__surface, self.__color,
            [(p.x, p.y) for p in points],
            width
        )
        return self

    def line(self, start: Point, end: Point, width: int = 1) -> 'PyDraw':
        pygame.draw.line(self.__surface, self.__color,
            tuple(start), tuple(end),
            width
        )
        return self

    def lines(self, points: List[Point], width: int = 1) -> 'PyDraw':
        pygame.draw.lines(self.__surface, self.__color, False,
            [(p.x, p.y) for p in points],
            width
        )
        return self

    def circle(self, circle: Circle, width: int = 0) -> 'PyDraw':
        pygame.draw.circle(self.__surface, self.__color,
            tuple(circle.center), circle.radius,
            width
        )
        return self

    def text(self, position: Point, text: str, size: int = 10) -> 'Draw':
        font = pygame.font.Font(pygame.font.get_default_font(), size)
        self.__surface.blit(
            font.render(text, True, self.__color),
            dest=tuple(position)
        )
        return self

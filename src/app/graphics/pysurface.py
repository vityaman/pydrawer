import pygame

from .figure.value.color import Color
from .pydraw import PyDraw
from .surface import Surface


class PySurface(Surface):
    def __init__(self, surface: pygame.Surface):
        self.__surface = surface

    def draw(self, color: Color = None) -> 'PyDraw':
        return PyDraw(self.__surface)

    def fill(self, color: Color = None):
        self.__surface.fill(tuple(color))

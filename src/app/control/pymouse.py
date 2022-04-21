import pygame

from .mouse import Mouse


class PyMouse(Mouse):
    def __init__(self) -> None:
        self.__pos = pygame.mouse.get_pos()

    @property
    def x(self) -> int:
        return self.__pos[0]

    @property
    def y(self) -> int:
        return self.__pos[1]

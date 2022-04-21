import pygame

from .keyboard import Keyboard


class PyKeyboard(Keyboard):
    def __init__(self, ) -> None:
        self.__pressed = pygame.key.get_pressed()

    def pressed(self, key: str) -> bool:
        return self.__pressed[key]

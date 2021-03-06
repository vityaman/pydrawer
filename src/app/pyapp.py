from abc import ABC

import pygame

from .control.pymouse import PyMouse
from .control.pykeyboard import PyKeyboard
from .control.mouse import Mouse
from .control.keyboard import Keyboard
from .control.event import Event
from .graphics.figure.value.size import Size
from .graphics.pysurface import PySurface
from .graphics.surface import Surface
from .app import App


class PyApp(App, ABC):
    def __init__(self, title: str, window_size: Size, fps: int):
        pygame.init()
        self.__window = PySurface(
            pygame.display.set_mode(tuple(window_size))
        )
        pygame.display.set_caption(title)

        self.__clock = pygame.time.Clock()
        self.__running = False
        self.__fps = fps

    def run(self):
        self.on_start()
        self.__running = True
        while self.__running:
            self.__clock.tick(self.__fps)

            self.__handle_events()
            self.on_control(PyMouse(), PyKeyboard())

            self.on_update()

            self.on_draw(self.__window)
            pygame.display.flip()
        self.on_stop()

    def on_start(self):
        pass

    def on_event(self, event: Event):
        pass

    def on_control(self, mouse: Mouse, keyboard: Keyboard):
        pass

    def on_update(self):
        pass

    def on_draw(self, surface: Surface):
        pass

    def on_stop(self):
        pass

    def stop(self):
        self.__running = False

    def __handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.on_event(Event(Event.Type.QUIT))

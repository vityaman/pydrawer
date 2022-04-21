from abc import ABC, abstractmethod

from .graphics.surface import Surface
from .control.keyboard import Keyboard
from .control.mouse import Mouse
from .control.event import Event


class App(ABC):
    @abstractmethod
    def run(self):
        raise NotImplementedError()

    @abstractmethod
    def on_start(self):
        raise NotImplementedError()

    @abstractmethod
    def on_event(self, event: Event):
        raise NotImplementedError()

    @abstractmethod
    def on_control(self, mouse: Mouse, keyboard: Keyboard):
        raise NotImplementedError()

    @abstractmethod
    def on_update(self):
        raise NotImplementedError()

    @abstractmethod
    def on_draw(self, surface: Surface):
        raise NotImplementedError()

    @abstractmethod
    def on_stop(self):
        raise NotImplementedError()

    @abstractmethod
    def stop(self):
        raise NotImplementedError()

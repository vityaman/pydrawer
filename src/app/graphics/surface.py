from abc import ABC, abstractmethod

from .draw import Draw
from .figure.value.color import Color


class Surface(ABC):
    @abstractmethod
    def draw(self, color: Color = None) -> Draw:
        raise NotImplementedError()

    @abstractmethod
    def fill(self, color: Color = None):
        raise NotImplementedError()

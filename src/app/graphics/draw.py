from abc import ABC, abstractmethod
from typing import Sequence

from .figure.value.color import Color
from .figure.value.point import Point
from .figure.rectangle import Rectangle
from .figure.circle import Circle


class Draw(ABC):
    @abstractmethod
    def color(self, color: Color) -> 'Draw':
        raise NotImplementedError()

    @abstractmethod
    def rect(self, rect: Rectangle, width: int = 1) -> 'Draw':
        raise NotImplementedError()

    @abstractmethod
    def polygon(self, points: Sequence[Point], width: int = 1) -> 'Draw':
        raise NotImplementedError()

    @abstractmethod
    def line(self, start: Point, end: Point, width: int = 1) -> 'Draw':
        raise NotImplementedError()

    @abstractmethod
    def circle(self, circle: Circle, width: int = 1) -> 'Draw':
        raise NotImplementedError()

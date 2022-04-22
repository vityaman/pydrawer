from abc import ABC, abstractmethod
from typing import List

from .figure.value import Color, Point
from .figure.rectangle import Rectangle
from .figure.circle import Circle


class Draw(ABC):
    @abstractmethod
    def color(self, color: Color) -> 'Draw':
        raise NotImplementedError()

    @abstractmethod
    def rect(self, rect: Rectangle, width: int = 0) -> 'Draw':
        raise NotImplementedError()

    @abstractmethod
    def polygon(self, points: List[Point], width: int = 0) -> 'Draw':
        raise NotImplementedError()

    @abstractmethod
    def line(self, start: Point, end: Point, width: int = 1) -> 'Draw':
        raise NotImplementedError()

    @abstractmethod
    def lines(self, points: List[Point], width: int = 1) -> 'Draw':
        raise NotImplementedError()

    @abstractmethod
    def circle(self, circle: Circle, width: int = 0) -> 'Draw':
        raise NotImplementedError()

    @abstractmethod
    def text(self, position: Point, text: str) -> 'Draw':
        raise NotImplementedError()

from typing import Callable, List

from .figure.value import Point, Vector, Color
from .figure import Rectangle, Circle
from .draw import Draw


class Transformed(Draw):
    def __init__(self, origin: Draw, transformation: Callable[[Point], Point]):
        self.__origin = origin
        self.__transformation = transformation

    def color(self, color: Color) -> 'Transformed':
        return Transformed(self.__origin.color(color), self.__center)

    def rect(self, rectangle: Rectangle, width: int = 0) -> 'Transformed':
        self.__origin.rect(Rectangle(
                *self.__transformed(Point(rectangle.left, rectangle.right)),
                rectangle.width, rectangle.height),
            width)
        return self

    def polygon(self, points: List[Point], width: int = 0) -> 'Transformed':
        self.__origin.polygon(
            self.__transformed_all(points), width)
        return self

    def line(self, start: Point, end: Point, width: int = 1) -> 'Transformed':
        self.__origin.line(self.__transformed(start), self.__transformed(end), width)
        return self

    def lines(self, points: List[Point], width: int = 1) -> 'Transformed':
        self.__origin.lines(self.__transformed_all(points), width)
        return self

    def circle(self, circle: Circle, width: int = 0) -> 'Transformed':
        self.__origin.circle(
            Circle(self.__transformed(circle.center), circle.radius),
            width)
        return self

    def text(self, position: Point, text: str) -> 'Transformed':
        self.__origin.text(self.__transformed(position), text)
        return self

    def __transformed(self, point: Point) -> Point:
        return self.__transformation(point)

    def __transformed_all(self, points: List[Point]) -> List[Point]:
        return (self.__transformed(point) for point in points)

    @classmethod
    def xoy(cls, origin: Draw, center: Point) -> 'Transformed':
        return Transformed(origin,
            lambda p: Point(p.x + center.x, -p.y + center.y)
        )

    @classmethod
    def scaled(cls, origin: Draw, scale: Vector) -> 'Transformed':
        return Transformed(origin,
            lambda p: Point(p.x * scale.x, p.y * scale.y)
        )

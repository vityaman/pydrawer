from .point import Point
from .vector import Vector


class XY:
    def __init__(self, center: Point, scale: Vector = None):
        self.__center = center
        if scale is None:
            scale = Vector(1, 1)
        self.__scale = scale


    @property
    def center(self) -> Point:
        return self.__center

    @property
    def scale(self) -> Vector:
        return self.__scale

    def original(self, point: Point) -> Point:
        original = Vector(
            point.x * self.scale.x,
           -point.y *  self.scale.y
        ) + self.center
        return Point(original.x, original.y)

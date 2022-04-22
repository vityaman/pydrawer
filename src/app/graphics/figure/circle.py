from .value import Point


class Circle:
    def __init__(self, center: Point, radius: int):
        self.__center = center
        self.__radius = radius

    @property
    def center(self) -> Point:
        return self.__center

    @property
    def radius(self) -> int:
        return self.__radius

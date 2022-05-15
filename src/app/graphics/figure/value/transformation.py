from math import cos, sin
from . import Vector


class LinearTransformation:
    def __init__(self, 
        x_1: float, y_1: float,
        x_2: float, y_2: float
    ):
        self.__x_1 = x_1
        self.__y_1 = y_1
        self.__x_2 = x_2
        self.__y_2 = y_2
    
    def apply(self, vector: Vector) -> Vector:  
        return Vector(
            self.__x_1 * vector.x + self.__y_1 * vector.y,
            self.__x_2 * vector.x + self.__y_2 * vector.y,
        )


def rotation(radians: float) -> 'LinearTransformation':
    cosine = cos(radians)
    sine = sin(radians)
    return LinearTransformation(
        cosine, -sine, 
        sine, cosine
    )


def scale(x_scale: float, y_scale: float) -> 'LinearTransformation':
    return LinearTransformation(
        x_scale, 0,
        0, y_scale
    )

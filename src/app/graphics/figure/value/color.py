from typing import Generator

class Color:
    def __init__(self, r: int, g: int, b: int, a: int = 255) -> None:
        self.__r = r
        self.__g = g
        self.__b = b
        self.__a = a

    @property
    def r(self) -> int:
        return self.__r

    @property
    def g(self) -> int:
        return self.__g

    @property
    def b(self) -> int:
        return self.__b

    @property
    def a(self) -> int:
        return self.__a

    def __iter__(self):
        yield self.r
        yield self.g
        yield self.b
        yield self.a

    def __repr__(self) -> str:
        return '#%02x%02x%02x' % tuple(self)

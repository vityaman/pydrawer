from typing import Generator


class Size:
    def __init__(self, width: int, height: int):
        self.__width = width
        self.__height = height

    @property
    def width(self) -> int:
        return self.__width

    @property
    def height(self) -> int:
        return self.__height

    def __iter__(self):
        yield self.width
        yield self.height

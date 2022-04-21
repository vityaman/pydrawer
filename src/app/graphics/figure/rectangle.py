
class Rectangle:
    def __init__(self, left: int, top: int, width: int, height: int):
        self.__left = left
        self.__top = top
        self.__width = width
        self.__height = height

    @property
    def left(self) -> int:
        return self.__left

    @property
    def right(self) -> int:
        return self.__left + self.__width

    @property
    def top(self) -> int:
        return self.__top

    @property
    def bottom(self) -> int:
        return self.__top + self.__height

    @property
    def height(self) -> int:
        return self.__height

    @property
    def width(self) -> int:
        return self.__width

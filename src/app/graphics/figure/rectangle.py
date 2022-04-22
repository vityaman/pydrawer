
class Rectangle:
    def __init__(self, left: int, right: int, bottom: int, top: int):
        self.__left = min(left, right)
        self.__right = max(left, right)
        self.__bottom = min(bottom, top)
        self.__top = max(bottom, top)

    @property
    def left(self) -> int:
        return self.__left

    @property
    def right(self) -> int:
        return self.__right

    @property
    def top(self) -> int:
        return self.__top

    @property
    def bottom(self) -> int:
        return self.__bottom

    @property
    def height(self) -> int:
        return self.top - self.bottom

    @property
    def width(self) -> int:
        return self.right - self.left

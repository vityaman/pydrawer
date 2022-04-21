
class Point:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y

    def __iter__(self):
        yield self.x
        yield self.y

    def __repr__(self) -> str:
        return f'({self.x}, {self.y})'

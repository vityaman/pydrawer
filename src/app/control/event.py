from enum import Enum


class Event:
    class Type(Enum):
        QUIT = 1

    def __init__(self, type: Type):
        self.__type = type

    @property
    def type(self) -> Type:
        return self.__type

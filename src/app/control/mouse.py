from abc import ABC, abstractproperty


class Mouse(ABC):
    @abstractproperty
    def x(self) -> int:
        raise NotImplementedError()

    @abstractproperty
    def y(self) -> int:
        raise NotImplementedError()

from abc import ABC, abstractmethod


class Keyboard(ABC):
    @abstractmethod
    def pressed(key: str) -> bool:
        raise NotImplementedError()

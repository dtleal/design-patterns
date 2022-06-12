from abc import ABC, abstractclassmethod
from observer import Observer


class Subject(ABC):
    """The subject interface declares a set of methods for managing subscribers

    Args:
        ABC (_type_): _description_
    """

    @abstractclassmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractclassmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractclassmethod
    def notify(self) -> None:
        pass
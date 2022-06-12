from abc import ABC, abstractclassmethod
from typing import Any


class Observer(ABC):
    @abstractclassmethod
    def update(self, subject: Any) -> None:
        pass
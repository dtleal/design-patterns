from __future__ import annotations
from abc import ABC, abstractclassmethod
from random import randrange
from typing import List

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


class ConcreteSubject(Subject):
    """The Subject owns some important state and notifies observers when the state changes        

    Args:
        Subject (_type_): _description_
    """
    _state: int = None

    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_b_logic(self) -> None:
        print("\nSubject: I'm doing something important.")
        self._state = randrange(0, 10)

        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()


class Observer(ABC):
    @abstractclassmethod
    def update(self, subject: Subject) -> None:
        pass


class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state < 3:
            print("ConcreteObserverA: Reacted to the event")


class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 0 or subject._state >= 2:
            print("ConcreteObserverB: Reacted to the event")


if __name__ == "__main__":
    # The client code

    subject = ConcreteSubject()

    ob_a = ConcreteObserverA()
    subject.attach(ob_a)

    ob_b = ConcreteObserverB()
    subject.attach(ob_b)

    subject.some_b_logic()
    subject.some_b_logic()

    subject.detach(ob_a)
    
    subject.some_b_logic()
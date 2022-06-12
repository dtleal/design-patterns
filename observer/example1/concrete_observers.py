from observer import Observer
from subject import Subject


class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state < 7:
            print("ConcreteObserverA: Reacted to the event")


class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 0 or subject._state >= 2:
            print("ConcreteObserverB: Reacted to the event")
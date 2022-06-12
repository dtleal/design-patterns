from concrete_subject import ConcreteSubject
from concrete_observers import ConcreteObserverA, ConcreteObserverB

if __name__ == "__main__":
    # The client code
    subject = ConcreteSubject()

    object_a = ConcreteObserverA()
    object_b = ConcreteObserverB()

    subject.attach(object_a)
    subject.attach(object_b)

    subject.some_logic()
    subject.some_logic()
    subject.some_logic()

    subject.detach(object_a)
    subject.detach(object_b)

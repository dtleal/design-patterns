"""
A refferal from https://refactoring.guru/pt-br/design-patterns/factory-method/python/example
and https://github.com/ArjanCodes/2021-factory-pattern
"""

from typing import Protocol, Type
from dataclasses import dataclass


class Creator(Protocol):

    def some_operation(self) -> str:
        ...


class ConcreteCreator1:

    def some_operation(self) -> str:
        return "App: Launched with the ConcreteCreator1."


class ConcreteCreator2:

    def some_operation(self) -> str:
        return "App: Launched with the ConcreteCreator2."


@dataclass
class Product:
    creator: Creator


@dataclass
class ProductFactory:
    creator_class: Type[Creator]

    def __call__(self) -> Product:
        return Product(self.creator_class())


def client_code(product: Product) -> None:

    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{product.creator.some_operation()}\n")


if __name__ == "__main__":
    factory_creator1 = ProductFactory(ConcreteCreator1)
    creator1 = factory_creator1()
    client_code(creator1)

    factory_creator2 = ProductFactory(ConcreteCreator2)
    creator2 = factory_creator2()
    client_code(creator2)
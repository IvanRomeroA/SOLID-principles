from abc import ABCMeta, abstractmethod


# Interfaces (Clases Abstractas):
class Products(metaclass=ABCMeta):

    @abstractmethod
    def get_values(self) -> dict:
        raise NotImplementedError

    @abstractmethod
    def set_quantity(self, quantity) -> None:
        raise NotImplementedError


class Actions(metaclass=ABCMeta):

    @abstractmethod
    def rewind(self) -> bool:
        raise NotImplementedError


# Clases:
class Cassette(Products, Actions):

    def __init__(self, name: str, quantity: int) -> None:
        self.name = name
        self.quantity = quantity

    def get_values(self) -> dict:
        return {'name': self.name, 'quantity': self.quantity}

    def set_quantity(self, quantity: int) -> None:
        self.quantity = quantity

    def rewind(self) -> bool:
        return True


class CD(Products):

    def __init__(self, name: str, quantity: int) -> None:
        self.name = name
        self.quantity = quantity

    def get_values(self) -> dict:
        return {'name': self.name, 'quantity': self.quantity}

    def set_quantity(self, quantity: int) -> None:
        self.quantity = quantity


# Instancias:
cassette = Cassette('Heavy Metal', 2)
print(cassette.get_values())

cd = CD('Trash Metal', 4)
print(cd.get_values())

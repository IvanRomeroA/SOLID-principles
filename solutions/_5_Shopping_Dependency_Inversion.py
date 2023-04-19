from abc import ABCMeta, abstractmethod


class Shopping:
    ...


# Interfaces:
class Persistence(metaclass=ABCMeta):
    @abstractmethod
    def save(self, shopping: Shopping) -> None:
        raise NotImplementedError


class PaymentMethod(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, shopping: Shopping) -> None:
        raise NotImplementedError


# Clases:
class MongoDatabase(Persistence):
    def save(self, shopping: Shopping): ...


class MySQLDatabase(Persistence):
    def save(self, shopping: Shopping): ...


class CreditCard(PaymentMethod):
    def pay(self, shopping: Shopping): ...


class Paypal(PaymentMethod):
    def pay(self, shopping: Shopping): ...


class ShoppingBasket:

    def __init__(self, persistance: Persistence,
                 payment_method: PaymentMethod) -> None:
        self._persistance = persistance
        self._payment_method = payment_method

    def buy(self, shopping: Shopping) -> None:
        self._persistance.save(shopping)
        self._payment_method.pay(shopping)


# Instancias:
shopping = Shopping()

# Persistencia
mongo_db = MongoDatabase()
mysql_db = MySQLDatabase()

# Métodos de Pago
credit_card = CreditCard()
paypal = Paypal()

# Ejecución:
shopping_basket_1 = ShoppingBasket(mongo_db, paypal)
shopping_basket_1.buy(shopping)

shopping_basket_2 = ShoppingBasket(mysql_db, credit_card)
shopping_basket_2.buy(shopping)

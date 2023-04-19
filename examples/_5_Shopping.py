# Clases
class Shopping:
    ...


class MongoDatabase:
    def save(self, shopping: Shopping): ...


class CreditCard:
    def pay(self, shopping: Shopping): ...


class ShoppingBasket:
    def buy(self, shopping: Shopping):
        db = MongoDatabase()
        credit_card = CreditCard()
        db.save(shopping)
        credit_card.pay(shopping)


# Instancias:
shopping = Shopping()

# Ejecución:
shopping_basket = ShoppingBasket()
shopping_basket.buy(shopping)

# Esta implementación dará problemas al hacer Pruebas Unitarias.

from ._5_Shopping import ShoppingBasket


# Problemas al hacer Pruebas Unitarias:
class TestShoppingBasket:
    BASE_PATH = 'examples._5_Shopping'
    SHOPPING_PATH = f'{BASE_PATH}.Shopping'
    DATABASE_PATH = f'{BASE_PATH}.MongoDatabase'
    CREDIT_CARD_PATH = f'{BASE_PATH}.CreditCard'

    def test_buy(self, mocker):
        # Es necesario hacer mocks de las clases internas y de sus métodos
        # Pero al estar creadas internamente, se ejecutarán con normalidad,
        # Esto no sería una Prueba Unitaria, sino una Prueba de Integración.
        shopping = mocker.patch(self.SHOPPING_PATH)

        # No hay donde utilizar estos mocks, esto supone un problema!
        database = mocker.patch(self.DATABASE_PATH)
        credit_card = mocker.patch(self.CREDIT_CARD_PATH)

        shopping_basket = ShoppingBasket()
        result = shopping_basket.buy(shopping)

        assert result is None

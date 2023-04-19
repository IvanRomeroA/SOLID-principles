from ._5_Shopping_Dependency_Inversion import ShoppingBasket


# Problemas al hacer Pruebas Unitarias:
class TestShoppingBasket:
    BASE_PATH = 'solutions._5_Shopping_Dependency_Inversion'
    SHOPPING_PATH = f'{BASE_PATH}.Shopping'
    MONGO_PATH = f'{BASE_PATH}.MongoDatabase'
    MYSQL_PATH = f'{BASE_PATH}.MySQLDatabase'
    CREDIT_CARD_PATH = f'{BASE_PATH}.CreditCard'
    PAYPAL_PATH = f'{BASE_PATH}.Paypal'

    def test_buy_mongo_paypal(self, mocker):
        shopping = mocker.patch(self.SHOPPING_PATH)
        database = mocker.patch(self.MONGO_PATH)
        database.save = mocker.MagicMock(return_value=None)
        payment_method = mocker.patch(self.PAYPAL_PATH)
        payment_method.pay = mocker.MagicMock(return_value=None)

        shopping_basket = ShoppingBasket(database, payment_method)
        result = shopping_basket.buy(shopping)

        assert result is None

    def test_buy_mysql_credit_card(self, mocker):
        shopping = mocker.patch(self.SHOPPING_PATH)
        database = mocker.patch(self.MYSQL_PATH)
        database.save = mocker.MagicMock(return_value=None)
        payment_method = mocker.patch(self.CREDIT_CARD_PATH)
        payment_method.pay = mocker.MagicMock(return_value=None)

        shopping_basket = ShoppingBasket(database, payment_method)
        result = shopping_basket.buy(shopping)

        assert result is None

# Ahora se tiene una clase que sólo manejará métodos de la orden
# y se separa el método de pago en otra clase llamada PaymentProcessor
class Order:

    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = 'open'

    def add_item(self, name: str, quantity: int, price: float) -> None:
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self) -> float:
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total


# Clase PaymentProcessor con los métodos: pago con débito y pago a crédito.
class PaymentProcessor:

    @staticmethod
    def pay_debit(order: Order, security_code: str) -> None:
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = 'paid'

    @staticmethod
    def pay_credit(order: Order, security_code: str) -> None:
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = 'paid'


# Ahora se instancia la clase Order, y se agrega los items a comprar en la orden.
order = Order()
order.add_item('Teclado', 1, 50.0)
order.add_item('Memoria', 1, 150.0)
order.add_item('Cable USB', 2, 5.0)

# Imprime el precio total de la orden
print(order.total_price())

# Instancia la clase de procesador de pago y se llama al método pagar con débito
# pasando como argumento la orden y el código de seguridad de la tarjeta.
processor = PaymentProcessor()
processor.pay_debit(order, '0372846')

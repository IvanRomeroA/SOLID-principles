class Order:

    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = 'open'

    def add_item(self, name: str, quantity: int, price: float) -> None:
        # Agrega un item con la cantidad y precio a la orden.
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self) -> float:
        # Retorna el precio total a pagar.
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total

    def pay(self, payment_type: str, security_code: str) -> None:
        # Genera el pago según la forma de pago, débito o crédito.
        if payment_type == 'debit':
            print("Processing debit payment type")
            print(f"Verifying security code: {security_code}")
            self.status = 'paid'
        elif payment_type == 'credit':
            print("Processing credit payment type")
            print(f"Verifying security code: {security_code}")
            self.status = 'paid'
        else:
            print(f"Unknown payment type: {payment_type}")


# Se crea la instancia de la orden con los items, sus cantidades y precios.
order = Order()
order.add_item('Teclado', 1, 50.0)
order.add_item('Memoria', 1, 150.0)
order.add_item('Cable USB', 2, 5.0)

# Imprime el precio total de la orden
print(order.total_price())

# Se define la forma de pago.
order.pay('debit', '0372846')

"""
«Товар и корзина». Класс Product (title, price, quantity) с методом total_price() (цена × количество). Класс Cart,
который хранит список продуктов и методы add(product), total_sum() и show(). Добавить несколько товаров, вывести общую
сумму.
"""

class Product:
    def __init__(self, title, price, quantity):
        self.title = title
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def total_sum(self):
        return sum(p.total_price() for p in self.products)

    def show(self):
        res_str = ""

        for p in self.products:
            res_str += f"{p.title}: {p.total_price()} руб.\n"

        return res_str

cart = Cart()
cart.add_product(Product("Яблоки", 10.0, 10))
cart.add_product(Product("Груши", 12.5, 5))
cart.add_product(Product("Апельсины", 15.2, 20))

print("Содержимое корзины:")
print(cart.show())
print(f"Общая сумма всей корзины: {cart.total_sum()} руб.")


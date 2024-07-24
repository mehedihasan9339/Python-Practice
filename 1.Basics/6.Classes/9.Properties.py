class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value


product = Product(50)
product.price = 10
print(product.price) # 10

product.price = -1
print(product.price) # ValueError: Price cannot be negative.

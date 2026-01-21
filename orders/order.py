from users import *
from products import *

class Order:
  def __init__(self, cashier:Cashier, customer:Customer):
    self.cashier = cashier
    self.customer = customer
    self.products = []

  def add(self, product : Product):
    self.products.append(product)

  def calculateTotal(self) -> float:
    total = 0.0
    for product in self.products:
        total += product.price
    # Redondeamos a 2 decimales
    return round(total, 2)
  
  def show(self):    
    print("Hello : "+self.customer.describe())
    print("Was attended by : "+self.cashier.describe())
    # Enumerar productos para mostrar "Product 1", "Product 2"...
    for i, product in enumerate(self.products, 1):
      print(f"Product {i}: {product.describe()}")
    print(f"Total price : {self.calculateTotal()}")
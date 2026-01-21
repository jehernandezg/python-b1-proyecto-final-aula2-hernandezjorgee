from abc import ABC, abstractmethod
from users import Cashier, Customer
# No importamos Product aquí para evitar dependencias circulares, se pasan como args

class Converter(ABC):
  @abstractmethod
  def convert(self,dataFrame,*args) -> list:
      pass  
  def print(self, objects):
    for item in objects:
      print(item.describe())

class CashierConverter(Converter):
  def convert(self,dataFrame, *args):    
    result = []
    for _, row in dataFrame.iterrows():
        # Crea instancia de Cashier usando las columnas del CSV
        cashier = Cashier(str(row['dni']), row['name'], int(row['age']), row['timetable'], float(row['salary']))
        result.append(cashier)
    return result

class CustomerConverter(Converter):
  def convert(self,dataFrame, *args):
    result = []
    for _, row in dataFrame.iterrows():
        # Crea instancia de Customer
        customer = Customer(str(row['dni']), row['name'], int(row['age']), row['email'], str(row['postalcode']))
        result.append(customer)
    return result

class ProductConverter(Converter):
  def convert(self,dataFrame, *args):
    result = []
    # args[0] será la clase (ej. Hamburger, Soda)
    product_class = args[0]
    for _, row in dataFrame.iterrows():
        product = product_class(str(row['id']), row['name'], float(row['price']))
        result.append(product)
    return result
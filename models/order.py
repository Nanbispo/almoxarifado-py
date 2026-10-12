from models.person import Person
from models.product import Product

class Order:
    def __init__(self, Person, Product, id):
        self.id = id
        self.Person = Person
        self.Product = Product

from models.product import Product


produto = Product("Carro", "Transportação", "disponivel")

print(produto.name, produto.department, produto.status)
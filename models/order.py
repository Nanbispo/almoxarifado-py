from datetime import date

from models.person import Person
from models.product import Product


class Order:
    def __init__(
        self,
        person: Person,
        product: Product,
        data_retirada: date,
        data_devolucao: date,
        data_devolucao_real: date | None = None,
        id=None,
    ):
        self.id = id
        self.person = person
        self.product = product
        self.data_retirada = data_retirada
        self.data_devolucao = data_devolucao
        self.data_devolucao_real = data_devolucao_real

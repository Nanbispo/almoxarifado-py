from models.department import Department

class Product:
    def __init__(self, name, department: Department, status: "Disponivel", id=None):
        self.id = id
        self.name = name
        self.department = department
        self.status = status


        
from models.department import Department

class Person:
    def __init__(self, name, department: Department, type, id):
        self.id = id
        self.name = name
        self.department = department
        self.type = type
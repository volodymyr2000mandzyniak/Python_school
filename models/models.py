import json
from framework.models import Model


class Plant(Model):
    file = "database/plants.json"
    fields = ["name", "address"]

    def __init__(self, name, address, id=None):
        self.name = name
        self.address = address
        self.id = id

    @classmethod
    def get_el_by_id(cls, id):
        data = cls.get_file_data()
        for el in data:
            if el["id"] == id:
                return cls(el["name"], el["address"], id=el["id"])

# ===============================================================

class Employee(Model):
    file = "database/employees.json"
    fields = ["name", "email", "plant_id"]

    def __init__(self, name, email, plant_id, id=None):
        self.name = name
        self.email = email
        self.plant_id = plant_id
        self.id = id

    # def generate_dict(self):
    #     return {
    #         "name": self.name,
    #         "email": self.email,
    #         "plant_id": self.plant_id
    #     }

    @classmethod
    def get_el_by_id(cls, id):
        data = cls.get_file_data()
        for el in data:
            if el["id"] == id:
                return cls(el["name"], el["email"], el["plant_id"], id=el["id"])

# ===============================================================

class Salon(Model):
    file = "database/salons.json"
    fields = ["name", "address"]

    def __init__(self, name, address, id=None):
        self.name = name
        self.address = address
        self.id = id


    # @classmethod
    # def get_el_by_id(cls, id):
    #     data = cls.get_file_data()
    #     for el in data:
    #         if el["id"] == id:
    #             return cls(el["name"], el["address"], id=el["id"])


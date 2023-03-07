import json
from abc import ABC, abstractmethod


class Model(ABC):
    file = ""
    fields = []

    # @abstractmethod
    # def generate_dict(self):
    #     pass

    # @abstractmethod
    @classmethod
    def get_el_by_id(cls, id):
        pass

    @classmethod
    def get_all(cls):
        data = cls.get_file_data()
        for el in data:
            for key in cls.fields:
                print(el[key])


    @classmethod
    def get_file_data(cls):
        file = open(cls.file, "r")
        data = json.loads(file.read())
        file.close()
        return data

    @classmethod
    def save_to_file(cls, data):
        file = open(cls.file, "w")
        file.write(json.dumps(data))
        file.close()


    def save(self, **kwargs):
        data = self.get_file_data()
        new_el = self.generate_dict(**kwargs)
        if len(data) > 1:
            new_el["id"] = len(data) + 1
        else:
            new_el["id"] = 1
        data.append(new_el)
        self.save_to_file(data)


    def update(self):
        data = self.get_file_data()
        for el in data:
            if el["id"] == self.id:
                for key in self.fields:
                    el[key] = input("Type a new " + key + ": ")
        self.save_to_file(data)


    def generate_dict(self, **kwargs):
        if kwargs["class_name"] == "employee":
            return {
                "name": kwargs["name"],
                "email": kwargs["email"],
                "plant_id": kwargs["plant_id"]
            }
        else:
            return {
                "name": kwargs["name"],
                "address": kwargs["address"],
                "id": kwargs["id"]
              }
        # elif kwargs["class_name"] == "salone":
        #     return {
        #         "name": kwargs["name"],
        #         "address": kwargs["address"],
        #     }
        # else:
        #     return {}


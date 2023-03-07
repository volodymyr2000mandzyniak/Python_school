import json

class Plant:
    file = "database/plants.json"

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def generate_dict(self):
        return {
            "name": self.name,
            "address": self.address
        }


    def save(self):
           self.get_all_plants_for_print()
           plants = self.get_all_plants()
           file = open(self.file, "w")
           plant = self.generate_dict()
           print(len(plants))

           if len(plants) > 1:
               print('plus one')
               plant["id"] = len(plants) + 1
           else:
               print('one')
               plant["id"] = 1

           plants.append(plant)
           file.write(json.dumps(plants))
           file.close()    


    @classmethod
    def get_all_plants(cls):
        file = open(cls.file, "r")
        plants = json.loads(file.read())
        file.close()
        return plants

   
    @classmethod
    def get_all_plants_for_print(cls):
        plants = cls.get_all_plants()
        for plant in plants:
            print(plant["name"])
            print(plant["address"])
            print(plant["id"])
            print("=================")


    @classmethod
    def update(cls, plant_id, new_data):
        plants = cls.get_all_plants()
        
        for plant in plants:
            if plant['id'] == plant_id:
                plant.update(new_data)
               
        file = open(cls.file, "w")
        file.write(json.dumps(plants))
        file.close()      

# =======================================================================================

class Employee:
    file = "database/employees.json"

    def __init__(self, name, email, plant_id):
        self.name = name
        self.email = email
        self.plant_id = plant_id

    def generate_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "plant_id": self.plant_id
        }


    def save(self):
        file = open(self.file, "r")
        employees = json.loads(file.read())
        file.close()
        file = open(self.file, "w")
        employee = self.generate_dict()

        if len(employees) > 1:
            employee["id"] = len(employees) + 1
        else:
            employee["id"] = 1

        employees.append(employee)
        file.write(json.dumps(employees))
        file.close()


    @classmethod
    def get_all_employees(cls):
        file = open(cls.file, "r")
        employees = json.loads(file.read())
        file.close()
        return employees

     
    @classmethod
    def get_all_employees_for_print(cls):
        employees = cls.get_all_employees()
        for employee in employees:
            print(employee["name"])
            print(employee["email"])
            print(employee["plant_id"])
            print("=====================")       


    @classmethod
    def update(cls, employee_id, new_data):
        employees = cls.get_all_employees()
        
        for employee in employees:
            if employee['id'] == employee_id:
                employee.update(new_data)
               
        file = open(cls.file, "w")
        file.write(json.dumps(employees))
        file.close()            
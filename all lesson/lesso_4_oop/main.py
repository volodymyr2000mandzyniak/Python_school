from models import Plant, Employee
import re

while True:
    print("1. Add Plant\n2. Gel all plants\n3. Update Plant")
    print("---------------------")
    print("4.Add Employee \n5.Get all employees\n6. Update Employees")
    print("---------------------")
    
    flag = int(input("Choose menu item: "))
    # Created Plant
    if flag == 1:
        name = input("Plant name: ")
        address = input("Plant address: ")
        plant = Plant(name, address)
        plant.save()

    # Get all plant
    elif flag == 2:
        Plant.get_all_plants_for_print()

    # Updated plant
    elif flag == 3:
        plant_id = int(input("Plant_id: "))  
        name = input("Plant new name: ")
        address = input("Plant new address: ")
        new_data = {'name': name, 'address': address}
        
        Plant.update(plant_id, new_data) 
        print("====Updated====")
    
#====================================================================
        
    # Created Employee
    elif flag == 4:
        name = input("Employee name: ")
        email = input("Employee email: ")
        plant_id = int(input("Plant id: "))
        
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print('your email is incorect.Example exemp@exmp.com')   
            continue
        else:
            employee = Employee(name, email, plant_id)
            employee.save()
            print("======Created=======")
    
    # Get all emplyees
    elif flag == 5:
        Employee.get_all_employees_for_print()
    

    # Update employee
    elif flag == 6:
        employee_id = int(input("Employee_id: "))
        name = input("Employee name: ")
        email = input("Employee email: ")
        plant_id = int(input("Plant id: "))
        new_data = {'name': name, 'email': email, 'plant_id': plant_id}
        
        Employee.update(employee_id, new_data)
        print("====Updated====")


            






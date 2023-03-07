from models import Plant, Employee, Salon 

while True:
    print("1. Add Plant\n2. Gel all plants\n3. Add Employee\n4. Get all employees\n5. Update employee\n6. Update Plant")
    print("--------------------")
    print("7. Add Salon\n8. Get All Salon\n9. Update Salon")
    flag = int(input("Choose menu item: "))
    
    if flag == 1:
        name = input("Plant name: ")
        address = input("Plant address: ")
        
        plant = Plant(name, address)
        plant.save(name=plant.name, address=plant.address, class_name='plant' )
    
    elif flag == 2:
        Plant.get_all()
    
    elif flag == 3:
        name = input("Employee name: ")
        email = input("Employee email: ")
        plant_id = int(input("Plant id: "))
        
        employee = Employee(name, email, plant_id)
        employee.save(name=employee.name, email=employee.email, plant_id=employee.plant_id, class_name='employee')
    
    elif flag == 4:
        Employee.get_all()
    
    elif flag == 5:
        id = int(input("Id which employee you want to update: "))
        employee = Employee.get_el_by_id(id)
        employee.update()

    elif flag == 6:
        id = int(input("Id which plant you want to update: "))
        Plant.update(id)
    # add Salon
    elif flag == 7:
        name = input("Enter name of Salon: ")
        adress = input("Enter adress of Salon: ")
        salon = Salon(name, adress)
        salon.save(name=salon.name, address=salon.address, class_name='salon')        
        print("=== Created ===")
    
    # Get All Salon 8
    # elif flag == 8:
    
    
    # # Update Salon 9
    # elif flag == 9:

    else:
        print("End")    
    
    




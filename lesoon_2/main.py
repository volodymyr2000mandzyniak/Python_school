from utils.helpers import write_new_human, get_all_humans, valid_email, user_update, unique_email

while True:
    try:
        print("1. Add new person! \n2. Get all persons! \n3. Update users: ")
        flag = int(input("Choose what you want to do: "))
        if flag == 1:
        
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            email = input("Email: ")

            email_uni = unique_email(email)

            if email_uni:
                print("=== This name is used === \n === Write another name ===")
            else:
                check_email = valid_email(email)

                if check_email:
                    human_dict = {'first_name': first_name, "last_name": last_name, "email": email}
                    write_new_human(human_dict)
                    print("======Created=======")
                else:
                    print('your email is incorect.Example exemp@exmp.com')   

        elif flag == 2:
            humans = get_all_humans()
            for human in humans:
                print("User_id: ", human["id"])
                print("First_name: ", human["first_name"])
                print("Last_name: ", human["last_name"])
                print("Email:", human["email"])
                print("==================================================================")
        elif flag == 3:
            user_id = int(input("Enter user id for update: "))
            humans = get_all_humans()

            human = []
       
            for user in humans:
                if user['id'] == user_id:
                    human.append(user)
        
            print(human[0])

            # human = [user for user in humans if user['id'] == user_id][0]
            new_first_name = input('new first name: ', )
            new_last_name = input('new last name: ')
            new_email = input('new email: ')
            check_email = valid_email(new_email)

            if check_email:
                updated = {'first_name': new_first_name, "last_name": new_last_name, "email": new_email}
                user_update(user_id, updated)
                print("======Uptaded=======")
            else:
                print('your email is incorect.Example exemp@exmp.com')

        else:
            print("Don't have this menu item")
            break
    except ValueError:
        print("*** Dont corect input, Pless enter only number! ***")        
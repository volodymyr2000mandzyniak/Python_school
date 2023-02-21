import json

def valid_email(email):
    list_email = email.split("@")
    check_email = True if len(list_email) == 2 and '.' in list_email[1] else False
    return check_email


def get_all_humans() -> list:
    f = open("database/persons.json", "r")
    data = json.loads(f.read())
    f.close()
    return data


def write_new_human(human: dict):
    data = get_all_humans()
    if len(data) < 1:
        human["id"] = 1
    else:
        human["id"] = len(data) + 1
    data.append(human)
    file = open("database/persons.json", "w")
    data = json.dumps(data)
    file.write(data)
    file.close()


def user_update(user_id, new_data):
    data = get_all_humans()
    for el in data:
        if el['id'] == user_id:
            el.update(new_data)
    
    file = open("database/persons.json", "w")
    json.dump(data, file)


def unique_email(email):
    data = get_all_humans()
    for el in data:
        if el['email'] == email:
            return True
    return False


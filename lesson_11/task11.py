from decorators import decorator_for_sensitive_data

@decorator_for_sensitive_data(10)

def get_sensitive_data():
    users = []
    with open("passwords.txt","r") as f:
        for i, j in enumerate(f):
            if i == 0:
                keys = j.strip().split(',')
            else:
                users.append(j.strip().split(','))
    list_of_users = []
    for user in users:
        users_dict = {}
        for key , value in enumerate(user):
            users_dict[keys[key]] = value
        list_of_users.append(users_dict)

    
    return list_of_users           

print(get_sensitive_data())








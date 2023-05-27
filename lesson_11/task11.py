from decorators import decorator_for_sensitive_data, decorator_for_error

@decorator_for_error
@decorator_for_sensitive_data(10)

def get_sensitive_data():
    users = []
    with open("passwords.txt","r") as f:
        for i, line in enumerate(f):
            if i == 0:
                continue
            else:
                users.append(line.strip().split(','))
    list_of_users = []
    for name, password  in users:
        users_dict = {
            name : password
        }
        list_of_users.append(users_dict)

    
    return list_of_users           

print(get_sensitive_data())
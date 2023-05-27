from datetime import datetime
# 1
def Login_Decorator(func):
    def wrapper(login, password):
        try:
            func(login, password)
        except Exception as e:
            with open("log.txt", "a") as f:
                f.write(f"{e} {datetime.now()}\n")

    return wrapper            

def Login(login, password):
    if login == "admin" and password == "admin":
        return True
    else:
        raise Exception("Invalid User")  

login = Login_Decorator(Login)
login("admin","user")

# 3
class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.f = open("log.txt" , "a")

    def do_login(self):
        if self.login == "admin"  and self.password == "admin":
            return True
        else:
            raise Exception("Invalid User")

    def write(self, date_time):
        self.f.write(f"{date_time}")        

    def __enter__(self):
        return self        

    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type is None:
            print("successful")
            self.f.close()
        else:
            self.write(exc_value, exc_tb, datetime.now())

            return True

with User("admin" ,"admin") as f:
    f.do_login()
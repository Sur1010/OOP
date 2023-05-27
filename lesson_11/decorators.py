from datetime import datetime

def decorator_for_error(func):
    def wrapper():
        try:
            return func()
        except Exception as e:
            with open("log.txt", "a") as file:
                file.write(f"{e} {datetime.now()}\n")

    return wrapper                

def decorator_for_sensitive_data(size):
    def wrapper(func):
        def wrap():
            long_size = func()
            if len(long_size) < size:
                raise Exception("error")
            return long_size

        return wrap

    return wrapper            
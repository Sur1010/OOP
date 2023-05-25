def decorator_for_sensitive_data(size):
    def wrapper(func):
        def wrap():
            long_size = func()
            if len(long_size) > size:
                raise Exception("error")
            return long_size

        return wrap

    return wrapper            




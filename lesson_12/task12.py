# # 1 
# # __call__ methodov kanchum enq vorpes function:

# class ExampleOne:
#     def __init__(self):
#         print("Created")

#     def __call__(self, a, b):
#         print(a * b)

# multiplication = ExampleOne()
# multiplication = (2,5)

# # 2
# # object sarqeluc skzbum ashxatum e __new__ methody heto __init__ methody ashxatuma ayn jamanak erb stexcum enq attribute-ner:

# class ExampleTwo:

#     def __new__(cls):
#         return object.__new__(cls)

#     def __init__(self):
#         self.instance_method()

#     def instance_method(self):
#         print('success!')

# my_object = (ExampleTwo)

# 3
# type-y class stexcox class-a bolor class-nery jarangvum en object-ic:

# Homework №12
class Meta(type):
    def __new__(meta, class_name, supers, class_dict):
        return type.__new__(meta, class_name, supers, class_dict)

    def __init__(self,  class_name, supers, class_dict):
        self.instance = None
        super(Meta, self).__init__( class_name, supers, class_dict)
        
    def __call__(self, *args, **kwargs):
        if not self.instance:
            self.instance = type.__call__(self, *args)
        
        return self.instance

class SpaceClass(object):
    pass

class Logger(SpaceClass, metaclass=Meta):
    pass

x = Logger()
y = Logger()
print(x is y)
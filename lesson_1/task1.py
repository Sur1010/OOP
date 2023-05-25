# 1
# ---- 1.1 ----
class Car:
    def __init__(self, brand, model, color, year, started = False):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year
        self.started = started

    def start(self):
        self.started = True
        print("br br br start")

    def stop(self):
        self.started = False
        print("stop\n")

    # ---- 2.1 ----
    def all_data(self):
        print(f"Brand = {self.brand}\nModel = {self.model}\nColor = {self.color}\nYear = {self.year}")

    # ---- 2.2 ---- 
    def data(self):
        return (self.brand , self.model)

    # ---- 2.3 ---- 
    def car_age(self):
        return (2023 - int(self.year))

    def change_color(self, new_color):
        self.color = new_color    



maserati = Car("Maserati", "Quattroporte", "black", "2023",)
lada = Car("LADA", "Niva", "red", "2023" )

maserati.all_data()
maserati.start()
maserati.stop()
lada.all_data()
lada.start()
lada.stop()

# ---- Research ----
# constructor-y avtomat kerpov kanchvum e erb stexcvum e object isk destructor-y kanchvume e erb jnjum enq object-y :
# constructor ( __init()__ )
# destructor ( __del()__ )
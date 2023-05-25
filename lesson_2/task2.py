# 1
class Car:
    # ---- 1.1 ----
    headlights_count = 4
    wheels_count = 4
    def __init__(self, horsepower, weight, engine_type):
        self.horsepower = horsepower
        self.weight = weight
        self.engine_type = engine_type

    # ---- 1.2 ----
    def max_speed(self):
        return int(self.horsepower) / int(self.weight) * 1500

    # ---- 1.3 ----
    @classmethod
    def change_wheels_count(cls, new_wheels_count):
        cls.headlights_count = new_wheels_count
        return new_wheels_count

    @staticmethod
    def change_headlights_count(new_headlights_count):
        Car.headlights_count = new_headlights_count
        return new_headlights_count

# ---- 1.4 ----
bmw = Car(500, 100, "V16")
print(bmw.max_speed())

# 2
class Bus(Car):
    # ---- 2.1 ----
    def __init__(self, horsepower, weight, engine_type, max_seats, busy_seats = 0):
        self.horsepower = horsepower
        self.weight = weight
        self.engine_type = engine_type
        self.max_seats = max_seats
        self.busy_seats = busy_seats

    # ---- 2.2 ----
    def add_busy_seats_count(self, new_seats):
        if new_seats < self.max_seats:
            self.busy_seats = new_seats
        return new_seats    

    # ---- 2.3 ----
    def free_seats(self):
        return int(self.max_seats) - int(self.busy_seats)

# ---- 2.4 ----
ford = Bus(1000, 500 , "V8", 25 , 10)
print(ford.max_speed())

# ---- Research ----
# __dict__ attribute-y veradarcnuma object-y dictionary-um
# dir() function-y veradarcnuma object-i bolor hatkutyunnery ev metodnery aranc arjeqneri 
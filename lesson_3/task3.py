# 1
class Animal:
    # ---- 1.1 ----
    def __init__(self, eyes, hands, lags, color, runing_speed = 45):
        self.eyes = eyes
        self.hands = hands
        self.lags = lags
        self.color = color
        self.runing_speed = runing_speed

    # ---- 1.2 ----
    def animal_sound(self):
        return f"dzayn em hanum"

    # ---- 1.3 ----
    def running(self):
        return f"vazum em {self.runing_speed}(km/h) aragutyamb"

# 2
class Cat(Animal):
    # ---- 2.1 ----
    def animal_sound(self):
        return f"mlavelu " + super().animal_sound()

    # ---- 2.2 ----
    def sound_and_run(self):
        return f"mlavum em " + super().running()

# 3
class Lion(Cat):
    """
    description of the class
    """

    def eat_meat(slef):
        print("mis em utum")
        
    # 4
    def __str__(self):
        return f"worked "

print(Lion.__doc__)
print(Animal.__bases__)
print(Cat.__bases__)
print(Lion.__bases__)
is_a_subclass = issubclass(Lion, Cat)
print(is_a_subclass)

# ---- Research ----
# __doc__ attribute veradarcnum e documentaciyan
# __bases__ attribute veradarcnum e parent class-i anunnery
# issubclass() function veradarcnum e True ete nshvach arajin arjeqy erkrord arjeqi child-n e 
# 1
# __getattribute__  uni default implementation isk __getattr__ chuni:
# __getattribute__ kanchvum e amen angam arjeqy veradarcneluc is ete arjeq chka ogtagorcvum e __getattr__:

# 2
# private attribute-i het  karox enq ashxatel menak class-i nersum , private attribute-y uni sahmanapak hnaravorutyun: 

# 3
class God:
    def __init__(self, first_name, count_of_hands, super_power):
        self.first_name = first_name
        self.count_of_hands = count_of_hands
        self.super_power = super_power

    def voice_after_clap(self):
        return f"sound of clapping"

    def clap(self):
        if self.count_of_hands >= 2:
            return self.voice_after_clap()
        else:
            return f"can't make a sound of clapping"    

# ---- 3.2 ----
class Zeus(God):
    def __init__(self, name, age, height):
        self.name = name
        self._age = age
        self.__height = height

class Herkules(Zeus):

    def get_public(self):
        public_list = []
        for i in self.__class__.mro():
            if i == object:
                continue
            for k , v in i.__dict__.items():
                if not k.startswith("_"):
                    public_list.append((k,v)) 

        return public_list         
                      
    def get_protected(self):
        protected_list = []
        for i in self.__class__.mro():
            if i == object:
                continue
        for k , v in i.__dict__.items():
            if k.startswith("_") and not k.startswith(f"_{i.__name__}"):
                    protected_list.append((k,v))

        return protected_list            
       
    def get_private(self):
        private_list = []
        for i in self.__class__.mro():
            if i == object:
                continue
        for k , v in i.__dict__.items():
            if k.startswith(f"_{i.__name__}"):
                private_list.append((k,v))

        return private_list           

# ---- Research ----
# __slots__ tuyl e talis hstak haytararel tvyalneri andamnery, 
# taracq e pahum hishoxutyan mej ev kanxum e __dict__ ev __weakref__ attribut-neri stexcumy:

# property()-in veradarcnum e getter, setter, deleter:
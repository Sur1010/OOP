import os 
# 1
class File:
    def getter_file(self):
        with open(f'{self.__class__.__name__}.txt', 'a') as f:
            return f

    def setter_file(self, file):
        with open(f'{file}.txt', 'w') as f:
            self._f = f

    @property
    def child_file(self):
        with open(f'{self.__class__.__name__}.txt', 'r') as f:
            return f.read()

    @child_file.setter
    def child_file(self,text):
        with open(f'{self.__class__.__name__}.txt', 'w') as f:
            f.write(text)

    @child_file.deleter
    def child_file(self):
        os.remove(f'{self.__class__.__name__}.txt')

    my_file = property(getter_file, setter_file) 

class Tesla(File):
    pass

class Lexus(File):
    pass

# ---- Research ----
# open arac fayli anuny file object-ic karox enq nayel file.name-i mijocov:

# ipmort anenq oc ev heto kanchenq oc.remove("file"):

# ipmort anenq oc ev heto kanchenq oc.rename("old name" , "new name"):
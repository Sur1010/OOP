from abc import ABC, abstractmethod
# 1
class A(object):
	def __init__(self):
		print ("A")

class B(A):
	def __init__(self):
		print ("B")

class C(A):
	def __init__(self):
		print ("C")

class D(B, C):
	def __init__(self):
		print ("D")

print(D.mro())

# skzbic kstugi d-um  heto knayi b-um qani vor c u b jarangvac en a ic c-ic heo knayi a-n:

# 2
class AbstractFile(ABC):
    @abstractmethod
    def translate(self):
        pass
    
    def write(self):
        pass

# ---- 2.1 ----
class EnglishFile(AbstractFile):
    # ---- 2.2 ----
    def translate(self, text):
        self.text = text
        letters = ("абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
                   "abwgdeejzijklmnoprstufhzcss_y_euaABVGDEEJZIJKLMNOPRSTUFHZCSS_Y_EUA")
        en = {ord(a):ord(b) for a, b in zip(*letters)}
        return text.translate(en)

    # ---- 2.3 ----
    def write(self):
        with open('translated.txt' , 'w+') as f:
            f.write(self.text)
            
# ---- 2.4 ---- 
class RussianFile(AbstractFile):
    def translate(self, text):
        self.text = text
        letters = ("абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
                   "abwgdeejzijklmnoprstufhzcss_y_euaABVGDEEJZIJKLMNOPRSTUFHZCSS_Y_EUA")
        ru = {ord(a):ord(b) for b, a in zip(*letters)}
        return text.translate(ru)
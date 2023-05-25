import re
# 1
# jarangakanutyuny mez tuyl e talis arden stexcvac skzbnakan  class-ic jarangel skzbnakan class-i bolor hatkutyunnery ev methodnery: 

# 2
# abstract class-ic chenq karox object stexcel ayd class-ic karox enq mek ayl urish class-um jarangel abstract methody ev jarangvac
# class-um abstract methodi vra popoxutyunner anel:

# 3
class FilterText:
    text = '055-445-789 E.Mask 124.06.2014 093-587-135 Nemo 1.09.1887 E.Auditore 24.17.2020 096-2288-987 R.Rocknrolla'

    # ---- 3.1 ----
    def __getattr__(self, attribute_name):
        if attribute_name == "name":
            find_all_name = re.findall(r"[A-Z][.][A-Z][a-z]*", self.text)
            return find_all_name

        elif attribute_name == "dates":
            find_all_dates = re.findall(r"[0-9]*[.][0-9]*[.][0-9]*", self.text)
            return find_all_dates

        elif attribute_name == "phone_numbers":
            find_all_phone_numbers = re.findall(r"[0-9]*[-][0-9]*[-][0-9]*", self.text)
            return find_all_phone_numbers

    # ---- 3.2 ----
    def __getitem__(self, index):
        return(self.text.split(' ')[index])

    # ---- 3.3 ----
    def __setitem__(self, index, value):
        list_text = self.text.split(' ')
        list_text[index] = value
        self.text = ",".join(list_text)


x = FilterText()
print(x.name)
print(x.dates)
print(x.phone_numbers)
print(x[1])
print(x[1:3])
x[0] = 'G.Ritchie'
print(x.text)

# ---- Research ----
# __bool__ method-y veradarcnum e True kam False:
# __len__ method-y veradarcnum e object-i erkarutyuny drakan amboxj tvov:
# if grelu depqum aravelutyuny trvum e __bool__ method-in:   
import os 
# 1
# __del__ kanchvum e ayn jamanak erb jnjum enq object-y, irakanacvum e tsragri avartic heto:
# __delete__ kanchvum e ayn jamanak erb jnjum enq attribute, irakanacvum e minchev tsragri avarty:

# ---- 2 ----
class FileError(Exception):
    def __init__(self, message = "error"):
        self.message = message

    def __str__(self):
        return self.message

class SingleError(FileError):
    def __init__(self, line, file_name):
        self.message = f"there is error on {line} line in {file_name}.txt file"
        
class ManyErrors(FileError):
    def __init__(self, lines, file_name):
        self.message = f"there are error lines on {','.join(lines)} lines in {file_name}.txt files"
        
        
class FileDescriptor:
    def __get__(self, instance, owner):
        with open(f'{instance.__class__.__name__}.txt', 'a') as f:
            return f

    def __set__(self, instance, value):
        with open(f'{instance.__class__.__name__}.txt', 'w') as f:
            return f

    def __delete__(self, instance):
        os.remove(f'{instance.__class__.__name__}.txt')

class ChildFileDescriptor:

    def __get__(self, instance, owner):
        print(owner.__name__)
        file_name = instance.__class__.__name__.lower()
        with open(f"{file_name}.txt", "r") as f:
            error_lines = []    

            for line in f:
                if "error" in line:
                    error_lines.append(line[0])

        if len(error_lines) == 1:
            raise SingleError(error_lines[0], file_name)

        elif len(error_lines) > 1:
            raise ManyErrors(error_lines, file_name)    

class File:
    file = FileDescriptor()
    child_file = ChildFileDescriptor()

class Tesla(File):
    pass

class Lexus(File):
    pass

t = Tesla()
try:
    t.child_file
except FileError as e:
    print(e)    
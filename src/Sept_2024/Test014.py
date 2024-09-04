''' Variables'''
# 1. Local Variable (within the function/block)
# 2. global variable
# 3. instance variable (within the class)
# 4. static variable ( in future)

a = 10 #Global variable

class Person:
    b = 11 # Instance - Belong to class
    c = 11 # Instance - Belong to class

    def print_information(self):
        d = 15 #Local variable - Belong to Function
        global a # Declare it as global with keyword
        a = "Hello"
        print(self.b)
        print(self.c)
        print(d)

object_Ref = Person()
object_Ref.print_information()
print(a)
#print(d)
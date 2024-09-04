'''Constructor - Special Function in Class,  __init__()
It will be automatically called when you create an Object'''

class Person:
    # Attributes
    id = None
    name = None
    age = None
    email = None
    height = None
    gender = None
    phone_no = None
    address = None
    # Behaviour
    def talk(self):  # No Return No Arg  # self - this , self will be first argument in every behaviour.
        print("I can talk")
    def sleep1(self, name):  # Arg with No Return
        print("Arg with No Return")
        print("Sleep", name)
    def sleep2(self, email):  # Arg with Return
        print("Arg with return")
        return None
    def walk(self):
        print("I am walking")
    def walk_return(self):  # No Arg with Return
        return "I am walking"

# Create an Object of the Class
# ObjectRef = ClassName() -> Object
a = Person()
a.name = "tushar"
print(a.name)
a.talk()

b = Person()
b.name = "namita"
print(b.name)
b.walk()

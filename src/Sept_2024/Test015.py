class Car:
    model = None
    name = None
    password = 123

    def __init__(self):
        self.password = "pramod"

    def change_password(self):
        print(self.password)

object_ref = Car()
print(object_ref.password)
print(object_ref.change_password())
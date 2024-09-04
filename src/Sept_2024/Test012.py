class Person:

    def __init__(self):
        self.name = input("Enter the name: ")
        self.age = input("Enter your age: ")
        self.phone = input("Enter your phone: ")
        self.occupation = input("Enter your occupation: ")

    def person_details(self):
        print(f"Name is {self.name}\n Age is {self.age}\n Phone is {self.phone}\n occupation is {self.occupation}")

# Create an Object
person1 = Person()

# Call the Function
person1.person_details()

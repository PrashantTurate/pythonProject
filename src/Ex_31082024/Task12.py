'''Create a Employee Class
A - name,age, phone, address, eid
B - walk, talk, print details,
with the Constructor which will set the values
Ask the user about the information for E1, E2
print the details of the E1, E2 via the print employee functions.
'''

class Employee:

    def __init__(self, name, age, phone, address, eid):
        self.name = name
        self.age = age
        self.phone = phone
        self.address = address
        self.eid = eid

    def walk(self):
        print(f"{self.name}, can walk")

    def talk(self):
        print(f"{self.name}, can talk")

    def print_details(self):
        print(f"Name: {self.name}\n Age: {self.age}\n phone: {self.phone}\n Address: {self.address}\n Eid: {self.eid}")

print("Enter Employee_1 information")
name1 = input("Enter the name: ")
age1 = int(input("Enter the age: "))
phone1 = input("Enter the phone: ")
address1 = input("Enter the address: ")
eid1 = input("Enter the eid: ")

print("Enter Employee_2 information")
name2 = input("Enter the name: ")
age2 = int(input("Enter the age: "))
phone2 = input("Enter the phone: ")
address2 = input("Enter the address: ")
eid2 = input("Enter the eid: ")

Employee_1 = Employee(name1, age1, phone1, address1, eid1)
Employee_2 = Employee(name2, age2, phone2, address2, eid2)

Employee_1.walk()
Employee_1.talk()
Employee_1.print_details()

Employee_2.walk()
Employee_2.talk()
Employee_2.print_details()


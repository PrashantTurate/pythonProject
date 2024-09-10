# Method Overriding - Same name in the parent and child
# child always override the parent functions
# super means call to parent function

class GrandFather:
    a = 10
    def home(self):
        print("Old Home")

class Father(GrandFather):
    b = 20
    def home(self):
        print("1BHK")
        print(self.b)
        print(super().a)

class Son(Father):
    c = 30
    def home(self):
        super().home() # Father Behaviour by super()
        print(super().b) # Father Asttributes by super()
        print("No House")
        print(self.c)

# self - me
# super() - Parent, Super class, Father

s1 = Son()
s1.home()
print(s1.a)
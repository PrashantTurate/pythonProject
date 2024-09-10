# Multilevel Inheritance

class GrandFather:
    diamond = "24 karat"

    def GFhome(self):
        print("1BHK")

class Father(GrandFather):
    gold = "22 karat"

    def Fhome2(self):
        print("2BHK")

class Son(Father):
    silver = "2kg"

    def Shome(self):
        print("3BHK")

s = Son()
s.Shome()
s.GFhome()
print(s.diamond)
f = Father()
f.Fhome2()
f.GFhome()
#f.Shome()       #Not allowed
gf = GrandFather()
gf.GFhome()
#gf.Shome()     #Not allowed
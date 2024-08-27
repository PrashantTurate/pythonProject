'''
Glb = 20
def func():
    a = 10
    print(a)
def func2(Glb):
    Glb = 50
    print(Glb)

func()
func2(Glb)


def Pizza_making(*ingredients):
    for i in ingredients:
        print(i)
print(" program start")
Ajay = Pizza_making("Tomato")
Vijay = Pizza_making("Olives","mushroom","pineapple","sweetcorn")
print(" program end")
'''

my_shoping_list = ["bread", "milk", "butter"]
print(my_shoping_list)

def Add_more(my_list):
    more_item = input("More item: \n")
    my_list.append(more_item)
    return my_list

Final_list = Add_more(my_shoping_list)
print(Final_list)

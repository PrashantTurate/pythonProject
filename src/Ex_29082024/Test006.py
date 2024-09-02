''' List - Collection of Items( Duplicate is allowed)'''

my_list = [2,4,9,16,25,64]
print(my_list)
print(len(my_list))

print(my_list[2])

my_list[0] = "Pramod"
my_list[2] = "Dutta"
my_list[4] = "Dutta2"

print(my_list)
for element in my_list:
    print(element)

my_list.append("Anil")
print(my_list)

my_list.remove("Anil")
print(my_list)

my_list.extend([23,45,67])
print(my_list)

my_list.insert(0,0)
print(my_list)
my_list.pop()
print(my_list)

my_list.reverse()
print(my_list)
my_list = [324,33,98,5,38,12]
my_list.sort(reverse=True)
print(my_list)

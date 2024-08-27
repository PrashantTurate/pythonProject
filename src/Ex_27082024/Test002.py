import math

def sum_three(a,b,c):
   return a+b+c

#p = lambda a,b,c: a+b+c
#print(op(1,2,3))

def give_me_power(num):
    return math.pow(num,2)

a=give_me_power(5)
print(a)

op = lambda num:math.pow(num,2)
print(op(5))

output = lambda:math.pow(int(input("Enter a number: ")),3)
print(output())

def find_odd_even(num):
    if num % 2 == 0:
        print(num, "is an odd number")
    else:
        print(num, "is an even number")

find_odd_even(4)


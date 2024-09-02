'''Tuple - Immutable in nature'''
#from src.Ex_29082024.Test006 import my_list

my_tuple = (1,2,3,4,5)
print(my_tuple)

#my_tuple[2] = 44  #does not support assignment

my_tuple = ('tta.com','sdet.live')
print("Tuple list: ",my_tuple)
my_api_list = list(my_tuple)
print("Tuple conversion to list: " ,my_api_list)
my_api_list = tuple(my_api_list)
print("list conversion to tuple: " ,my_api_list)

# Real case, where we Tuples
API_URLSs = ("https://sdet.live/python0x", "https://awesomeqa.com", "https://thetestingacademy.com")
print(API_URLSs[0])
print(API_URLSs[1])

hero1 = ("Batman", "Bruce Wayne")
hero2 = ("Wonder Woman", "Diana Prince")
new_tuple = (hero1,hero2)
print(new_tuple)
print(new_tuple[0])
print(new_tuple[0][0])
print(new_tuple[1][1])

t = (12, 34, 56)
my_tuple = t + (3,) #append value at the end
print(my_tuple)
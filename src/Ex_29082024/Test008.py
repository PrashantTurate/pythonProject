'''SET - unique - Duplicates are not allowed'''

list_of_unique_items = {1, 2, 3, 4, 4, 5, 5}
print(list_of_unique_items)

list1 = [45.2, 33, 33, 45, 21]
set1 = set(list1)
print(set1)

set1 = {1, 2, 3}
set2 = {4, 5, 6}
my_set = set1.union(set2)
print(my_set)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
my_set = set1.intersection(set2)
print(my_set)

my_set = set1.difference(set2)
#my_set = set2.difference(set1)
print(my_set)


set1 = {1, 2, 3, 4, 5}
set2 = {2, 3, 8}
subset = set2.issubset(set1)
print(subset)
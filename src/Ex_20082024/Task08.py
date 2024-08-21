
'''Write a program that classifies a triangle based on its side lengths. Given three input values representing the lengths of the sides,
determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal),
or scalene (no sides are equal).'''

side1 = input("Enter a side1 length: ")
side2 = input("Enter a side2 length: ")
side3 = input("Enter a side3 length: ")
if side1==side2==side3:
    print(f"Triangle is Equilateral")
elif side1==side2 or side2==side3 or side3==side1:
    print("Triangle is Isosceles")
else:
    print("Triangle is Scalene")

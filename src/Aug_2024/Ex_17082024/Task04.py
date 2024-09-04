import math

# Write a Python program to calculate the area of a circle given its radius using the formula ``` area=π×r^2``` ( Take pie as 3.14)

radius = float(input("Enter a radius of a circle: "))
area = math.pi * math.pow(radius, 2)
area2 = 3.14 * radius ** 2
print("The area of the circle is: ", f"{area:.2f}")
print("The area of the circle is: ", area2)

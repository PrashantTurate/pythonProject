
# Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.

num1 = int(input('Enter a first number: '))
num2 = int(input('Enter a second number: '))
if num1 > num2:
    print("first number is greater than second number")
elif num2 > num1:
    print("second number is greater than first number")
else:
    print("first number is equal to second number")
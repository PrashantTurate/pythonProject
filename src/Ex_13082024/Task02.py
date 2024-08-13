
#Program to take two numbers from user and display maximum of two numbers.
#Program to take two numbers from user and display Summation,Subtraction,Multiplication,Division,Power to exponent
# of two numbers.

num1 = int(input('Enter a first number: '))
num2 = int(input('Enter a second number: '))

print('Maximum of',f"{num1}",'and',f"{num2}",'is: ',max(num1,num2))

print('Summation of',f"{num1}",'and',f"{num2}",'is: ',num1+num2)
print('Subtraction of',f"{num1}",'and',f"{num2}",'is: ',num1-num2)
print('Multiplication of',f"{num1}",'and',f"{num2}",'is: ',num1*num2)
print('Division of',f"{num1}",'by',f"{num2}",'is: ',num1/num2)
print('Power to exponent of',f"{num1}",'raised to',f"{num2}",'is: ',pow(num1,num2))


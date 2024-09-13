# Exceptions

# print(x)  #value not defined error
# print(10/0)  #Division by zero error
# print(1+"1")  #TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(int('a'))  ##ValueError: invalid literal for int() with base 10: 'a'
# my_list = [1,2,3]
# print(my_list[5])  #IndexError: list index out of range
#while True  print("Hello World")   #SyntaxError: invalid syntax
    #print("Check for Indentation")   #IndentationError: unexpected indent

a = int(input("Ent the num1 :"))    # ValueError: invalid literal for int()  (int/string)
b = int(input("Ent the num2 :"))
c = a / b                           # ZeroDivisionError: division by zero    (int/0)

print("Result Div is ", c)

#Exception using Try........Except

print("Start of the program")
try:
    a = int(input("Ent the num1 :"))  # ValueError: invalid literal for int()  (int/string)
    b = int(input("Ent the num2 :"))
    c = a / b  # ZeroDivisionError: division by zero    (int/0)
    print("Result Div is ", c)
except Exception as e:   # e is alias , "Exception" is base Class for all exceptions
    print(e)
    print("Please check your input, it should not be zero or string")
print("End of the program")
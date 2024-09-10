class Calculator:
    def __init__(self):
        print("Basic Calculator")

    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

calc = Calculator()
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
SUM = calc.sum(a, b)
SUB = calc.sub(a, b)
MUL = calc.mul(a, b)
DIV = calc.div(a, b)

print(f"Summation of {a} and {b} is {SUM}\n Subtraction of {a} and {b} is {SUB}\n Multiplication of {a} and {b} is {MUL}\n"
      f"Divison of {a} and {b} is {DIV}")
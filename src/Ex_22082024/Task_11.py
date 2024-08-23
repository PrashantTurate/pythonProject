'''Task #11 -
✅ Fibonaci series 0,0+1, 0+1+1, n = 7 0, 1, 2, 3, 5, 8, 13'''


num = int(input("Enter the number of digits that you want in the Fibonacci sequence: "))
a = 0
b = 1
if num <= 0:
    print("INVALID INPUT")
else:
    print("Fibonacci sequence up to the given terms will be: ")
    print(a, b, end=" ")
    for x in range(2, num):
        c = a + b
        print(c, end=" ")
        a = b
        b = c

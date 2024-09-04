'''Task #10 -
✅ Factorial n = 5 5! -->54321 -> 120 3! -> 321 -> 6 4! -> 432*1 -> 24'''


num=int(input("Enter a Number: "))
fact = 1
if num < 0 :
    print("Factorial does not exist for negative numbers")
elif num == 0 or num == 1:
    print("Factorial is 1")
else:
    for i in range(1,num+1,1):
        fact=fact*i
    print(f"The factorial of number {num} is: {fact}")


'''i = 1
while i <= num:
    fact = fact*i
    i = i + 1
    print(fact)
'''


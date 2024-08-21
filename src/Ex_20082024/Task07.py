
'''Create a program that determines whether a given year is a leap year. A leap year is divisible by 4,
but not by 100 unless it is also divisible by 400'''

Year = int(input("Enter a year: "))
if Year % 400 == 0 and Year % 100 == 0:
    print("Given year is a leap year")
elif Year % 4 == 0 and Year % 100 != 0:
    print("Given year is a leap year")
else:
    print("Given year is a non-leap year")


# How to write to a file

with open('TestData.txt','a') as file:
    file.write(" Hello, How are you? ")

# How to read a file
with open('TestData.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line,end="")

'''
try:
    with open("TestData.txt", "r") as file:
        content = file.readlines()
        print(content)
except FileNotFoundError as fnfr:
    print(fnfr)
finally:
    try:
        file.close()
    except NameError as ne:
        print("NE")
'''
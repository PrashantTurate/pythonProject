'''Dictionary - Unordered collection of data'''

student_information_1 = {
    "name": "Pramod",
    "Age": 55,
    "Address": "Bangalore"
}
print(student_information_1)
print(type(student_information_1))
print(student_information_1["Age"])

student_information_2 = {
    "name": "Amit",
    "Age": 48,
    "Address": "Chennai"
}
student_list = [student_information_1,student_information_2]
print(student_list)
print(student_list[1])
# element_list = []

# #Comprehension Lists
# list_var = [element for element in element_list if conditionals]
# #Comprehension Dictionarys
# dict_var = {key : element for key, element in element_list if conditionals}
# #Comprehension Sets
# set_var = {element for element in element_list if conditionals}

# number_list = list(range(100))
# even_list = [number for number in number_list if number % 2 == 0]
# print(even_list)

# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 
# 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 
# 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]

# #Having two lists:
# list_a = [1, 2, 3]
# list_b = ['a', 'b', 'c']
# #Zip function return a new list combining
# #each element of the lists passed as argument
# zipped = zip(list_a, list_b)
# print(list(zipped))
# "[(1, 'a'), (2, 'b'), (3, 'c')]"

# #Having two lists
# student_uid = [1, 2, 3]
# student = ['Joseph', 'Cesar', 'Jennyfer']
# students = {uid: student for uid, student in zip(student_uid, student)}
# print(students)
# >>>{1: 'Joseph', 2: 'Cesar', 3: 'Jennyfer'}

random_numbers = [2, 9, 8, 9, 6, 1, 1, 5, 3, 4]
numbers = {number for number in random_numbers}
print(numbers)
>>>"{1, 2, 3, 4, 5, 6, 8, 9}"
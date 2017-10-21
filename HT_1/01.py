"""
1 .Write a script which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers. 
        Sample data : 1, 5, 7, 23
        Output : 
        List : [' 1', ' 5', ' 7', ' 23'] 
        Tuple : (' 1', ' 5', ' 7', ' 23')

"""

# string_of_numbers = input("Введите стоку чисел: ")
string_of_numbers = "1, 5, 7, 23"
print ("Строка: " + string_of_numbers)

list_of_numbers = string_of_numbers.split(', ')
print ("Список: " + str(list_of_numbers))

tuple_of_numbers = tuple(string_of_numbers.split(', '))
print ("Кортеж: " + str(tuple_of_numbers))


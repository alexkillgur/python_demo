# 7. Write a script to concatenate all elements in a list into a string and print it.

list_of_values = [1, 5, "bla-bla-bla", 'X', 3]
print ("Исходный массив значений: {}".format(list_of_values))

list_of_strings = list(map(lambda x: str(x), list_of_values))

print ("Конкатенированная строка: {}".format(" ".join(list_of_strings)))


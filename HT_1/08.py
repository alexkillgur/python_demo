"""
8. Write a script to replace last value of tuples in a list. 
        Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
        Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
"""

list_of_tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print ("Исходный массив значений: {}".format(list_of_tuples))

n = 100

modifired_list = list(map(lambda x: x[:-1] + (n,), list_of_tuples))
print ("Модифицированный массив значений: {}".format(modifired_list))


"""
6. Write a script to check whether a specified value is contained in a group of values. 
        Test Data : 
        3 -> [1, 5, 8, 3] : True
        -1 -> (1, 5, 8, 3) : False
"""

array_of_values = [1, 5, 8, 3]
print ("Исходный массив значений: {}".format(array_of_values))

array_of_inputs = [3, -1]
print ("Исходный массив вхождений: {}".format(array_of_inputs))

result = list(map(lambda x: x in array_of_values, array_of_inputs))
print ("Результат проверки вхождений: {}".format(result))


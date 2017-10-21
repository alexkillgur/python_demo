"""
9. Write a script to remove an empty tuple(s) from a list of tuples.
        Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
        Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
"""

list_of_tuples = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
print ("Исходный массив значений: {}".format(list_of_tuples))

modifired_list = list(filter(lambda x: x != (), list_of_tuples))
print ("Модифицированный массив значений: {}".format(modifired_list))


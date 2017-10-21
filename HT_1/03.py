# 3. Write a script to sum of the first n positive integers.

list_of_integers = [-1, 2, 58, -8, 9, 13, -45, 54, -10, -15, 20]
print ("Исходный лист: " + str(list_of_integers))

n = 5

print ("Сумма первых {} положительных элементов: {}".format(n, sum(list(filter(lambda x: x > 0, list_of_integers))[:n])))


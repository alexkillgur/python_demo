# 13. Write a script to get the maximum and minimum value in a dictionary.

dic = {1: 120, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7:60, 8:80, 9:140, 10:100}

print ("Исходный словарь: {}".format(dic))

print ("Минимальное значение: {}".format(dic[min(dic, key=dic.get)]))
print ("Максимальное значение: {}".format(dic[max(dic, key=dic.get)]))


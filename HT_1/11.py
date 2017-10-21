# 11. Write a script to remove duplicates from Dictionary.

dic = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7:60, 8:80, 9:40, 10:100}

print ("Исходный словарь: {}".format(dic))

modifired_dic = {}

for key, value in dic.items():
    if value not in modifired_dic.values():
        modifired_dic[key] = value

print ("Модифицированный словарь: {}".format(modifired_dic))


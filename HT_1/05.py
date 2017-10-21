"""
5. Write a script to convert decimal to hexadecimal
        Sample decimal number: 30, 4
        Expected output: 1e, 04
"""

array_of_integer = [10, 100, 30, 4, 16, 8, 256, 144]
print ("Исходный массив десятичных чисел: {}".format(array_of_integer))

array_of_hex = list(map(lambda x: "{0:x}".format(x), array_of_integer))
#array_of_hex = list(map(lambda x: hex(x).split('x')[-1], array_of_integer))

print ("Полученный массив шестандцатиричных чисел: {}".format(array_of_hex))


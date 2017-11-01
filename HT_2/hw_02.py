import math


# Class that implements switch-case
class Switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        yield self.match
        raise StopIteration

    def match(self, *args):
        if self.fall or not args:
            return True
        elif self.value in args:
            self.fall = True
            return True
        return False


# Class for triangle methods for Task 3
class Rectangle():
    # Checks if all sides of triangle > 0
    @staticmethod
    def is_positive(a, b, c):
        if a > 0 and b > 0 and c > 0:
            return True
        else:
            return False

    # Checks if triangle can exists with this length of sides
    @staticmethod
    def is_triangle(a, b, c):
        if a + b > c and a + c > b and c + b > a:
            return True
        return False

    # Check if triangle has a hypotenuse
    @staticmethod
    def is_hypotenuse_exist(a, b, c):
        if a == math.sqrt(b ** 2 + c ** 2) or b == math.sqrt(a ** 2 + c ** 2) or c == math.sqrt(a ** 2 + b ** 2):
            return True
        else:
            return False


# Demo class for functions
class FuncDemo:
    # Task 1: season by switch
    @staticmethod
    def season_by_switch(num_of_month):
        for case in Switch(num_of_month):
            if case(12, 1, 2):
                print('Winter')
                break
            if case(3, 4, 5):
                print('Spring')
                break
            if case(6, 7, 8):
                print('Summer')
                break
            if case(9, 10, 11):
                print('Autumn')
                break
            if case():
                print('Not a season')

    # Task 1: season by dict
    @staticmethod
    def season_by_dict(num_of_month):
        if num_of_month in range(1, 13):
            return {
                1: 'Winter',
                2: 'Winter',
                3: 'Spring',
                4: 'Spring',
                5: 'Spring',
                6: 'Summer',
                7: 'Summer',
                8: 'Summer',
                9: 'Autumn',
                10: 'Autumn',
                11: 'Autumn',
                12: 'Winter'
            }[num_of_month]
        else:
            return 'Not a season'

    # Task 1: season by if-else
    @staticmethod
    def season_by_if(num_of_month):
        if num_of_month in range(1, 13):
            if num_of_month in range(3, 6):
                print('Spring')
            elif num_of_month in range(6, 9):
                print('Summer')
            elif num_of_month in range(9, 12):
                print('Autumn')
            else:
                print('Winter')
        else:
            print('Not a season')

    # Task 2: default parameters
    @staticmethod
    def parameters_default(first_parameter, second_parameter=None):
        if second_parameter is None:
            return 'No second parameter'
        else:
            return first_parameter + second_parameter

    # Task 3: check if figure with given length of sides is rectangular triangle
    @staticmethod
    def is_rectangular_triangle(a, b, c):
        if Rectangle.is_positive(a, b, c):
            if Rectangle.is_triangle(a, b, c):
                if Rectangle.is_hypotenuse_exist(a, b, c):
                    print('Triangle is rectangular')
                else:
                    print('Triangle is not rectangular')
            else:
                print('Not a triangle')
        else:
            print('Not positive values')

    # Task 4: conditions
    @staticmethod
    def if_else(x, y):
        if x == y:
            print('X equal to Y')
        elif x > y:
            print('X more than Y by', x - y)
        else:
            print('X less than Y by', y - x)

    # Task 5: simple parse given string
    @staticmethod
    def strings(string):
        if isinstance(string, str):
            print('Initial string: {0}'.format(string))
            numbers = list(map(int, filter(lambda digit: digit.isdigit(), string)))
            letters = list(filter(lambda letter: letter.isalpha(), string))
            if len(string) in range(30, 51):
                print('Length: {0}, number of digits: {1}, number of letter: {2} '.format(len(string), len(numbers), len(string) - len(numbers)))
            elif len(string) < 30:
                print('Sum of all digits: {0}, string without digits: {1} '.format(sum(numbers), ''.join(letters)))
            else:
                print('String without letter: {0} '.format(''.join(list(map(str, numbers)))))
            print()
        else:
            print('Not string')

    # Task 6 and 7: some function
    @staticmethod
    def __add(x, y):
        return x + y

    # Task 6 and 7: some function
    @staticmethod
    def __subtract(x, y):
        return x - y

    # Task 6 and 7: some function
    @staticmethod
    def __multiply(x, y):
        return x * y

    # Task 6 and 7: some function
    @staticmethod
    def __divide(x, y):
        return x / y

    # Task 7: calculator
    @staticmethod
    def calculator(x, y, operation):
        dict_of_operation = {
            'add': FuncDemo.__add(x, y),
            'sub': FuncDemo.__subtract(x, y),
            'mul': FuncDemo.__multiply(x, y),
            'div': FuncDemo.__divide(x, y)
        }
        return dict_of_operation.get(operation)


print('------------------------------')
print('TASK #1: three types of season')
print('------------------------------')
FuncDemo.season_by_switch(12)
print(FuncDemo.season_by_dict(5))
FuncDemo.season_by_if(9)
print()
print('--------------------------')
print('TASK #2: default parameter')
print('--------------------------')
print(FuncDemo.parameters_default(10))
print(FuncDemo.parameters_default(10, 14))
print()
print('----------------------------------------')
print('TASK #3: call three function from fourth')
print('----------------------------------------')
FuncDemo.is_rectangular_triangle(9, 4, 5)
FuncDemo.is_rectangular_triangle(8, 4, 5)
FuncDemo.is_rectangular_triangle(3, 4, 5)
print()
print('----------------')
print('TASK #4: if-else')
print('----------------')
FuncDemo.if_else(3, 3)
FuncDemo.if_else(3, 4)
FuncDemo.if_else(5, 3)
print()
print('----------------')
print('TASK #5: strings')
print('----------------')
FuncDemo.strings('f98neroi4nr0c3n30irn03ifek85')
FuncDemo.strings('f98neroi4nr0c3n30irn03ien3c0rfek785')
FuncDemo.strings('f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345')
FuncDemo.strings(12)
print()
print('------------------------')
print('TASKS #6, #7: calculator')
print('------------------------')
print('Adding {0} and {1}: {2} '.format(5, 4, FuncDemo.calculator(5, 4, 'add')))
print('Subtract {0} and {1}: {2} '.format(5, 4, FuncDemo.calculator(5, 4, 'sub')))
print('Multiply {0} and {1}: {2} '.format(5, 4, FuncDemo.calculator(5, 4, 'mul')))
print('Divide {0} and {1}: {2} '.format(5, 4, FuncDemo.calculator(5, 4, 'div')))
print()

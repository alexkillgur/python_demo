import math


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


class Rectangle():
    @staticmethod
    def is_positive(a, b, c):
        if a > 0 and b > 0 and c > 0:
            return True
        else:
            return False

    @staticmethod
    def is_triangle(a, b, c):
        if a + b > c and a + c > b and c + b > a:
            return True
        return False

    @staticmethod
    def is_hypotenuse_exist(a, b, c):
        if a == math.sqrt(b ** 2 + c ** 2) or b == math.sqrt(a ** 2 + c ** 2) or c == math.sqrt(a ** 2 + b ** 2):
            return True
        else:
            return False


class FuncDemo:
    @staticmethod
    def season_by_switch(num_of_month):
        for case in Switch(num_of_month):
            if case(12):
                pass
            if case(1):
                pass
            if case(2):
                print('Winter')
                break
            if case(3):
                pass
            if case(4):
                pass
            if case(5):
                print('Spring')
                break
            if case(6):
                pass
            if case(7):
                pass
            if case(8):
                print('Summer')
                break
            if case(9):
                pass
            if case(10):
                pass
            if case(11):
                print('Autumn')
                break
            if case():
                print('Not a season')

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

    @staticmethod
    def parameters_default(first_parameter, second_parameter=None):
        if second_parameter is None:
            return 'No second parameter'
        else:
            return first_parameter + second_parameter

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

    @staticmethod
    def if_else(x, y):
        if x == y:
            print('X equal to Y')
        elif x > y:
            print('X more than Y by', x - y)
        else:
            print('X less than Y by', y - x)


funcDemo = FuncDemo()
print('Function #1: three types of season')
FuncDemo.season_by_switch(12)
print(FuncDemo.season_by_dict(5))
FuncDemo.season_by_if(9)
print()
print('Function #2: default parameter')
print(FuncDemo.parameters_default(10))
print(FuncDemo.parameters_default(10, 14))
print()
print('Function #3: call three function from fourth')
FuncDemo.is_rectangular_triangle(9, 4, 5)
FuncDemo.is_rectangular_triangle(8, 4, 5)
FuncDemo.is_rectangular_triangle(3, 4, 5)
print()
print('Function #4: if-else')
FuncDemo.if_else(3, 3)
FuncDemo.if_else(3, 4)
FuncDemo.if_else(5, 3)
print()

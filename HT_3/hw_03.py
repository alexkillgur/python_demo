import random
from time import time

SIZE = 100000


def get_random_int(min_value=0, max_value=99):
    return random.randint(min_value, max_value)


def get_random_float(min_value=0, max_value=99):
    return random.uniform(min_value, max_value)


def get_array_int(size=SIZE, random_seed=17):
    random.seed(random_seed)
    return [get_random_int() for i in range(size)]


def get_array_float(size=SIZE, random_seed=17):
    random.seed(random_seed)
    return [get_random_float() for i in range(size)]


def get_arrays(size=SIZE, random_seed=17):
    return get_array_int(size, random_seed), get_array_float(size, random_seed)


def selection_sort_algorithm(list_to_sort):
    for first_ind in range(len(list_to_sort)-1):
        min_ind = first_ind

        for second_ind in range(first_ind+1, len(list_to_sort)):
            if list_to_sort[second_ind] < list_to_sort[min_ind]:
                min_ind = second_ind

        if min_ind != first_ind:
            list_to_sort[first_ind], list_to_sort[min_ind] = list_to_sort[min_ind], list_to_sort[first_ind]

    return list_to_sort


def insertion_sort_algorithm(list_to_sort):
    for ind in range(1, len(list_to_sort)):
        value_to_insert = list_to_sort[ind]
        hole_position = ind

        while hole_position > 0 and list_to_sort[hole_position-1] > value_to_insert:
            list_to_sort[hole_position] = list_to_sort[hole_position-1]
            hole_position = hole_position - 1

        list_to_sort[hole_position] = value_to_insert

    return list_to_sort


def bubble_sort_algorithm(list_to_sort):
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for ind in range(len(list_to_sort)-1):
            if list_to_sort[ind] > list_to_sort[ind+1]:
                is_sorted = False
                list_to_sort[ind], list_to_sort[ind+1] = list_to_sort[ind+1], list_to_sort[ind]

    return list_to_sort


def python_sort_algorithm(list_to_sort):
    list_to_sort.sort()
    return list_to_sort


def time_measurement(list_to_measure):
    measurement = {
        'selection sort': selection_sort_algorithm,
        'insertion sort': insertion_sort_algorithm,
        'bubble sort   ': bubble_sort_algorithm
    }

    for key, value in measurement.items():
        start_time = time()
        sorted_list = value(list_to_measure.copy())
        end_time = time()
        print(key + ': time = ' + '{0:02.0f}:{1:07.4f}'.format(*divmod((end_time - start_time), 60)) +
              ', the list is sorted correctly = ' + str(sorted_list == python_sort_algorithm(list_to_measure.copy())))

list_of_int, list_of_float = get_arrays()

print('List of integers: ')
time_measurement(list_of_int)
print()
print('List of float: ')
time_measurement(list_of_float)

# Output
# List of integers:
# selection sort: time = 10:22.7429, the list is sorted correctly = True
# insertion sort: time = 12:37.8713, the list is sorted correctly = True
# bubble sort   : time = 34:34.5917, the list is sorted correctly = True
#
# List of float:
# selection sort: time = 10:32.3705, the list is sorted correctly = True
# insertion sort: time = 13:42.9454, the list is sorted correctly = True
# bubble sort   : time = 39:42.1056, the list is sorted correctly = True
import numpy as np
import random

"""
def generate(n, w, s, output_file):
n - number of objects to choose (int)
w - maximum carrying capacity of the knapsack (int)
s - maximum knapsack size (int)
output_file - name of the file into which the task is to be save
"""


def generate(n, w, s, output_file):
    initialized_arrays = initialize_arrays(n, w, s)
    w_i = initialized_arrays[0]
    s_i = initialized_arrays[1]
    c_i = initialized_arrays[2]

    w_i_min = 2 * w
    s_i_min = 2 * s
    w_i_max = np.ceil(10 * w / n)
    s_i_max = np.ceil(10 * s / n)

    # generate random values
    generate_random_values(n, w_i, w_i_max, s_i, s_i_max, c_i)

    # check if weights and sizes fulfill conditions for sum of their elements and update them if needed
    update_weights_if_needed(w_i, w_i_min, w_i_max)
    update_sizes_if_needed(s_i, s_i_min, s_i_max)

    save_data_to_csv([row for row in zip(w_i, s_i, c_i)], output_file)
    return 1


def generate_random_values(n, w_i, w_i_max, s_i, s_i_max, c_i):
    for i in range(1, n + 1):
        w_i[i] = random.randrange(1, w_i_max)
        s_i[i] = random.randrange(1, s_i_max)
        c_i[i] = random.randrange(1, n)


def initialize_arrays(n, w, s):
    w_i = np.empty(n + 1)
    s_i = np.empty(n + 1)
    c_i = np.empty(n + 1)

    # initialize first row for the file
    w_i[0] = n
    s_i[0] = w
    c_i[0] = s
    return w_i, s_i, c_i


def update_weights_if_needed(w_i, w_i_min, w_i_max):
    if not is_correct_sum_of_elements(w_i, w_i_min):
        print('Update for weights is needed!')
        increase_values_for_elements(w_i, w_i_min, w_i_max)


def update_sizes_if_needed(s_i, s_i_min, s_i_max):
    if not is_correct_sum_of_elements(s_i, s_i_min):
        print('Update for sizes is needed!')
        increase_values_for_elements(s_i, s_i_min, s_i_max)


def is_correct_sum_of_elements(values_array, minimal_value):
    return sum(values_array) > minimal_value


def increase_values_for_elements(values_array, minimal_value, maximal_value):
    while not is_correct_sum_of_elements(values_array, minimal_value):
        for value in values_array:
            if value * 2 <= maximal_value:
                value *= 2


def save_data_to_csv(data, output_file):
    np.savetxt(output_file, data, delimiter=',', fmt='%i')

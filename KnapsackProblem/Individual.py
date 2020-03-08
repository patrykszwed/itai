import numpy as np
from constants import *


def get_task_value_to_sum(task, value_to_sum):
    return {
        'w_i': task.w_i,
        's_i': task.s_i,
        'c_i': task.c_i
    }[value_to_sum]


class Individual:
    n_items = 0
    task = 0
    items_array = np.empty(n_items)

    def __init__(self, task, items_array):
        self.n_items = task.n_items
        self.items_array = items_array
        self.task = task

    def evaluate(self):
        if self.get_total_sum_of_value('w_i') >= MAXIMUM_WEIGHT \
                or self.get_total_sum_of_value('s_i') >= MAXIMUM_SIZE:
            return 0
        return self.get_total_sum_of_value('c_i')

    def get_total_sum_of_value(self, value_to_sum):
        total_sum = 0
        task_value = get_task_value_to_sum(self.task, value_to_sum)
        for index in range(len(self.items_array)):
            if self.items_array[index] == 1:
                total_sum += task_value[index]
        return total_sum

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
    items_array = 0

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
        task_value = get_task_value_to_sum(self.task, value_to_sum)
        filter_array = self.items_array == 1
        filtered_array = task_value[filter_array]
        return np.sum(filtered_array)

import random


def get_random_indexes_from_array(array, number_of_indexes_to_pick):
    already_picked_indexes = []
    random_indexes = []
    # print('number_of_indexes_to_pick = ', number_of_indexes_to_pick)
    while len(random_indexes) < number_of_indexes_to_pick:
        # print('len(random_indexes) ', len(random_indexes))
        # print('len(array) =', len(array))
        picked_index = random.randrange(0, len(array))
        # print('picked_index = ', picked_index)
        if picked_index not in already_picked_indexes:
            # print('Index ', picked_index, ' was not picked yet!')
            random_indexes.append(picked_index)
            already_picked_indexes.append(picked_index)
    return random_indexes


# def get_constant_to_change(constant_to_change):
#     return {
#         'CROSSOVER_RATE': task.w_i,
#         'MUTATION_RATE': task.s_i,
#         'c_i': task.c_i
#     }[constant_to_change]

import random


def get_random_indexes_from_array(array, number_of_indexes_to_pick):
    already_picked_indexes = []
    random_indexes = []
    while len(random_indexes) < number_of_indexes_to_pick:
        picked_index = random.randrange(0, len(array))
        if picked_index not in already_picked_indexes:
            random_indexes.append(picked_index)
        else:
            already_picked_indexes.append(picked_index)
    return random_indexes

import numpy as np


def transform_dictionary_to_vector(dictionary):
    vector = []
    for key in dictionary.keys():
        vector.append(key)
        vector.append(dictionary[key])
    return vector


def is_correct_letter(letter):
    return letter.isalpha() or letter == '\''


def save_data_to_arff(data, output_file):
    np.savetxt(output_file, data, delimiter=',', fmt='%s', encoding='utf-8')

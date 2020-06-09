import numpy as np

from constants import K, QUOTE_SIGN, cats


def transform_dictionary_to_vector(dictionary):
    vector = []
    for key in dictionary.keys():
        vector.append(key)
        vector.append(dictionary[key])
    return vector


def is_correct_letter(letter):
    return letter.isalnum()


def is_correct_word(word):
    return len(word) > 0 and word.isalnum() and word.count(QUOTE_SIGN) <= 1


def save_data_to_arff(data, output_file):
    np.savetxt(output_file, data, delimiter=',', fmt='%s', encoding='utf-8')


def append_arff_relation_header(vectors_for_each_document):
    vectors_for_each_document.insert(0, '@RELATION docCategory')
    return vectors_for_each_document


def append_arff_attributes_headers(vectors_for_each_document, k_most_frequent_words_vector):
    k_most_frequent_words = k_most_frequent_words_vector[::2]
    vectors_for_each_document.insert(0,
                                     '@ATTRIBUTE category_class {' + ','.join(cats) + '}')
    idx = 0
    while idx < K:
        vectors_for_each_document.insert(0, '@ATTRIBUTE ' + k_most_frequent_words[idx] + ' NUMERIC')
        idx += 1

    return vectors_for_each_document


def append_arff_data_header(vectors_for_each_document):
    vectors_for_each_document.insert(0, '@DATA')
    return vectors_for_each_document


def append_arff_header_to_vectors_file(vectors_for_each_document, k_most_frequent_words_vector):
    vectors_for_each_document = append_arff_data_header(vectors_for_each_document)
    vectors_for_each_document = append_arff_attributes_headers(vectors_for_each_document, k_most_frequent_words_vector)
    vectors_for_each_document = append_arff_relation_header(vectors_for_each_document)
    return vectors_for_each_document

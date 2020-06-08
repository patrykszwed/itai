import numpy as np

from constants import K, QUOTE_SIGN


def quote(word):
    print('word = ', word)
    if word.startswith(QUOTE_SIGN) and word.endswith(QUOTE_SIGN):
        return word[1:len(word) - 1]
    if word.startswith(QUOTE_SIGN):
        return word[1:]
    if word.endswith(QUOTE_SIGN):
        return word[:len(word) - 1]
    quote_sign_index = word.index(QUOTE_SIGN)
    first_part_of_word = word[:quote_sign_index]
    second_part_of_word = word[quote_sign_index + 1:]
    return QUOTE_SIGN + first_part_of_word + '\\' + QUOTE_SIGN + second_part_of_word + QUOTE_SIGN


def transform_dictionary_to_vector(dictionary):
    vector = []
    for key in dictionary.keys():
        vector.append(key)
        vector.append(dictionary[key])
    return vector


def is_correct_letter(letter):
    return letter.isalpha()  # or letter == QUOTE_SIGN or letter == '-'


def is_correct_word(word):
    return len(word) > 0 and word.count(QUOTE_SIGN) <= 1


def save_data_to_arff(data, output_file):
    np.savetxt(output_file, data, delimiter=',', fmt='%s', encoding='utf-8')


def append_arff_relation_header(vectors_for_each_document):
    vectors_for_each_document.insert(0, '@relation documentCategory')
    return vectors_for_each_document


def append_arff_attributes_headers(vectors_for_each_document):
    idx = K - 1
    while idx >= 0:
        vectors_for_each_document.insert(0, '@attribute frequency_of_w' + str(idx) + ' integer')
        vectors_for_each_document.insert(0, '@attribute word_' + str(idx) + ' string')
        idx -= 1
    vectors_for_each_document.insert(0,
                                     '@attribute class {alt.atheism,comp.graphics,rec.autos,sci.med,talk.politics.guns}')
    vectors_for_each_document.insert(0,
                                     '@attribute doc_id integer')
    return vectors_for_each_document


def append_arff_data_header(vectors_for_each_document):
    vectors_for_each_document.insert(0, '@data')
    return vectors_for_each_document


def append_arff_header_to_vectors_file(vectors_for_each_document):
    vectors_for_each_document = append_arff_data_header(vectors_for_each_document)
    vectors_for_each_document = append_arff_attributes_headers(vectors_for_each_document)
    vectors_for_each_document = append_arff_relation_header(vectors_for_each_document)
    return vectors_for_each_document

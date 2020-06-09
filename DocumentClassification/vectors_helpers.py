from pprint import pprint

from helpers import transform_dictionary_to_vector, is_correct_letter, quote, is_correct_word
from constants import K, QUOTE_SIGN


def get_doc_words(docs_bodies):
    words_split = docs_bodies.split()
    words = []
    words_split.append(',')
    for word in words_split:
        new_word = ''
        for i in range(len(word)):
            letter = word[i]
            if is_correct_letter(letter):
                new_word += letter
        if is_correct_word(new_word):
            if new_word.find(QUOTE_SIGN) != -1:
                print('Word before quote =', new_word)
                new_word = quote(new_word)
                print('Word after quote =', new_word)
            words.append(new_word)
    return words


def get_word_frequencies_dicts(docs_words):
    word_frequencies_dicts = []
    for doc_words in docs_words:
        word_frequencies_dictionary = {}
        for word in doc_words:
            if word in word_frequencies_dictionary:
                word_frequency = word_frequencies_dictionary[word]
                word_frequencies_dictionary[word] = word_frequency + 1
            else:
                word_frequencies_dictionary[word] = 1
        word_frequencies_dicts.append(word_frequencies_dictionary)
    return word_frequencies_dicts


def get_docs_words(docs_bodies):
    docs_words = []
    for doc_body in docs_bodies:
        doc_words = get_doc_words(doc_body)
        if len(doc_words) > 0:
            docs_words.append(doc_words)
    return docs_words


def get_ready_vectors(word_frequencies_dicts, docs_categories_labels,
                      docs_categories_names):
    # pprint(docs_categories_labels)
    # pprint(docs_categories_names)
    ready_vectors = []
    for idx, word_frequencies_dict in enumerate(word_frequencies_dicts):
        word_frequencies_vector = [idx, docs_categories_names[idx], word_frequencies_dict]
        ready_vectors.append(word_frequencies_vector)
    return ready_vectors


def get_docs_vectors(newsgroups_train):
    newsgroups_train_labels_map = dict(enumerate(newsgroups_train.target_names))
    print('newsgroups_train_labels_map', newsgroups_train_labels_map)

    docs_bodies, docs_categories_labels, docs_categories_names = (newsgroups_train.data, newsgroups_train.target,
                                                                  [newsgroups_train_labels_map[label] for label in
                                                                   newsgroups_train.target])  # docs_categories_labels - category id
    docs_words = get_docs_words(docs_bodies)
    word_frequencies_dicts = get_word_frequencies_dicts(docs_words)
    ready_vectors = get_ready_vectors(word_frequencies_dicts,
                                      docs_categories_labels,
                                      docs_categories_names)
    return ready_vectors


def get_sorted_dicts_by_words_count(most_frequent_words):
    return {k: v for k, v in sorted(most_frequent_words.items(), key=lambda item: item[1])}


def get_k_most_frequent_words_vector(vector):
    return vector[-K * 2:]  # multiplied by 2 as we take word-count pairs


def get_k_most_frequent_words(vectors):
    most_frequent_words = {}
    for vector in vectors:
        words_dict = vector[2]
        for word in words_dict:
            count = words_dict[word]
            if word in most_frequent_words:
                most_frequent_words[word] += count
            else:
                most_frequent_words[word] = count
    sorted_dicts_by_words_count = get_sorted_dicts_by_words_count(most_frequent_words)
    vector = transform_dictionary_to_vector(sorted_dicts_by_words_count)
    k_most_frequent_words_vector = get_k_most_frequent_words_vector(vector)
    return k_most_frequent_words_vector, sorted_dicts_by_words_count


def get_most_frequent_words_for_document_category(most_frequent_words_for_each_category, category):
    for most_frequent_words_for_category in most_frequent_words_for_each_category:
        if most_frequent_words_for_category[0] == category:
            return get_k_most_frequent_words_vector(most_frequent_words_for_category)
    return None


# def get_vectors_for_each_document(word_vectors, most_frequent_words):
#     vectors_for_each_document = []
#     i = 0
#     for word_vector in word_vectors:
#         # print('word_vector', word_vector)
#         category = word_vector[1]
#         vector_for_one_document = [i, category]
#         docs_words_frequencies = word_vector[2]
#         word_idx = 0
#         while word_idx < len(most_frequent_words):
#             most_frequent_word = most_frequent_words[word_idx]
#             count = 0
#             if most_frequent_word in docs_words_frequencies:
#                 # count = docs_words_frequencies[docs_words_frequencies.index(most_frequent_word) + 1]
#                 count = docs_words_frequencies[most_frequent_word]
#                 vector_for_one_document.append(most_frequent_word)
#                 vector_for_one_document.append(count)
#             word_idx += 2
#         # vector_for_one_document = transform_dictionary_to_vector(vector_for_one_document)
#         # print('len(vector_for_one_document)', len(vector_for_one_document))
#         # print('vector_for_one_document', vector_for_one_document)
#         vectors_for_each_document.append(vector_for_one_document)
#         i += 1
#     return vectors_for_each_document


def get_doc_words_number(docs_words_frequencies):
    doc_words_number = 0
    for doc_words_frequencies in docs_words_frequencies:
        doc_words_number += docs_words_frequencies[doc_words_frequencies]
    return doc_words_number


def get_vectors_for_each_document(word_vectors, most_frequent_words):
    vectors_for_each_document = []
    i = 0
    for word_vector in word_vectors:
        # print('word_vector', word_vector)
        category = word_vector[1]
        vector_for_one_document = '' + str(i) + ',' + category + ','
        docs_words_frequencies = word_vector[2]
        doc_words_number = get_doc_words_number(docs_words_frequencies)
        word_idx = 0
        # print('doc_words_number', doc_words_number)
        while word_idx < len(most_frequent_words):
            most_frequent_word = most_frequent_words[word_idx]
            count = 0
            if most_frequent_word in docs_words_frequencies:
                count = docs_words_frequencies[most_frequent_word]
            # vector_for_one_document += most_frequent_word + ','
            vector_for_one_document += str(count) + ','
            word_idx += 2
        if vector_for_one_document[len(vector_for_one_document) - 1] == ',':
            vector_for_one_document = vector_for_one_document[:len(vector_for_one_document) - 1]
        vectors_for_each_document.append(vector_for_one_document)
        i += 1
    return vectors_for_each_document

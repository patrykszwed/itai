from pprint import pprint

from helpers import transform_dictionary_to_vector, is_correct_letter
from constants import K


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
        if len(new_word) > 0:
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


def get_sorted_dicts_by_words_count(most_frequent_words_for_each_category_dict):
    k_most_frequent_words_for_each_category_dict = {}
    for category in most_frequent_words_for_each_category_dict:
        most_frequent_words_dict = most_frequent_words_for_each_category_dict[category]
        sorted_words_by_count = {k: v for k, v in sorted(most_frequent_words_dict.items(), key=lambda item: item[1])}
        k_most_frequent_words_for_each_category_dict[category] = sorted_words_by_count
    return k_most_frequent_words_for_each_category_dict


def get_k_most_frequent_words_vector(vector):
    return vector[-K * 2:]  # multiplied by 2 as we take word-count pairs


def get_most_frequent_words_for_each_category(vectors):
    most_frequent_words_for_each_category = []
    most_frequent_words_for_each_category_dict = {}
    for vector in vectors:
        category = vector[1]
        most_frequent_words_for_one_category = {}
        if category in most_frequent_words_for_each_category_dict:
            most_frequent_words_for_one_category = most_frequent_words_for_each_category_dict[category]
        else:
            most_frequent_words_for_each_category_dict[category] = most_frequent_words_for_one_category
        words_dict = vector[2]
        for word in words_dict:
            count = words_dict[word]
            if word in most_frequent_words_for_one_category:
                most_frequent_words_for_one_category[word] += count
            else:
                most_frequent_words_for_one_category[word] = count
    sorted_dicts_by_words_count = get_sorted_dicts_by_words_count(
        most_frequent_words_for_each_category_dict)
    for category in sorted_dicts_by_words_count:
        print('category', category)
        vector = transform_dictionary_to_vector(sorted_dicts_by_words_count[category])
        print('len(vector)', len(vector))
        k_most_frequent_words_vector = get_k_most_frequent_words_vector(vector)
        print('len(k_most_frequent_words_vector)', len(k_most_frequent_words_vector))
        k_most_frequent_words_vector.insert(0, category)
        most_frequent_words_for_each_category.append(k_most_frequent_words_vector)
    return most_frequent_words_for_each_category

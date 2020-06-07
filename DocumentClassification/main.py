from sklearn.datasets import fetch_20newsgroups
from pprint import pprint


def is_correct_letter(letter):
    return letter.isalpha() or letter == '\''


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


def transform_dictionary_to_vector(word_frequencies_dictionary):
    vector = []
    for key in word_frequencies_dictionary.keys():
        vector.append(key)
        vector.append(word_frequencies_dictionary[key])
    return vector


def get_word_frequencies_vectors(docs_words):
    word_frequencies_vectors = []
    for doc_words in docs_words:
        word_frequencies_dictionary = {}
        # print('doc_words', doc_words)
        for word in doc_words:
            # print('word', word)
            if word in word_frequencies_dictionary:
                word_frequency = word_frequencies_dictionary[word]
                word_frequencies_dictionary[word] = word_frequency + 1
            else:
                word_frequencies_dictionary[word] = 1
        # print('word_frequencies_dictionary', word_frequencies_dictionary)
        doc_word_frequencies_vectors = transform_dictionary_to_vector(word_frequencies_dictionary)
        # print('doc_word_frequencies_vectors', doc_word_frequencies_vectors)
        word_frequencies_vectors.append(doc_word_frequencies_vectors)
    return word_frequencies_vectors


def get_docs_words(docs_bodies):
    docs_words = []
    for doc_body in docs_bodies:
        doc_words = get_doc_words(doc_body)
        if len(doc_words) > 0:
            docs_words.append(doc_words)
    return docs_words


def get_ready_vectors(word_frequencies_vectors, docs_categories_labels,
                      docs_categories_names):
    pprint(docs_categories_labels)
    pprint(docs_categories_names)
    ready_vectors = []
    for idx, word_frequencies_vector in enumerate(word_frequencies_vectors):
        word_frequencies_vector.insert(0, idx)
        word_frequencies_vector.insert(1, docs_categories_names[idx])
        ready_vectors.append(word_frequencies_vector)
    return ready_vectors


def convert_docs_to_vectors(newsgroups_train):
    newsgroups_train_labels_map = dict(enumerate(newsgroups_train.target_names))
    print('newsgroups_train_labels_map', newsgroups_train_labels_map)

    docs_bodies, docs_categories_labels, docs_categories_names = (newsgroups_train.data, newsgroups_train.target,
                                                                  [newsgroups_train_labels_map[label] for label in
                                                                   newsgroups_train.target])  # docs_categories_labels - category id
    docs_words = get_docs_words(docs_bodies)
    word_frequencies_vectors = get_word_frequencies_vectors(docs_words)
    ready_vectors = get_ready_vectors(word_frequencies_vectors,
                                      docs_categories_labels,
                                      docs_categories_names)
    return ready_vectors


cats = ['comp.graphics', 'rec.autos', 'sci.med', 'talk.politics.guns', 'alt.atheism']
newsgroups_train = fetch_20newsgroups(subset='train', remove=('headers', 'footers', 'quotes'), categories=cats)

vectors = convert_docs_to_vectors(newsgroups_train)
print('vectors[0]', vectors[0])
# print(vectors)

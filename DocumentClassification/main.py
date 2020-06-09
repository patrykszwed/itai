from sklearn.datasets import fetch_20newsgroups

from helpers import save_data_to_arff, append_arff_header_to_vectors_file
from vectors_helpers import get_docs_vectors, get_k_most_frequent_words, get_vectors_for_each_document
from constants import cats


def generate_arff_file(subset_name):
    newsgroups_train = fetch_20newsgroups(subset=subset_name, remove=('headers', 'footers', 'quotes'), categories=cats)

    vectors = get_docs_vectors(newsgroups_train)
    k_most_frequent_words_vector, dicts_by_words_count = get_k_most_frequent_words(vectors)
    vectors_for_each_document = get_vectors_for_each_document(vectors, k_most_frequent_words_vector)

    vectors_for_each_document = append_arff_header_to_vectors_file(vectors_for_each_document,
                                                                   k_most_frequent_words_vector)

    save_data_to_arff(vectors_for_each_document, 'dataset.arff')


generate_arff_file('train')

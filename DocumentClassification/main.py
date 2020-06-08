import numpy as np
from sklearn.datasets import fetch_20newsgroups
from pprint import pprint

from helpers import save_data_to_arff, append_arff_header_to_vectors_file
from vectors_helpers import get_docs_vectors, get_k_most_frequent_words, get_vectors_for_each_document

cats = ['comp.graphics', 'rec.autos', 'sci.med', 'talk.politics.guns', 'alt.atheism']
newsgroups_train = fetch_20newsgroups(subset='train', remove=('headers', 'footers', 'quotes'), categories=cats)

vectors = get_docs_vectors(newsgroups_train)
k_most_frequent_words_vector, dicts_by_words_count = get_k_most_frequent_words(vectors)
vectors_for_each_document = get_vectors_for_each_document(vectors, k_most_frequent_words_vector)

vectors_for_each_document = append_arff_header_to_vectors_file(vectors_for_each_document)
save_data_to_arff(vectors_for_each_document[:20008], 'docs_vectors.arff')

save_data_to_arff(k_most_frequent_words_vector, 'most_frequent_words.arff')

import numpy as np
from sklearn.datasets import fetch_20newsgroups
from pprint import pprint

from helpers import save_data_to_arff
from vectors_helpers import get_docs_vectors, get_most_frequent_words_for_each_category

cats = ['comp.graphics', 'rec.autos', 'sci.med', 'talk.politics.guns', 'alt.atheism']
newsgroups_train = fetch_20newsgroups(subset='train', remove=('headers', 'footers', 'quotes'), categories=cats)

vectors = get_docs_vectors(newsgroups_train)
most_frequent_words_for_each_category = get_most_frequent_words_for_each_category(vectors)

save_data_to_arff(vectors, 'words_vectors')
save_data_to_arff(most_frequent_words_for_each_category, 'most_frequent_words')

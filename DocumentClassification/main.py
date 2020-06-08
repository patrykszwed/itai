import numpy as np
from sklearn.datasets import fetch_20newsgroups
from pprint import pprint

from helpers import save_data_to_arff
from vectors_helpers import get_docs_vectors, get_most_frequent_words_for_each_category, get_vectors_for_each_document

cats = ['comp.graphics', 'rec.autos', 'sci.med', 'talk.politics.guns', 'alt.atheism']
newsgroups_train = fetch_20newsgroups(subset='train', remove=('headers', 'footers', 'quotes'), categories=cats)

vectors = get_docs_vectors(newsgroups_train)
most_frequent_words_for_each_category, dicts_by_words_count = get_most_frequent_words_for_each_category(vectors)
vectors_for_each_document = get_vectors_for_each_document(vectors, most_frequent_words_for_each_category)
print('len(vectors_for_each_document', len(vectors_for_each_document))
save_data_to_arff(vectors_for_each_document, 'docs_vectors')
# print('most_frequent_words_for_each_category[0] = ', len(most_frequent_words_for_each_category[0]))
# for word in most_frequent_words_for_each_category[0]:
#     print('word = ', word)
save_data_to_arff(most_frequent_words_for_each_category, 'most_frequent_words')

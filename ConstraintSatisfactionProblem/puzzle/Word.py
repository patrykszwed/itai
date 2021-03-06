from puzzle.fields_helpers import find_empty_fields


def init_words_domains(crossword):
    for word in crossword.words:
        word.init_domain(crossword)


class Word:
    def __init__(self, word):
        self.value = word
        self.domain = 0

    def init_domain(self, crossword):
        empty_fields = find_empty_fields(crossword, self.value)
        self.domain = empty_fields

    value = 0
    domain = []

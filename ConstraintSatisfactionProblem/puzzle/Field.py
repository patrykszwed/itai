class Field:
    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y
        self.domain = []
        self.contained_words = []

    # def calculate_domain(self, row, column, subgrid):
    #     initial_domain = []
    #     domain_to_check = get_fields_values(row) + get_fields_values(column) + get_fields_values(subgrid)
    #     for value in range(1, 10):
    #         if value not in domain_to_check:
    #             initial_domain.append(value)
    #     self.domain = initial_domain

    def add_word_to_contained_words(self, word):
        if self.y == 2 and self.x == 2:
            print('Y = 2 add word', word)
            print('self.contained_words', self.contained_words)
        if word not in self.contained_words:
            self.contained_words.append(word)

    def remove_word_from_contained_words(self, word):
        if word in self.contained_words:
            self.contained_words.remove(word)

    def print(self):
        print('Field location: [', self.x, ',', self.y, '], value:', self.value)

    value = 0
    x = 0
    y = 0
    contained_words = []
    domain = 0

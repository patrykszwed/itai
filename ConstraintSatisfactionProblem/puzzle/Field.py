class Field:
    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y
        self.contained_words = []

    def add_word_to_contained_words(self, word):
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

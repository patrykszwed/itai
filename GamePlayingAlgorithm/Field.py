class Field:
    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y

    def print(self):
        print('Field location: [', self.x, ',', self.y, '], value:', self.value)

    value = 0
    x = 0
    y = 0

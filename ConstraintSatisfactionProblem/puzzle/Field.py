class Field:
    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y
        self.domain = []

    # def calculate_domain(self, row, column, subgrid):
    #     initial_domain = []
    #     domain_to_check = get_fields_values(row) + get_fields_values(column) + get_fields_values(subgrid)
    #     for value in range(1, 10):
    #         if value not in domain_to_check:
    #             initial_domain.append(value)
    #     self.domain = initial_domain

    def print(self):
        print('Field location: [', self.x, ',', self.y, '], value:', self.value)

    value = 0
    x = 0
    y = 0
    domain = 0

from puzzle.Column import Column
from puzzle.Field import Field
from puzzle.Row import Row


def update_values(crossword, fields, word, is_set_to_zero):
    for i in range(len(fields)):
        field = fields[i]
        column = crossword.columns[field.x]
        column.fields[field.y].value = '_' if is_set_to_zero else word[i]
        row = crossword.rows[field.y]
        row.fields[field.x].value = '_' if is_set_to_zero else word[i]


def get_fields(rows):
    fields = []
    for i in range(9):
        row_fields = rows[i].fields
        for j in range(len(row_fields)):
            fields.append(row_fields[j])
    return fields


class Crossword:
    def __init__(self, crossword_data, words_data, difficulty):
        # print('init crossword_data', crossword_data)
        self.number_of_rows = len(crossword_data)
        # print('self.number_of_rows', self.number_of_rows)
        self.number_of_columns = len(crossword_data[0])
        # print('self.number_of_columns', self.number_of_columns)
        self.difficulty = difficulty
        self.rows = self.get_rows(crossword_data)
        self.columns = self.get_columns(self.rows)
        # print('self.columns', self.columns)
        words_data.sort(key=len, reverse=True)
        self.words = [word for word in words_data]
        print('self.words', self.words)

    def get_rows(self, crossword_data):
        rows = []
        for i in range(self.number_of_rows):
            fields = []
            for j in range(self.number_of_columns):
                fields.append(Field(crossword_data[i][j], j, i))
            rows.append(Row(i, fields))
        return rows

    def get_columns(self, rows):
        fields = []
        for i in range(self.number_of_columns):
            fields.append([])
        for i in range(self.number_of_rows):
            row_fields = rows[i].fields
            for j in range(self.number_of_columns):
                fields[j].append(row_fields[j])
        columns = []
        for i in range(self.number_of_columns):
            columns.append(Column(i, fields[i]))
        return columns

    difficulty = 0
    columns = []
    number_of_columns = 0
    rows = []
    number_of_rows = 0
    fields = []
    backtrack_steps = 0

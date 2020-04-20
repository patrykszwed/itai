from puzzle.Task import Task


def read_puzzle():
    crosswords_data = []
    words_data = []
    for i in range(5):
        crossword_file = f'D:\Studia\AI\ConstraintSatisfactionProblem\data\Jolka\puzzle{i}'
        crosswords_data.append(open(crossword_file, 'r').read().splitlines())
        words_file = f'D:\Studia\AI\ConstraintSatisfactionProblem\data\Jolka\words{i}'
        words_data.append(open(words_file, 'r').read().splitlines())
    return Task([list(t) for t in crosswords_data], [list(t) for t in words_data])

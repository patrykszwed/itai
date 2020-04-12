import numpy as np


class Task:
    def __init__(self, games_data):
        self.number_of_games = len(games_data)
        self.games_data = np.asarray(games_data)

    number_of_games = 0
    games_data = np.asarray(0)

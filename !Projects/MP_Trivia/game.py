from connection import TriviaConnection
from user import User
from interface import ask_question, choose_user
import pandas as pd
import pickle
from tabulate import tabulate


class Game:
    users = []

    @staticmethod
    def select_user():
        user = choose_user(Game.users)
        if user:
            return user
        else:
            user = User(input('Enter player name: '))
            Game.users.append(user)
            return user

    @staticmethod
    def save_games():
        with open('trivia_game.save', 'bw') as file:
            pickle.dump(obj=Game.users, file=file)

    @staticmethod
    def load_games():
        try:
            with open('trivia_game.save', 'br') as file:
                Game.users = pickle.load(file)
        except (FileNotFoundError, IOError):
            pass

    @staticmethod
    def get_leader_board():
        leader_board = pd.concat(
            objs=[user.get_statistics(last_game=False, print_result=False, return_df=True) for user in Game.users],
            axis=0,
            ignore_index=True,
            sort=False
        )
        return leader_board

    @staticmethod
    def get_total_statistics(show_category=False, show_difficulty=False, print_table=True, return_df=False):
        sort_cols = []
        if show_category:
            sort_cols.append('category')
        if show_difficulty:
            sort_cols.append('difficulty')
        group_cols = sort_cols + ['player']

        stat_board = Game.get_leader_board().groupby(group_cols)['total', 'correct'].sum().reset_index()
        stat_board['ratio'] = stat_board['correct'] / stat_board['total']
        stat_board.sort_values(by=sort_cols + ['ratio'], ascending=False, inplace=True)

        if print_table:
            print(tabulate(stat_board, headers='keys', showindex=False, tablefmt='psql'))

        if return_df:
            return stat_board

    def __init__(self, load_games=True):
        if load_games:
            Game.load_games()
        self.connection = TriviaConnection()
        self.user = Game.select_user()

    def play(self):
        questions = self.connection.get_questions()
        print('\n\n')
        result_df = pd.DataFrame(columns=['category', 'difficulty', 'question', 'user_answer', 'correct_answer'])
        for i, q in questions.iterrows():
            print(f"Question {i + 1}:\t", end='')

            result_df = result_df.append(
                {
                    'category': q.category,
                    'difficulty': q.difficulty,
                    'question': q.question,
                    'user_answer': ask_question(q),
                    'correct_answer': q.correct_answer
                },
                ignore_index=True)

        self.user.add_result(result_df)
        self.user.get_statistics()
        Game.save_games()

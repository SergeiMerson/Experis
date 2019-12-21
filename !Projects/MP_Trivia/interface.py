import pandas as pd


class TriviaOptionSelector:

    @staticmethod
    def get_number_of_questions():
        q_number = None
        while not q_number:
            try:
                q_number = int(input('Enter number of questions: '))
                q_number = None if q_number < 1 else q_number

            except ValueError:
                print('Please enter number greater than 0')

        return q_number

    def __init__(self, header, options_dict):
        self.header = header
        self.options_dict = options_dict
        self.options_list = ['ANY'] + sorted(options_dict.keys())

    # Print to user available options, get his choice and try to interpret it:
    def get_user_input(self):
        print('\n', self.header, '\n')

        for i, opt in enumerate(self.options_list):
            print(f"{i}:\t{opt}")

        user_answer = input('Please choose your option: ')

        try:
            return self.options_dict[self.options_list[int(user_answer)]]

        except (ValueError, KeyError, IndexError):
            return False


def choose_user(users):
    if len(users) == 0:
        return None

    else:
        print('Choose existing player or create a new one:')
        print('1.\tCreate a new player')
        for i, u in enumerate(users, 1):
            print(f"{i+1}.\t{u.name}")

        choice = None
        while not choice:
            try:
                choice = int(input('>->->'))
                choice = None if choice not in range(len(users) + 2) else choice
            except ValueError:
                print('Please select an option number')

        if choice == 1:
            return None
        else:
            return users[choice - 2]


def ask_question(test):

    options = sorted([test.correct_answer] + test.incorrect_answers)

    print('\n', test.question, sep='')
    print("Possible answers:")
    for i, opt in enumerate(options, 1):
        print(f"{i}:\t{opt}")

    user_answer = None
    while not user_answer:
        try:
            user_answer = int(input('>->-> '))
            user_answer = None if user_answer - 1 not in range(len(options)) else user_answer
        except ValueError:
            print('Please enter the answer number')

    print('\n')
    return options[user_answer - 1]

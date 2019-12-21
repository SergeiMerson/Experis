import urllib.request
import json
import pandas as pd
from html import unescape
from interface import TriviaOptionSelector


class TriviaConnection:
    url_token_request = "https://opentdb.com/api_token.php?command=request"
    url_categories_request = "https://opentdb.com/api_category.php"
    difficulties = {'Easy': 'easy', 'Medium': 'medium', 'Hard': 'hard'}
    types = {'Multiple Choice': 'multiple', 'True/False': 'boolean'}

    @staticmethod
    def get_token():
        with urllib.request.urlopen(TriviaConnection.url_token_request) as url:
            answer = json.loads(url.read().decode())
            if answer['response_code'] == 0:
                return answer['token']
            else:
                return False

    @staticmethod
    def get_categories():
        with urllib.request.urlopen(TriviaConnection.url_categories_request) as url:
            answer = json.loads(url.read().decode())
            cat_dict = {}
            for rec in answer['trivia_categories']:
                cat_dict[rec['name']] = rec['id']
            return cat_dict

    @staticmethod
    def clear_html_symbols(target):
        if isinstance(target, str):
            return unescape(target)
        else:
            return [unescape(element) for element in target]

    def __init__(self):
        self.token = TriviaConnection.get_token()
        self.categories = TriviaConnection.get_categories()

    def compile_user_request(self):
        q_number = TriviaOptionSelector.get_number_of_questions()
        q_category = TriviaOptionSelector('Categories:', self.categories).get_user_input()
        q_difficulty = TriviaOptionSelector('Difficulty:', self.difficulties).get_user_input()
        q_type = TriviaOptionSelector('Type:', self.types).get_user_input()

        pattern = f"https://opentdb.com/api.php?amount={q_number}"
        if q_category:
            pattern += f"&category={q_category}"
        if q_difficulty:
            pattern += f"&difficulty={q_difficulty}"
        if q_type:
            pattern += f"&type={q_type}"
        if self.token:
            pattern += f"&token={self.token}"

        return pattern, q_difficulty

    def get_questions(self):
        request_url, q_difficulty = self.compile_user_request()
        with urllib.request.urlopen(request_url) as url:
            answer = json.loads(url.read().decode())
            if answer['response_code'] == 0:
                questions = pd.DataFrame(answer['results'])
                questions = questions.applymap(TriviaConnection.clear_html_symbols)
                questions['difficulty'] = q_difficulty if q_difficulty else 'mixed'
                return questions
            else:
                return None

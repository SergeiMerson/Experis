import pyodbc
import json
import requests


class DBSetup:
    db_name = 'TriviaDB'

    @staticmethod
    def connect_to_server():
        connection_parameters = """
                                   Driver=ODBC Driver 17 for SQL Server;
                                   Server=.\LENOVOSQLEXPRESS;
                                   Trusted_Connection=yes;
                                """
        connection = pyodbc.connect(connection_parameters, autocommit=True)
        return connection

    def __init__(self):
        self.connection = DBSetup.connect_to_server()
        self.connect_to_db()

    def connect_to_db(self):
        try:
            self.connection.execute(f"USE {DBSetup.db_name}")
        except pyodbc.OperationalError:
            print(f'There is no such database called {DBSetup.db_name}, creating a new one')
            self.create_db(DBSetup.db_name)

    def create_db(self, db_name):
        self.connection.autocommit = True
        try:
            self.connection.execute(f"CREATE DATABASE {db_name};")
        except pyodbc.ProgrammingError:
            print(f'There already exists database named {db_name}')
        # self.connection.autocommit = False

    def delete_db(self):
        db_name = DBSetup.db_name
        validation_string = input(f"""Are you sure that you want to delete {db_name}??
                                      To continue enter the name of this database: """)
        if validation_string == db_name:
            self.connection.autocommit = True
            try:
                self.connection.execute(f"""USE master;
                                            DROP DATABASE {db_name} ;  
                                         """)
                self.connection.execute(f"""USE {db_name}""")
                print(f"Can not delete {db_name}, please try to close existing connections to the database")
            except pyodbc.OperationalError:
                print(f"Successfully deleted {db_name}")
            # self.connection.autocommit = False

    def create_table(self, table_dict):
        name = table_dict['name']
        cols = table_dict['columns']
        query = f"CREATE TABLE {name} (" + ", ".join([" ".join(c) for c in cols]) + ");"
        self.connect_to_db()
        self.connection.execute(query)

    @staticmethod
    def add_to_table(table_dict, cursor):
        name = table_dict['name']
        values = table_dict['values']

        for v in values:
            n_params = len(v)
            query = f"INSERT INTO {name} VALUES (" + ", ".join(['?'] * n_params) + ")"
            cursor.execute(query, *v)


class DBRequests(DBSetup):
    def __init__(self):
        super(DBRequests, self).__init__()
        self.vocabulary = self.reindex_vocabularies()

    def initialize_basic_tables(self, list_of_tables, replace=True):
        self.connection.autocommit = True
        if replace:
            for table in list_of_tables[::-1]:
                self.connection.execute(f"DROP TABLE IF EXISTS {table['name']}")

        for table in list_of_tables:
            self.create_table(table)

            if table['values']:
                cursor = self.connection.cursor()
                self.add_to_table(table, cursor)
                cursor.commit()

        # Reindex vocabularies:
        self.vocabulary = self.reindex_vocabularies()

    def get_categories_from_api(self):
        response = requests.get("https://opentdb.com/api_category.php")
        categories = json.loads(response.text)['trivia_categories']

        self.connection.autocommit = False
        cursor = self.connection.cursor()
        try:
            for category in categories:
                cursor.execute(f"""INSERT INTO qCategories
                                        VALUES (?, ?) ;""", category['id'], category['name'])
            cursor.commit()
            self.vocabulary = self.reindex_vocabularies()

        except pyodbc.ProgrammingError:
            cursor.rollback()

    def get_vocabulary(self, table, key, val):
        cursor = self.connection.cursor()
        try:
            cursor.execute(f"SELECT {key}, {val} FROM {table};")
            vocabulary = {k: v for k, v in cursor}
            return vocabulary
        except pyodbc.ProgrammingError:
            return None

    def reindex_vocabularies(self):
        vocabulary = {
            'categories': self.get_vocabulary('qCategories', 'Category', 'CategoryID'),
            'difficulties': self.get_vocabulary('qDifficulties', 'DifficultyID', 'Difficulty'),
            'types': self.get_vocabulary('qTypes', 'TypeID', 'Type')}
        return vocabulary

    def add_question2db(self, q_dict, cursor=None):
        print('START!!!')
        q_category = self.vocabulary['categories'][q_dict['category']]
        q_difficulty = q_dict['difficulty']
        q_type = q_dict['type']
        q_text = q_dict['question']
        q_ans_correct = q_dict['correct_answer']
        q_ans_wrong = q_dict['incorrect_answers']

        if cursor is None:
            self.connection.autocommit = False
            cursor = self.connection.cursor()

        try:
            print('try to add question')
            print(f'Passing: {q_category}\n{q_difficulty}\n{q_type}\n{q_text}')
            self.add_to_table({'name': 'Questions',
                               'values': [(q_category, q_difficulty, q_type, q_text)]},
                              cursor)
            print('added question')
            q_id = cursor.execute("""
                                    SELECT QuestionID
                                      FROM Questions
                                     WHERE Question = ?
                                    """, q_text).fetchval()
            print('added answers')
            # Add correct answer:
            self.add_to_table({'name': 'qAnswers', 'values': [(q_id, q_ans_correct, 1)]}, cursor)

            # Add wrong answers:
            for ans in q_ans_wrong:
                self.add_to_table({'name': 'qAnswers', 'values': [(q_id, ans, 0)]}, cursor)

            # If everything went without errors - commit changes:
            cursor.commit()

        except (pyodbc.ProgrammingError, pyodbc.IntegrityError):
            cursor.rollback()

    def get_random_questions(self, n_questions=1):
        #  1) get question:
        cols = "QuestionID, CategoryID, DifficultyID, TypeID, Question"
        sql_request_questions = f"""SELECT  TOP {n_questions} {cols}
                                      FROM  Questions
                                  ORDER BY  NEWID(); """
        respond_questions = self.connection.cursor().execute(sql_request_questions).fetchall()

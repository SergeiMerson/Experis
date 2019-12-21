import random


def generate_id():
    letters = [chr(l) for l in list(range(65, 91)) + list(range(97, 123))]
    return ''.join(random.choices(letters, k=5)) + str(random.choice(range(int(1e5), int(1e6))))


class Author:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.id = generate_id()


class Book:
    def __init__(self, title, author_id):
        self.title = title
        self.author_id = author_id
        self.id = author_id + '-' + generate_id()
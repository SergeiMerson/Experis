import basics


class Register:
    def __init__(self):
        self.register = {}

    def get_items(self):
        return (val for _, val in self.register.items())

    def get_by_key(self, key):
        try:
            return self.register[key]
        except KeyError:
            print('There is no such ID')

    def reset_register(self):
        user_input = input('Do you really want to reset the Register and delete all records? [Y]/[N]: ')
        if user_input.lower() == 'y':
            self.register.clear()
            print('The Register was reset successfully')


class AuthorRegister(Register):

    def add(self, first_name, last_name):
        author = basics.Author(first_name, last_name)
        self.register[author.id] = author
        print(f'Successfully added {first_name} {last_name} to the Register with ID: {author.id}')
        return author

    def remove(self, author_id):
        try:
            author = self.register[author_id]
            del self.register[author_id]
            print(f'Successfully removed {author.first_name} {author.last_name} with ID: {author_id} form Register')
        except KeyError:
            print(f'There is no Author with ID: {author_id}')

    def search_by_name(self, first_name='?', last_name='?'):
        operator = any if any((first_name == '?', last_name == '?')) else all
        return [a for a in self.get_items()
                if operator((
                    first_name.lower() in a.first_name.lower(),
                    last_name.lower() in a.last_name.lower()
                ))]


class BookRegister(Register):

    def add(self, title, author_id):
        book = basics.Book(title, author_id)
        self.register[book.id] = book
        return book

    def remove(self, book_id):
        try:
            book_title = self.register[book_id].title
            del self.register[book_id]
            print(f'Successfully deleted Book {book_title} with id: {book_id}')
        except KeyError:
            print(f'There is no Book with ID: {book_id}')

    def search_by_title(self, title):
        return [b for b in self.get_items() if title.lower() in b.title.lower()]

    def search_by_author_id(self, author_id):
        return [b for b in self.get_items() if author_id == b.author_id]

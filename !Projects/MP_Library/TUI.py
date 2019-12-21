import library


# ======================== Dialog windows and structures ========================= #
def _print_header(title='', width=120):
    print('\n' * 2, f"{(' ' + str(title) + ' ').center(width, '=')}", '\n', sep='')


def _print_closure(width=120):
    print('\n', '=' * width, sep='')


def print_menu(title, options, width=120, first_element=0):
    _print_header(title=title, width=width)
    for i, opt in enumerate(options, first_element):
        print(f"{str(i):>4s} : {opt}")
    _print_closure(width)


def print_list_of_items(title, lst, width=120):
    _print_header(title=title, width=width)
    max_len_0 = max(map(len, [row[0] for row in lst]))
    max_len_1 = max(map(len, [row[1] for row in lst]))
    for row in lst:
        print(' '*4 + f"{str(row[0]):<{max_len_0}}",
              f"{str(row[1]):<{max_len_1}}",
              *row[2:], sep=' '*4)
    _print_closure(width=width)


# ================================ Help functions ================================ #
def get_user_choice(current_menu, menu_calls):
    user_choice = False
    while not user_choice:
        try:
            user_answer = int(input('Please enter your choice: '))
            user_choice = menu_calls[current_menu][user_answer]
        except (ValueError, KeyError):
            print('Cannot understand your input, please try again:')
    return user_choice


def get_author_name():
    first_name = input('First name: ')
    last_name = input('Last name: ')
    first_name = first_name if first_name else '?'
    last_name = last_name if last_name else '?'
    return first_name, last_name


# ================================================================================ #
# ================== TUI - Library Class with only user inputs =================== #


class TextUserInterface(library.Library):
    # ================================= Authors ================================== #

    def tui_add_author(self):
        first_name, last_name = get_author_name()
        self.add_author(first_name, last_name)

    def tui_remove_author(self):
        first_name, last_name = get_author_name()
        self.remove_author(first_name, last_name)

    # ================================== Books =================================== #

    def tui_add_book(self):
        title = input('Title: ')
        if title.lower() != 'exit':
            first_name = input('First name: ')
            if first_name.lower() != 'exit':
                last_name = input('Last name: ')
                if last_name.lower() != 'exit':
                    self.add_book(title, first_name, last_name)

    def tui_remove_book(self):
        book_id = input('ID: ')
        self.books.remove(book_id)

    # ================================== Search ================================== #

    def tui_find_author_by_id(self):
        author_id = input('ID: ')
        author = self.authors.get_by_key(author_id)
        print_list_of_items(f"Search result for ID: {author_id}",
                            [[author.id, author.first_name, author.last_name]])

    def tui_find_author_by_name(self):
        first_name, last_name = get_author_name()
        _ = self.search_author(first_name, last_name)

    def tui_find_author_by_book(self):
        self.tui_find_book_by_title()

    def tui_find_book_by_id(self):
        book_id = input('ID: ')
        book = self.books.get_by_key(book_id)
        print_list_of_items(f"Search result for ID: {book_id}",
                            [[book.id, book.first_name, book.last_name]])

    def tui_find_book_by_title(self):
        title = input('Title: ')
        list_of_results = []
        book_list = self.books.search_by_title(title)
        for book in book_list:
            author = self.authors.get_by_key(book.author_id)
            list_of_results.append([book.id, book.title, author.first_name + ' ' + author.last_name])
        if book_list:
            print_list_of_items(f"Search results for: {title}", list_of_results)
        else:
            print(f"Nothing was found for '{title}'")

    def tui_find_books_by_author(self):
        first_name, last_name = get_author_name()
        return self.search_books_by_author(first_name, last_name)

    # =================================== I/O ==================================== #

    def tui_save_library(self):
        self.save_library()

    def tui_load_library(self):
        self.load_library()

    def tui_export_library(self):
        self.export_library()

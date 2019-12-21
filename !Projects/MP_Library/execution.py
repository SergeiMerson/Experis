import menu_items as mi
import TUI as tui


def run_program():

    # Initializations:
    library = tui.TextUserInterface()
    print('Welcome to the Library Management Application!')
    # library.load_library()

    actions = {
        # Main Menu:
        100: {'func': tui.print_menu, 'args': mi.main_menu},
        # Book Register:
        200: {'func': tui.print_menu, 'args': mi.book_register},
        201: {'func': library.tui_add_book, 'args': {}},
        202: {'func': library.tui_remove_book, 'args': {}},
        203: {'func': library.tui_find_book_by_id, 'args': {}},
        204: {'func': library.tui_find_book_by_title, 'args': {}},
        205: {'func': library.tui_find_books_by_author, 'args': {}},
        # Author Register:
        300: {'func': tui.print_menu, 'args': mi.author_register},
        301: {'func': library.tui_add_author, 'args': {}},
        302: {'func': library.tui_remove_author, 'args': {}},
        303: {'func': library.tui_find_author_by_id, 'args': {}},
        304: {'func': library.tui_find_author_by_name, 'args': {}},
        305: {'func': library.tui_find_author_by_book, 'args': {}},
        # Search
        400: {'func': tui.print_menu, 'args': mi.search_menu},
        401: {'func': library.tui_find_book_by_id, 'args': {}},
        402: {'func': library.tui_find_book_by_title, 'args': {}},
        403: {'func': library.tui_find_books_by_author, 'args': {}},
        404: {'func': library.tui_find_author_by_id, 'args': {}},
        405: {'func': library.tui_find_author_by_name, 'args': {}},
        # I/O:
        500: {'func': tui.print_menu, 'args': mi.io_menu},
        501: {'func': library.tui_export_library, 'args': {}},
        502: {'func': library.tui_save_library, 'args': {}},
        503: {'func': library.tui_load_library, 'args': {}}}

    menu_calls = {
        100: {1: 200, 2: 300, 3: 400, 4: 500, 5: 999},
        200: {0: 100, 1: 201, 2: 202, 3: 203, 4: 204, 5: 205, 6: 999},
        300: {0: 100, 1: 301, 2: 302, 3: 303, 4: 304, 5: 305, 6: 999},
        400: {0: 100, 1: 401, 2: 402, 3: 403, 4: 404, 5: 405, 6: 999},
        500: {0: 100, 1: 501, 2: 502, 3: 503, 6: 999}}

    # Show main menu when program starts:
    current_menu = 100
    user_choice = 100
    tui.print_menu(**mi.main_menu)

    while current_menu != 999:
        # Show menu window if action was selected (not another menu):
        if user_choice not in (100, 200, 300, 400, 500, 999):
            menu = actions[current_menu]
            menu['func'](**menu['args'])

        # Get user choice:
        user_choice = tui.get_user_choice(current_menu, menu_calls)

        # Execute action according to this choice:
        action = actions[user_choice]
        func = action['func']
        args = action['args']
        func(**args)

        # If user select to go to another menu - switch it's index:
        if user_choice in (100, 200, 300, 400, 500, 999):
            current_menu = user_choice

    print('Exiting the program, have a nice day!')


if __name__ == '__main__':
    run_program()

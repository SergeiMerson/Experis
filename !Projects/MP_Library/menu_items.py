main_menu = {'title': 'Main Menu',
             'options': ['Book Register', 'Author Register', 'Search',
                         'Export & Backup', 'Exit'],
             'first_element': 1}

book_register = {'title': 'Book Register',
                 'options': ['Main Menu', 'Add Book', 'Remove Book',
                             'Find Book by ID', 'Find Book by Title',
                             'Find Book by Author', 'Exit'],
                 'first_element': 0}

author_register = {'title': 'Author Register',
                   'options': ['Main Menu', 'Add Author', 'Remove Author',
                               'Find Author by ID', 'Find Author by name',
                               'Find Author by Book', 'Exit'],
                   'first_element': 0}

search_menu = {'title': 'Search',
               'options': ['Main Menu', 'Find Book by ID', 'Find Book by Title',
                           'Find Book by Author', 'Find Author by ID',
                           'Find Author by name', 'Exit'],
               'first_element': 0}

io_menu = {'title': 'Export & Backup',
           'options': ['Main Menu', 'Export to JSON', 'Save to backup',
                       'Restore from backup', 'Exit'],
           'first_element': 0}

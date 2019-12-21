import library as lc


library = lc.Library()
try:
    library.load_library()
except IOError:
    library.add_book('White Hang', 'Jack','London')
    library.add_book('Long Night', 'Jack','Martin')
    library.add_book('Long Journey', 'Brain','Storm')
    library.add_book('Far Far Away', 'Brain','Storm')
    library.add_book('Python for Dummies', 'Yuval','Shaul')
    library.add_book('Python for those who didn\'t understand the first book', 'Yuval','Shaul' )
    library.save_library()


from Exercises.Project_Gutenberg import cleantext


def line_generator(book_path):
    with open(book_path, 'r', encoding='UTF-8') as book_file:
        for line in book_file:
            yield line


def count_words(book_path: str) -> dict:
    lines = line_generator(book_path)
    vocabulary = {}

    for line in lines:
        list_of_words = cleantext.clean_line(line)
        for word in list_of_words:
            vocabulary[word] = vocabulary.get(word, 0) + 1

    return vocabulary


def print_vocabulary(vocabulary):
    # Print result in descending order:
    for key, val in sorted(vocabulary.items(),
                           key=lambda key_val: (key_val[1], (key_val[0])),
                           reverse=True):
        print(f'{key:<15s} {val:<4d}', sep='\t')


def count_macbeth():
    book_path = r"d:\Projects\ExperisAcademy\Exercises\Project_Gutenberg\Macbeth.txt"
    vocabulary = count_words(book_path)
    print_vocabulary(vocabulary)


if __name__ == '__main__':
    count_macbeth()

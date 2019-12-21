def get_stopwords():
    stopwords_path = r"d:\Projects\ExperisAcademy\Exercises\Project_Gutenberg\stopwords.txt"
    with open(stopwords_path, 'r', encoding='UTF-8') as stopwords_file:
        return set([symbol.strip() for symbol in stopwords_file.readlines()])


def get_val_chars():
    ascii_val_chars = list(range(65,91)) + list(range(97,123))
    val_chars = {chr(i) for i in ascii_val_chars}
    return val_chars


def clear_non_chars(string):
    val_chars = get_val_chars()
    return ''.join((char if char in val_chars else ' ' for char in string))


def clean_line(line):
    stopwords = get_stopwords()
    string = clear_non_chars(line)
    list_of_words = [word.lower() for word in string.split() if word.lower() not in stopwords]
    return list_of_words

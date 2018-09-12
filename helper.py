def is_isbn_or_key(key_word):
    """
    判断是isbn还是关键字
    isbn13 由13个0-9的数字组成
    isbn10 由10个0-9的数字组成，可能含有'-'
    :param key_word:
    :return:
    """
    key_word = key_word.strip()
    isbn_or_key = 'key'
    if len(key_word) == 13 and key_word.isdigit():
        isbn_or_key = 'isbn'
    short_key_word = key_word.replace('-', '')
    if len(short_key_word) == 10 and short_key_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key

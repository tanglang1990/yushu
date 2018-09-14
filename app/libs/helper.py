def is_isbn_or_key(keyword):
    """
    判断是isbn还是关键字
    isbn13 由13个0-9的数字组成
    isbn10 由10个0-9的数字组成，可能含有'-'
    :param key_word:
    :return:
    """
    keyword = keyword.strip()
    isbn_or_key = 'key'
    if len(keyword) == 13 and keyword.isdigit():
        isbn_or_key = 'isbn'
    short_keyword = keyword.replace('-', '')
    if len(short_keyword) == 10 and short_keyword.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key

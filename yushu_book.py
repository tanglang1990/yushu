from httper import HTTP


class YuShuBook:
    isbn_url = 'https://api.douban.com/v2/book/isbn/{}'
    keyword_url = 'https://api.douban.com/v2/book/search?q={}&start={}&count={}'

    @classmethod
    def search_by_isbn(cls, q):
        url = cls.isbn_url.format(q)
        result = HTTP.get(url)
        return result

    @classmethod
    def search_by_keyword(cls, q, start=0, count=15):
        url = cls.keyword_url.format(q, start, count)
        result = HTTP.get(url)
        return result

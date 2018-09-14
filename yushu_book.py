from httper import HTTP


class YuShuBook:
    per_page = 15
    isbn_url = 'https://api.douban.com/v2/book/isbn/{}'
    keyword_url = 'https://api.douban.com/v2/book/search?q={}&start={}&count={}'

    @classmethod
    def search_by_isbn(cls, q):
        url = cls.isbn_url.format(q)
        result = HTTP.get(url)
        return result

    @classmethod
    def search_by_keyword(cls, q, page=1):
        url = cls.keyword_url.format(q, (page-1)*cls.per_page, cls.per_page)
        result = HTTP.get(url)
        return result

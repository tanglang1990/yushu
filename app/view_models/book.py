class BookViewModel:
    '''
    数据要求
    {
        'books': [{
            'title': '',
            'publisher': '',
            'pages': '',
            'author': '',
            'price': 0,
            'summary': '',
            'image': ''
        }],
        'total': 0,
        'keyword': ''
    }
    '''

    @classmethod
    def package_single(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = 1
            returned['books'].append(cls.handle_book_data(data))
        return returned

    @classmethod
    def package_collection(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = data['total']
            returned['books'] = [cls.handle_book_data(book_item) for book_item in data['books']]
        return returned

    @classmethod
    def handle_book_data(cls, data):
        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'pages': data['pages'],
            'author': '、'.join(data['author']),
            'price': data['price'],
            'summary': data['summary'],
            'image': data['image']
        }
        return book
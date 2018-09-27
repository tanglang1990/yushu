class MyResource:
    # def __enter__(self):
    #     print('connect to resource')
    #     return self
    #
    # def __exit__(self, exc_type, exc_value, tb):
    #     print('close resource connection')

    def query(self):
        print('query data')


# with MyResource() as r:
#     r.query()


from contextlib import contextmanager


@contextmanager
def make_myresource():
    print('connect to resource')
    # pass
    # return MyResource()
    yield MyResource()
    print('close resource connection')


with make_myresource() as r:
    r.query()


@contextmanager
def book_mark():
    print('《', end='')
    yield
    print('》', end='')


with book_mark():
    print("神雕侠侣", end='')

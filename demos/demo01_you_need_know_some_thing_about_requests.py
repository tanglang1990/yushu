from flask import request


def prase_request():
    '''
    request 需要由视图函数驱动
    如果是单纯的调用得到的将是一个本地代理LocalProxy
    后续我们会深入讲这样一种机制
    '''
    a = request
    pass


prase_request()

class A:
    def go(self):
        return object()


class B:
    def run(self):
        return object()


def func():
    return object()


def main(param):
    # 我想在main中调用传入的参数得到一个对象object
    if isinstance(param, A):
        return param.go()
    if isinstance(param, B):
        return param.run()
    if callable(param):
        return param()


if __name__ == '__main__':
    a = A()
    b = B()

    print(main(a))
    print(main(b))
    print(main(func))

#
# class A:
#     def __call__(self):
#         return object()
#
#
# class B:
#     def __call__(self):
#         return object()
#
#
# def func():
#     return object()
#
#
# def main(param):
#     # 我想在main中调用传入的参数得到一个对象object
#     return param()
#
#
# if __name__ == '__main__':
#     a = A()
#     b = B()
#
#     print(main(a))
#     print(main(b))
#     print(main(func))

# callable可调用对象的意义
# 1、简化对象下方法的调用，如可把 a.func() 简化成 a()
# 2、统一调用接口，如上面例子中展示的，统一调用param()即可，主要用于抽象编程

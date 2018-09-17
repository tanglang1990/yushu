# 原理 字典 保存数据
# 操作数据
# werkzeug local Local 字典
# LocalStack Local 字典
# Local使用字典的方式实现的线程隔离
# 线程隔离的栈结构
# 封装 如果一次封装解决不了问题，那么就再来一次
# 编程也是一种艺术 含蓄

# {thread_id1:value1,thread_id2:value2...}
# L 线程隔离的对象
# t1 L.a t2 L.a
# Local

# 线程隔离的对象 被线程隔离的对象
# 操作线程隔离的对象（Local、LocalStack）来实现其他对象的线程隔离

import threading

import time
from werkzeug.local import Local


class A:
    b = 1


# my_obj = A()
my_obj = Local()
my_obj.b = 1


def worker():
    # 新线程
    my_obj.b = 2
    print('in new thread b is:' + str(my_obj.b))


new_t = threading.Thread(target=worker, name='qiyue_thread')
new_t.start()
time.sleep(1)
# 主线程
print('in main thread b is:' + str(my_obj.b))

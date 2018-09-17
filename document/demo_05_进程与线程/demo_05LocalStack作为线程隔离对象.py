import threading

import time

from werkzeug.local import LocalStack

my_stack = LocalStack()
my_stack.push(1)
print('in main thread after push , value is:' + str(my_stack.top))


def worker():
    # 新线程
    print('in new thread before push, value is:' + str(my_stack.top))
    my_stack.push(2)
    print('in new thread after push,value is:' + str(my_stack.top))


new_t = threading.Thread(target=worker, name='qiyue_thread')
new_t.start()
time.sleep(1)
# 主线程
print('finally, in main thread value is:' + str(my_stack.top))

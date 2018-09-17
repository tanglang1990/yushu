# 全局解释器锁,多任务执行的情况,很多使用的多进程
# pythonGIL全局解释器锁,多线程执行效率比较糟糕


# # 多线程--->相对于1个进程而言(共享数据,多个子线程所共享的数据)
# # 多个线程操作共享数据出现数据混乱
# from threading import Thread
#
# money = 0
#
#
# def change_money(num):
#     global money
#     for i in range(num):  # 先存100,马上取100,先存后取,重复执行多少次,理想的结果依然为0
#         money = money + num
#         money = money - num
#
#
# # 两个子线程操作共享数据money---->理想的结果还是0
# thr1 = Thread(target=change_money, args=(200,))
# thr2 = Thread(target=change_money, args=(300,))
# thr1.start()
# thr2.start()
# thr1.join()
# thr2.join()
# print('最后的money数目为', money)
## 符合我们的正常逻辑?问题会出现在哪?


# # 新的问题?假如循环次数改得很大?
# from threading import Thread
#
# money = 0
#
#
# def change_money(num):
#     global money
#     for i in range(num):  # 先存100,马上取100,先存后取,重复执行多少次,理想的结果依然为0
#         money = money + num
#         money = money - num
#
#
# # 两个子线程操作共享数据money---->理想的结果还是0
# thr1 = Thread(target=change_money, args=(9999999,))
# thr2 = Thread(target=change_money, args=(8888888,))
# thr1.start()
# thr2.start()
# thr1.join()
# thr2.join()
# print('最后的money数目为', money)
# 两个子线程操作共享数据money---->理想的结果还是0
# 最后的money数目为 -127777765   共享数据出现了混乱

# 思考为什么会出现这种问题？
# 原因是因为高级语言的一条语句在CPU执行时是若干条语句，即使一个简单的计算：
# money = money + num
# 也分两步：
# 计算money + num，存入临时变量中；
# 将临时变量的值赋给money。
# 也就是可以看成：
# x = money + num
# money = x
# 如果操作系统以下面的顺序执行thr1、thr2：
# 初始值 money = 0
#
# t1: x1 = money + 5  # x1 = 0 + 5 = 5
#
# t2: x2 = money + 8  # x2 = 0 + 8 = 8
# t2: money = x2      # money = 8
#
# t1: money = x1      # money = 5
# t1: x1 = money - 5  # x1 = 5 - 5 = 0
# t1: money = x1      # money = 0
#
# t2: x2 = money - 8  # x2 = 0 - 8 = -8
# t2: money = x2   # money = -8
#
# 结果 money = -8


# # 解决这个问题,引入锁机制?
# from threading import Thread, Lock, current_thread
#
# money = 0
# # 操作共享数据之前先构建锁对象
# lock = Lock()
#
#
# def run_money(num):
#     global money
#     try:
#         # 先加锁
#         lock.acquire()
#         for i in range(num):  # 先存100,马上取100,先存后取,重复执行多少次,理想的结果依然为0
#             money = money + num
#             money = money - num
#     finally:
#         lock.release()  # 释放锁对象
#
#
# thr1 = Thread(target=run_money, args=(9999999,))
# thr2 = Thread(target=run_money, args=(8888888,))
# thr1.start()
# thr2.start()
# thr1.join()
# thr2.join()
# print('最后的money数目为', money)

import threading


def hello():
    print("I'm the new thread")
    t = threading.current_thread()
    print(t.getName())


new_t = threading.Thread(target=hello, name='ten thread')
new_t.start()

t = threading.current_thread()
print(t.getName())

# 更加充分的利用CPU的优势
# 异步编程
# 单核CPU
# 8核 A核 B核 并行的执行程序
# Python不能充分利用多核CPU优势
# 6s + 6s = 6s
# Python的多线程是鸡肋  这句话对吗？
# GIL 全局解释器锁 global interpreter lock


# 内存资源 在一个进程中由多个线程共享
# Cpython解释器本身线程是不安全的

# a=3

# A a+=1
# print(a)

# B a+=1
# print(b)

# 分别用AB线程执行一次a+=1,最后的结果其实并不一定会为5
# 思考为什么会出现这种问题？
# 原因是因为高级语言的一条语句在CPU执行时是若干条语句（在python中就是所谓的字节码:bytecode），
# 即使一个简单的计算 a+=1也分两步：
# 计算a+1，存入临时变量中；
# 将临时变量的值赋给a。
# 也就是可以看成：
# x = a + 1
# a = x
# 详细效果见demo_02

# 怎么去解决这个问题？
# 锁
# 细粒度的锁 程序员 主动加的锁
# 粗粒度的锁 解释器 GIL 多核CPU 1个线程执行 一定程度上保证了线程安全

# 多线程是不是鸡肋？
# GIL node.js 单线程 单进程
# 10个线程 非常依赖CPU的计算 CPU密集型程序（比如：视频编解码、圆周率的运算）
# IO密集型 查询数据库、请求网络资源、读写文件

# IO密集型 很多时候都是在等待
# 请求 线程
# 10个请求flask开启多少个线程处理？
# webserver
# nginx apache tomcat IIS

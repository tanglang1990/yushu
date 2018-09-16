import threading


def hello():
    print("I'm the new thread")
    t = threading.current_thread()
    print(t.getName())


new_t = threading.Thread(target=hello, name='ten thread')
new_t.start()

# 更加充分的利用CPU的优势
# 异步编程

t = threading.current_thread()
print(t.getName())

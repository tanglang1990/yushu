from werkzeug.local import LocalStack

# 栈的特性
s = LocalStack()
s.push(1)
print(s.top)
print(s.top)
print(s.pop())
print(s.top)

s.push(1)
s.push(2)
# 栈 先进先出
print(s.top)
print(s.top)
print(s.pop())
print(s.top)

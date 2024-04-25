from collections import deque
x = deque()
x.append('a')
x.append('b')
x.append('c')
x.append('d')

print("initial queue")
print(x)

print("Elements dequeued from the queue")
print(x.popleft())
print(x.popleft())
print(x.popleft())

print("Queue after removing elements")
print(x)
print(type(x))

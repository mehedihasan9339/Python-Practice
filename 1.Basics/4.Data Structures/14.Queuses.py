from collections import deque

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)

queue.appendleft(0)
print(queue) # deque([0, 1, 2, 3])

queue.pop()
print(queue) # deque([0, 1, 2])

queue.popleft()
print(queue) # deque([1, 2])

queue.clear()

if not queue:
    print("empty") # empty


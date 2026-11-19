from collections import deque

# Stack - LIFO (Last In First Out)

stack = []

stack.append(5)
print(stack)

x= stack.pop()
print(x)


# Queues - FIFO (First In First Out)

q = deque()

# Enqueue - Add element to the right - O(1)

q.append(5)
q.append(6)
q.append(7)
print(q)

# Dequeue (popleft) - Remove element from the left - O(1)
q.popleft()
print(q)

# Peek from left side (the front element)

print(q[0])

# Peek from the right (last element)
print(q[-1])


from collections import deque

q= deque()

q.append("a") # Queue: [a]
q.append("b") # Queue: [a,b]
q.append("c") # Queue: [a,b,c]
q.popleft() # Removes A, queue: [b,c]
q.append("d") # queue: [b,c,d]
q.popleft() # removes B, queue: [c,d]

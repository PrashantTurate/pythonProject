# deque - double-ended queue
# FIFO - A list-like sequence optimized for data accesses near its endpoints.

from collections import deque

d = deque([1,2,3,4,5,9,8,7])
print("deque list:",d)
d.append(3)
print("deque list with append:",d)
d.appendleft(0)
print("deque list with left append:",d)
d.extend([11,12,13,14,15])
print("deque list with extend list:",d)
#print(d.pop())
#print(d.popleft())
d.reverse()
print("deque reverse list:",d)


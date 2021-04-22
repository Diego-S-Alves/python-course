"""
Uma lista de alta performance
"""
from collections import deque

deq = deque('geek')

print(deq)

deq.append('y')

print(deq)

deq.appendleft('k')

print(deq)

#pop e popleft

import collections
q= collections.deque()

q.appendleft(10)
q.appendleft(20)
q.appendleft(30)

print('Elemets in Queue', q)

print('deleted element',q.pop())

print("queue elements after delete",q)
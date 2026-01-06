from collections import deque
n=int(input())
lst=[i for i in range(1,n+1)]
q=deque(lst)
while len(q)!=1:
    q.popleft()
    t=q.popleft()
    q.append(t)
print(q[0])
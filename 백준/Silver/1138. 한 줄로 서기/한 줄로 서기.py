from collections import deque
n=int(input())
lst=list(map(int,input().split()))
q=deque()
for i in range(-1,-(n+1),-1):
    h=i+n+1
    v=lst[i]
    l=len(q)
    if v > l//2: #왼쪽에서~
        t=[]
        for _ in range(v):
            t.append(q.popleft())
        q.appendleft(h)
        for _ in range(v):
            q.appendleft(t.pop())
    else:
        t=[]
        for _ in range(l-v):
           t.append(q.pop())
        q.append(h)
        for _ in range(l-v):
            q.append(t.pop())
print(*list(q))

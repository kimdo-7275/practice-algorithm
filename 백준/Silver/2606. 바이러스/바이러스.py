from collections import deque
n=int(input())
m=int(input())
dp=[[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    x,y=map(int,input().split())
    dp[x][y]=1
    dp[y][x]=1
queue=deque()
s=set()
s.add(1)
for i in range(n+1):
    if dp[1][i]==1:
        queue.append(i)
while queue:
    v=queue.popleft()
    s.add(v)
    for i in range(n+1):
        if dp[v][i]==1 and i not in s:
            s.add(i)
            queue.append(i)
print(len(s)-1)
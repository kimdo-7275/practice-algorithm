from collections import deque
n=int(input())
p1,p2=map(int,input().split())
m=int(input())
arr=[[0]*(n+1) for _ in range(n+1)]
visit=[0]*(n+1)
for _ in range(m):
    a,b=map(int,input().split())
    arr[a][b]=1
    arr[b][a]=1
q=deque()
q.append(p1)
visit[p1]=1
while q:
    p=q.popleft()
    for i in range(1,n+1):
        if arr[p][i] and not visit[i]:
            visit[i]=visit[p]+1
            q.append(i)

if visit[p2]:
    print(visit[p2]-1)
else:
    print(-1)

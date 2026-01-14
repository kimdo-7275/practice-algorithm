from collections import deque
n,m=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
visit=[[0]*m for _ in range(n)]
def bfs():
    for i in range(n):
        for j in range(m):
            if arr[i][j]!=2:
                continue
            q=deque()
            q.append((i,j))
            visit[i][j]=1
            arr[i][j]=0
            while q:
                pi,pj=q.popleft()
                for di,dj in ((-1,0),(1,0),(0,1),(0,-1)):
                    ni,nj=pi+di,pj+dj
                    if 0<=ni<n and 0<=nj<m and not visit[ni][nj] and arr[ni][nj]:
                        visit[ni][nj]=1
                        arr[ni][nj]=arr[pi][pj]+1
                        q.append((ni,nj))
            return
bfs()
for i in range(n):
    for j in range(m):
        if not visit[i][j] and arr[i][j]:
            arr[i][j]=-1
for a in arr:
    print(*a)
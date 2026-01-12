from collections import deque
n=int(input())
arr = [list(input()) for _ in range(n)]
visited=[[0]*n for _ in range(n)]
answer=[]
for i in range(n):
    for j in range(n):
        if arr[i][j]=='1' and visited[i][j]==0:
            q=deque()
            q.append((i,j))
            visited[i][j]=1
            count=0
            while q:
                pi,pj=q.popleft()
                count+=1
                for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
                    ni,nj=pi+di, pj+dj
                    if 0<=ni<n and 0<=nj<n and arr[ni][nj]=='1' and visited[ni][nj]==0:
                        q.append((ni,nj))
                        visited[ni][nj]=1
            answer.append(count)
print(len(answer))
answer.sort()
for i in answer:
    print(i)

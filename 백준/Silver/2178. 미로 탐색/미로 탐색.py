n,m=map(int,input().split())
arr = [list(map(int,input())) for _ in range(n)]

visited=[[0]*m for _ in range(n)]

q=[(0,0)]
visited[0][0]=1
while q:
    i,j = q.pop(0)
    for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
        ni,nj=i+di,j+dj
        if 0<=ni<n and 0<=nj<m and arr[ni][nj] and visited[ni][nj]==0:
            arr[ni][nj]=arr[i][j]+1
            q.append((ni,nj))
            visited[ni][nj]=1
print(arr[-1][-1])

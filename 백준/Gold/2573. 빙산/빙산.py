from collections import deque
n,m=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]

def time_pass(arr):
    new_arr=[[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j]:
                melt=0
                for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                    ni,nj=di+i,dj+j
                    if 0<=ni<n and 0<=nj<m and arr[ni][nj]==0:
                        melt+=1
                new_arr[i][j]=max(0,arr[i][j]-melt)
    return [x[:]for x in new_arr]

def count_island(arr):
    island_num=0
    visit=[[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j] and not visit[i][j]:
                island_num+=1
                q=deque()
                q.append((i,j))
                visit[i][j]=1
                while q:
                    pi,pj=q.popleft()
                    for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                        ni,nj=pi+di,pj+dj
                        if 0<=ni<n and 0<=nj<m and not visit[ni][nj] and arr[ni][nj]:
                            visit[ni][nj]=1
                            q.append((ni,nj))
    return island_num
year=0
while True:
    year+=1
    arr=time_pass(arr)
    island_num=count_island(arr)
    if island_num>1:
        print(year)
        break
    elif island_num==1:
        continue
    elif island_num==0:
        print(0)
        break
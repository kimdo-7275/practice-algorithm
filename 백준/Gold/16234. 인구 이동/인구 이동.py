from collections import deque
n,l,r=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
day=0
while True:
    day+=1
    visit=[[0]*n for _ in range(n)]
    visit_num=1
    for i in range(n):
        for j in range(n):
            if visit[i][j]:
                continue
            visit[i][j]=visit_num
            q=deque()
            q.append((i,j))
            while q:
                pi,pj=q.popleft()
                for di,dj in ((-1,0),(1,0),(0,1),(0,-1)):
                    ni,nj=di+pi,dj+pj
                    if 0<=ni<n and 0<=nj<n and not visit[ni][nj] and l<=abs(arr[pi][pj]-arr[ni][nj])<=r:
                        visit[ni][nj]=visit_num
                        q.append((ni,nj))
            visit_num+=1
    if visit_num==n**2+1:
        print(day-1)
        break
    visit_2=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visit_2[i][j]:
                continue
            pop=[arr[i][j]]
            loc=[(i,j)]
            vn=visit[i][j]
            visit_2[i][j]=1
            q=deque()
            q.append((i,j))
            while q:
                pi, pj = q.popleft()
                for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                    ni, nj = di + pi, dj + pj
                    if 0 <= ni < n and 0 <= nj < n and not visit_2[ni][nj] and visit[ni][nj]==vn:
                        visit_2[ni][nj]=1
                        q.append((ni,nj))
                        pop.append(arr[ni][nj])
                        loc.append((ni,nj))
            n_pop=sum(pop)//len(pop)
            for ni,nj in loc:
                arr[ni][nj]=n_pop
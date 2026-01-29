from collections import deque
import heapq
def bfs(t,n):
    arr=[list(map(int,input().split())) for _ in range(n)]
    visit=[[float('inf')]*n for _ in range(n)]
    visit[0][0]=arr[0][0]
    heap=[(arr[0][0],0,0)]
    while heap:
        cnt_weight,cnt_x,cnt_y=heapq.heappop(heap)

        if cnt_weight > visit[cnt_x] [cnt_y]:
            continue

        for di,dj in ((-1,0),(1,0),(0,1),(0,-1)):
            ni,nj=cnt_x+di, cnt_y+dj
            if 0<=ni<n and 0<=nj<n:
                dist=cnt_weight+arr[ni][nj]
                if dist<visit[ni][nj]:
                    visit[ni][nj]=dist
                    heapq.heappush(heap,(dist,ni,nj))
    print(f"Problem {t}: {visit[-1][-1]}")
t=1
while True:
    n=int(input())
    if n==0:
        break
    bfs(t,n)
    t+=1
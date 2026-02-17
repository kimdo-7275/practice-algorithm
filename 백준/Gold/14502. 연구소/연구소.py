from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

answer=0




def bfs(new_wall):
    virus=[[0]*m for _ in range(n)]
    visited_2=[[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j]==2 and (i,j) not in new_wall and not visited_2[i][j]:
                virus[i][j]=1
                q=deque()
                q.append((i, j))
                visited_2[i][j] = 1
                while q:
                    pi, pj = q.popleft()
                    for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
                        ni,nj=pi+di,pj+dj
                        if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 0 and virus[ni][nj]==0 and (ni, nj) not in new_wall and not visited_2[ni][nj]:
                            q.append((ni,nj))
                            virus[ni][nj]=1
                            visited_2[ni][nj]=1
    safe = 0
    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j]==0 and (i,j) not in new_wall and not visited[i][j] and virus[i][j]==0:
                q = deque()
                q.append((i,j))
                visited[i][j] = 1
                safe+=1
                while q:
                    pi, pj = q.popleft()
                    for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
                        ni,nj=pi+di,pj+dj
                        if 0<=ni<n and 0<=nj<m and arr[ni][nj]==0 and (ni,nj) not in new_wall and not visited[ni][nj] and virus[i][j]==0:
                            safe+=1
                            q.append((ni,nj))
                            visited[ni][nj]=1
    return safe
zeros=[]
for i in range(n):
    for j in range(m):
        if arr[i][j]==0:
            zeros.append((i,j))

def get_combination(zeros):
    result=[]
    def dfs(start,combination):
        if len(combination)==3:
            result.append(combination[:])
            return
        for i in range(start,len(zeros)):
            combination.append(zeros[i])
            dfs(i+1,combination)
            combination.pop()
    dfs(0,[])
    return result

combinations=get_combination(zeros)
for walls in combinations:
    answer=max(answer,bfs(walls))
print(answer)



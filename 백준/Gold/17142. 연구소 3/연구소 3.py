from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
global_viruses = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            global_viruses.append((i, j))
answer = N * N + 1
def bfs(arr, viruses):
    visit = [[-1] * N for _ in range(N)]
    q = deque()
    for virus in viruses:
        q.append(virus)
        visit[virus[0]][virus[1]] = 0
    while q:
        pi, pj = q.popleft()
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni, nj = pi + di, pj + dj
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] == 0 and visit[ni][nj] == -1:
                    visit[ni][nj] = visit[pi][pj] + 1
                    q.append((ni, nj))
                elif arr[ni][nj] == 1:
                    continue
                elif arr[ni][nj] == 2 and visit[ni][nj] == -1:
                    visit[ni][nj] = visit[pi][pj]+ 1
                    q.append((ni,nj))
    local_max = 0
    possible = True
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0 and visit[i][j] == -1:
                possible = False
                return local_max, possible
            elif arr[i][j]==0:
                local_max=max(local_max,visit[i][j])
    return local_max, possible



def dfs(start,local_viruses):
    global answer
    if len(local_viruses)==M:
        local_max, possible=bfs(arr,local_viruses)
        if possible:
            answer=min(answer,local_max)
        return
    for i in range(start,len(global_viruses)):
        local_viruses.append(global_viruses[i])
        dfs(i+1,local_viruses)
        local_viruses.pop()
dfs(0,[])
if answer==N*N+1:
    print(-1)
else:
    print(answer)

'''
4 2
2 1 1 2
0 1 0 2
1 1 1 2
0 0 0 2
'''
import sys
from collections import deque

n, m = map(int, input().split())
gp = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


# 2의 위치 찾기
def find_goal(nn, mm, dp):
    for i in range(nn):
        for j in range(mm):
            if dp[i][j] == 2:
                return [i, j]


# 2의 위치
goal = find_goal(n, m, gp)
goal_x = goal[0]
goal_y = goal[1]

q = deque()
q.append((goal_x, goal_y))
while q:
    x, y = q.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m and gp[nx][ny] == 1 and visited[nx][ny] == 0:
            q.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1

# 가지 못하는 1은 -1로 처리
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and gp[i][j] == 1:
            visited[i][j] = -1
# 답안 출력
for i in range(n):
    for j in range(m):
        print(visited[i][j], end=' ')
    print()
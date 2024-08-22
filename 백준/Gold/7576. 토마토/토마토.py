from collections import deque

m, n = map(int, input().split())
tomato_box = [list(map(int, input().split())) for _ in range(n)]

day = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque()

for i in range(n):
    for j in range(m):
        if tomato_box[i][j] == 1:
            queue.append((i, j))
while queue:
    nx, ny = queue.popleft()
    for d in range(4):
        x = nx + dx[d]
        y = ny + dy[d]
        if 0 <= x < n and 0 <= y < m and tomato_box[x][y] == 0:
            queue.append((x, y))
            tomato_box[x][y] = tomato_box[nx][ny] + 1


def answer():
    for i in range(n):
        for j in range(m):
            if tomato_box[i][j] == 0:
                return -1
    maxi = 0
    for i in range(n):
        maxi = max(maxi, max(tomato_box[i]))
    maxi -= 1
    return maxi


print(answer())
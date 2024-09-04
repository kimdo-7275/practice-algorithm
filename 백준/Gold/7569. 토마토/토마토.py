import sys
from collections import deque

m, n, h = map(int, input().split())

gp = [[[int(i) for i in sys.stdin.readline().split()] for _ in range(n)] for _ in range(h)]

day = 0

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(h)]
q = deque()
# 처음 토마토 위치 찾기
for i in range(h):
    for j in range(n):
        for k in range(m):
            if gp[i][j][k] == 1:
                visited[i][j][k] = True
                q.append((i, j, k))
while q:
    for _ in range(len(q)):
        nz, ny, nx = q.popleft()
        for d in range(6):
            x = nx + dx[d]
            y = ny + dy[d]
            z = nz + dz[d]
            if 0 <= x < m and 0 <= y < n and 0 <= z < h and not visited[z][y][x] and gp[z][y][x] == 0:
                gp[z][y][x] = 1
                q.append((z, y, x))
                visited[z][y][x] = True
    day += 1
day-=1

# 모두 익었는지 체크하는 함수
def check(day):
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if gp[i][j][k] == 0:
                    return -1
    return day


# 정답
print(check(day))

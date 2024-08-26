import sys
from collections import deque

n = int(input())
gp = [[i for i in sys.stdin.readline().strip()] for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


# check 함수
def check():
    count_1 = 0
    queue_1 = deque()
    visited = [[False for _ in range(n)] for _ in range(n)]
    queue_1.append((0, 0))
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                queue_1.append((i, j))
                count_1 += 1
                while queue_1:
                    x, y = queue_1.pop()
                    for nn in range(4):
                        nx = x + dx[nn]
                        ny = y + dy[nn]
                        if 0 <= nx < n and 0 <= ny < n and gp[nx][ny] == gp[x][y] and not visited[nx][ny]:
                            visited[nx][ny] = True
                            queue_1.append((nx, ny))
    return count_1


answer_1 = check()
for i in range(n):
    for j in range(n):
        if gp[i][j] == 'G':
            gp[i][j] = 'R'
answer_2 = check()

print(answer_1, end=' ')
print(answer_2)

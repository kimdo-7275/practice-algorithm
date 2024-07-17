import sys

t = int(input())
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    gp = [[0] * m for i in range(n)]
    for _ in range(k):
        a, b = map(int, sys.stdin.readline().split())
        gp[b][a] = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    count = 0
    for i in range(m):
        for j in range(n):
            if gp[j][i] == 0:
                continue
            else:  # gp[n][m]==1일 경우
                count += 1
                lst = []
                lst.append((j, i))
                gp[j][i] = 0
                while lst:
                    x, y = lst.pop()
                    for q in range(4):
                        nx = x + dx[q]
                        ny = y + dy[q]
                        if 0 <= nx < n and 0 <= ny < m and gp[nx][ny] == 1:
                            lst.append((nx, ny))
                            gp[nx][ny] = 0
    print(count)
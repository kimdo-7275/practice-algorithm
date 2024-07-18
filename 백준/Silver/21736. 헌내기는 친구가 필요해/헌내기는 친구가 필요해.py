import sys

n, m = map(int, sys.stdin.readline().split())
gp = []
for _ in range(n):
    st = sys.stdin.readline().strip()
    lst = [i for i in st]
    gp.append(lst)

# I 위치 찾기
find = False
for i in range(n):
    for j in range(m):
        if gp[i][j] == 'I':
            find = True
            location = [i, j]
            break
    if find:
        break
# P 찾아 가보자
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

count = 0
lst = [location]

while lst:
    x, y = lst.pop()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if gp[nx][ny] == 'O':
                gp[nx][ny] = 'I'
                lst.append([nx, ny])
            elif gp[nx][ny] == 'P':
                count += 1
                gp[nx][ny] = 'I'
                lst.append([nx, ny])

# 정답 출력
if count != 0:
    print(count)
else:
    print('TT')
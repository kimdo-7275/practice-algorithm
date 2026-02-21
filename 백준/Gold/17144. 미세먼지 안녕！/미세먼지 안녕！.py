r, c ,t= map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
# 로봇 좌표 구하기
air_robot = []
for i in range(r):
    if arr[i][0] == -1:
        air_robot.append(i)
u_i, u_j, d_i, d_j = air_robot[0], 0, air_robot[1], 0

# 1. 미세먼지 확산(동시)
#   확산할 때는 나누기5해서 소숫점 버리기 -> 남은 미세먼지는 확산된 만큼 빼기
def difuse(arr):
    new_arr = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if arr[i][j] == 0:
                continue
            elif arr[i][j] == -1:
                new_arr[i][j] = -1
                continue
            else:
                new_arr[i][j] += arr[i][j]
                t = arr[i][j] // 5
                for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < r and 0 <= nj < c and arr[ni][nj] != -1:
                        new_arr[ni][nj] += t
                        new_arr[i][j] -= t
    return new_arr


# 2. 공기청정기 작동
#   위쪽은 반시계 순환(0,1,2,3 순서), 아래쪽은 시계 순환(0,3,2,1 순서)
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def air_rotate(arr):
    # 위쪽 반신계 순환 먼저
    d = 0
    pre=0
    pi, pj = u_i + dx[d], u_j + dy[d]
    while (pi, pj) != (u_i, u_j):
        if not (0 <= pi < r and 0 <= pj < c):
            pi, pj = pi - dx[d], pj - dy[d]
            d=(d+1)%4
            pi, pj = pi + dx[d], pj + dy[d]
            continue
        tmp=arr[pi][pj]
        arr[pi][pj]=pre
        pre=tmp
        pi, pj = pi + dx[d], pj + dy[d]
    # 아래쪽 시계 순환
    d = 0
    pre = 0
    pi, pj = d_i + dx[d], d_j + dy[d]
    while (pi, pj) != (d_i, d_j):
        if not (0 <= pi < r and 0 <= pj < c):
            pi, pj = pi - dx[d], pj - dy[d]
            d = (d - 1) % 4
            pi, pj = pi + dx[d], pj + dy[d]
            continue
        tmp = arr[pi][pj]
        arr[pi][pj] = pre
        pre = tmp
        pi, pj = pi + dx[d], pj + dy[d]
    return arr
# T초가 지난 후 남아있는 미세먼지의 양
def remain(arr):
    remaining=0
    for i in range(r):
        for j in range(c):
            if arr[i][j]>0:
                remaining+=arr[i][j]
    return remaining
for _ in range(t):
    arr=difuse(arr)
    arr=air_rotate(arr)
print(remain(arr))
# N*M의 공간
N, M = map(int,input().split())

# (r,c)초기 위치, d=0,1,2,3 -> 북동남서
r,c,d=map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]

# 방향들 -> 0123(북동남서) 고려해서 설정
dx=[-1,0,1,0]
dy=[0,1,0,-1]

# 범위 확인용
def in_range(x,y):
    return 0 <= x < N and 0 <= y < M

def cleaner(x,y,d):
    count = 0

    while True:
        # 1번 청소 하는 경우
        if grid[x][y] == 0:
            grid[x][y] =- 1
            count += 1

    # 2번 주변 4칸 확인 하기
        for _ in range(4):
            d = (d-1) % 4
            nx, ny = x+dx[d], y+dy[d]
            if in_range(nx,ny) and grid[nx][ny] == 0: # 주변에 청소 안한거 발견!
                x, y = nx, ny
                break # 다시 1번 조건확인하고 청소하러 갑니다.
    # 3번 -> 4칸 깨끗하고 뒤로 한칸 가자
        else:
            x, y = x+dx[d]*(-1), y+dy[d]*(-1) # 후진
            if in_range(x, y) and grid[x][y] == 1:
                print(count)
                return

cleaner(r,c,d)




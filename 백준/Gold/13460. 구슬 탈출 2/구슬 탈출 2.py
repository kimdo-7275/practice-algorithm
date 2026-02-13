from collections import deque



def move(i, j, di, dj):
    cnt = 0
    while True:
        i += di
        j += dj
        cnt += 1
        if arr[i][j] == '#':
            return i - di, j - dj, cnt - 1
        elif arr[i][j] == 'O':
            return i, j, cnt


n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

# 구멍 찾기
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'O':
            hi, hj = i, j
        elif arr[i][j] == 'R':
            ri, rj = i, j
        elif arr[i][j] == 'B':
            bi, bj = i, j
# r_visit = [[0] * m for _ in range(n)]
# b_visit = [[0] * m for _ in range(n)]
visited = [[[[0] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

def bfs(ri, rj, bi, bj):
    q = deque()
    q.append((ri, rj, bi, bj))
    # r_visit[ri][rj] = 1
    # b_visit[bi][bj] = 1
    visited[ri][rj][bi][bj]=1
    count = 0
    while q:
        count += 1
        if count > 10:
            print(-1)
            return
        for _ in range(len(q)):
            pri, prj, pbi, pbj = q.popleft()
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ri, rj, r_cnt = move(pri, prj, di, dj)
                bi, bj, b_cnt = move(pbi, pbj, di, dj)

                # 파란공 구멍에 빠진 경우 패스~
                if (bi, bj) == (hi, hj):
                    continue
                # 빨간공만 빠지면 성공
                if (ri, rj) == (hi, hj):
                    print(count)
                    return
                # 빨간공 파란공 겹치면 처리하기
                if (ri, rj) == (bi, bj):
                    if r_cnt > b_cnt:
                        ri -= di
                        rj -= dj
                    elif r_cnt < b_cnt:
                        bi -= di
                        bj -= dj
                # 둘중에 하나라도 방문한 적이 없어야한다.
                if visited[ri][rj][bi][bj] == 1:
                    continue
                visited[ri][rj][bi][bj]=1
                q.append((ri, rj, bi, bj))
    print(-1)


bfs(ri, rj, bi, bj)

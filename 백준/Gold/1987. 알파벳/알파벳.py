import sys
r, c = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(r)]
def solve():
    queue = set([(0, 0, board[0][0])])
    max_dist = 0

    while queue:
        i, j, path = queue.pop()
        max_dist = max(max_dist, len(path))

        # 4방향 탐색
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni, nj = i + di, j + dj

            if 0 <= ni < r and 0 <= nj < c:
                # 새로운 알파벳인 경우만 큐에 추가
                if board[ni][nj] not in path:
                    queue.add((ni, nj, path + board[ni][nj]))

    return max_dist


print(solve())
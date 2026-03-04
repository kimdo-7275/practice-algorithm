from collections import deque
def my_print(arr):
    for ar in arr:
        print(*ar)
    print('=========')
N, M, OIL = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
# board에 taxi는 -1로, guest는 2부터 표시하자
ti, tj = map(lambda x: int(x) - 1, input().split())
guest = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]
guest_visit = [0] * M
for i in range(M):
    idx = i + 2
    si, sj, ei, ej = guest[i]
    board[si][sj] = idx
# my_print(board)

def min_guest(ti, tj):
    if board[ti][tj]>1:
        guest_visit[board[ti][tj] - 2] = 1
        idx=board[ti][tj]
        board[ti][tj]=0
        return (ti, tj, 0,idx)
    visit = [[0] * N for _ in range(N)]
    q = deque()
    q.append((ti, tj))
    visit[ti][tj] = 1
    while q:
        candi=[]
        for _ in range(len(q)):
            pi, pj = q.popleft()
            for di, dj in ((-1, 0), (0, -1), (0, 1), (1, 0)):
                ni, nj = pi + di, pj + dj
                if 0 <= ni < N and 0 <= nj < N and not visit[ni][nj] and board[ni][nj] != 1:
                    if board[ni][nj] == 0:
                        q.append((ni, nj))
                        visit[ni][nj] = visit[pi][pj] + 1
                    elif board[ni][nj] != 0 and not guest_visit[board[ni][nj] - 2]:
                        visit[ni][nj]=visit[pi][pj]+1
                        candi.append((ni,nj,visit[pi][pj],board[ni][nj]))


        if candi:
            candi.sort(key=lambda x:(x[0],x[1]))
            guest_visit[candi[0][3]-2]=1
            board[candi[0][0]][candi[0][1]]=0
            return candi[0]
    if sum(guest_visit) != M:
        return False  # 손님 남았는데 다음 손님 못찾은 경우


def go_to_desti(si, sj,idx):   # 목적지까지 거리만 return
    _, _, ei, ej = guest[idx - 2]  # 택시 도착 위치
    if (si,sj)==(ei,ej):
        return(ei,ej,0)
    visit = [[0] * N for _ in range(N)]
    q = deque()
    q.append((si, sj))
    visit[si][sj] = 1
    while q:
        pi, pj = q.popleft()
        for di, dj in ((-1, 0), (0, -1), (0, 1), (1, 0)):
            ni, nj = pi + di, pj + dj
            if 0 <= ni < N and 0 <= nj < N and not visit[ni][nj] and board[ni][nj] != 1:
                if (ni,nj)==(ei,ej):
                    return (ni, nj, visit[pi][pj])  # 도착지랑 이동한 거리
                else:
                    q.append((ni,nj))
                    visit[ni][nj]=visit[pi][pj]+1
    return False

while True:
    if sum(guest_visit)==M:
        print(OIL)
        break
    case1 = min_guest(ti, tj)

    if case1:
        si,sj,dis1,idx=case1
    else:
        print(-1)
        break
    if OIL<dis1:
        print(-1)
        break
    OIL-=dis1
    case2=go_to_desti(si,sj,idx)
    if case2:
        gi, gj, dis2 = case2
        if dis2>OIL:
            print(-1)
            break
        else:
            OIL+=dis2
    else:

        print(-1)
        break
    ti,tj=gi,gj

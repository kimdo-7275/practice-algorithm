def my_print(arr):
    for ar in arr:
        print(*ar)
    print('==========')


start_board = [[0] * 4 for _ in range(4)]
start_fishes = [[0] * 3 for _ in range(17)]
# 물고기 죽은어 fishes에 표시할 때는 방향에 -1 저장해놓기
for i in range(4):
    a, ad, b, bd, c, cd, d, dd = map(int, input().split())
    start_board[i][0], start_board[i][1], start_board[i][2], start_board[i][3] = a, b, c, d
    start_fishes[a], start_fishes[b], start_fishes[c], start_fishes[d] = [i, 0, ad - 1], [i, 1, bd - 1], [i, 2,
                                                                                                          cd - 1], [i,
                                                                                                                    3,
                                                                                                                    dd - 1]
# my_print(start_board)

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
total_fish = 0
for i in range(1, 17):
    total_fish += i
answer = 0


def move_fishes(board, fishes, si, sj):  # si,sj 상어 위치임
    for fish_num in range(1, 17):
        # 죽은 물고기는 패스
        if fishes[fish_num][2] == -1:
            continue
        fi, fj, now_d = fishes[fish_num]
        # 8방향 돌아보기
        for i in range(8):
            chg_d = (now_d + i) % 8
            ni, nj = fi + dx[chg_d], fj + dy[chg_d]
            if 0 <= ni < 4 and 0 <= nj < 4 and (ni, nj) != (si, sj):
                # 이동할 자리에 물고기 없는 경우
                if board[ni][nj] == 0:
                    board[fi][fj], board[ni][nj] = 0, fish_num
                    fishes[fish_num] = [ni, nj, chg_d]
                # 물고기랑 바꾸는 경우
                else:
                    board[fi][fj], board[ni][nj] = board[ni][nj], board[fi][fj]
                    fishes[fish_num], fishes[board[fi][fj]] = [ni, nj, chg_d], [fi, fj, fishes[board[fi][fj]][2]]
                break
    return board, fishes


def eat_fish(board):
    remain_fish = 0
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                remain_fish += board[i][j]
    return total_fish - remain_fish


def dfs(board, fishes, si, sj, sd):
    global answer
    board, fishes = move_fishes(board, fishes, si, sj)
    # print(f'물고기 다 움직임 : 상어위치는 {si,sj}')
    # my_print(board)
    shark_can_move = False
    for i in range(1, 4):
        nsi, nsj = si + dx[sd] * i, sj + dy[sd] * i
        if 0 <= nsi < 4 and 0 <= nsj < 4 and board[nsi][nsj]:
            shark_can_move = True
            n_board = [x[:] for x in board]
            n_fishes = [x[:] for x in fishes]
            fish_num = n_board[nsi][nsj]
            n_board[nsi][nsj] = 0
            nsd = n_fishes[fish_num][2]
            n_fishes[fish_num][2] = -1
            # print(f"상어 움직임 : {si,sj}에서 {nsi,nsj}로 움직임")
            # my_print(n_board)
            dfs(n_board, n_fishes, nsi, nsj, nsd)
    if shark_can_move == False:
        answer = max(answer, eat_fish(board))
        return


start_fish = start_board[0][0]
start_board[0][0] = 0
start_d = start_fishes[start_fish][2]
start_fishes[start_fish][2] = -1
# my_print(start_board)
# board, fishes = move_fishes(start_board, start_fishes, 0, 0)
# my_print(board)
dfs(start_board,start_fishes,0,0,start_d)
print(answer)

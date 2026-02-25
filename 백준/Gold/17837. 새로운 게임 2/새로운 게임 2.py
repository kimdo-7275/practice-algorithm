N,K=map(int,input().split())
color_board=[list(map(int,input().split())) for _ in range(N)]
# 방향 바꿀 때 1,3이면 1더하고 2,4이면 1빼기로 방향 바꾸면 됨.
dx=[0,0,0,-1,1]
dy=[0,1,-1,0,0]
horses_board={} # 여기 안에는 번호 : [i,j,d,자기 아래, 자기 위에] 이렇게 들어가 ㄹ듯?
up_board=[[0]*N for _ in range(N)]  # 가장 위에 있는 번호 말
for idx in range(1,K+1):
    i,j,d=map(int,input().split())
    horses_board[idx]=[i-1,j-1,d,0,0]
    up_board[i-1][j-1]=idx
def white(idx,pi,pj,ni,nj,d,pre,nx):
    if pre==0:
        up_board[pi][pj]=pre
    else:
        horses_board[pre][4]=0
        horses_board[idx][3]=0
        up_board[pi][pj] = pre
    while idx!=0:
        nx=horses_board[idx][4]
        if up_board[ni][nj]!=0:
            horses_board[up_board[ni][nj]][4]=idx
        horses_board[idx]=[ni,nj,horses_board[idx][2],up_board[ni][nj],0]
        up_board[ni][nj]=idx
        idx=nx
def red(idx,pi,pj,ni,nj,d,pre,nx):
    if pre==0:
        up_board[pi][pj]=pre
    else:
        horses_board[pre][4]=0
        horses_board[idx][3] = 0
        up_board[pi][pj] = pre
    stack=[]
    while idx!=0:
        stack.append(idx)
        idx=horses_board[idx][4]

    while stack:
        idx=stack.pop()
        nx=horses_board[idx][3]
        if up_board[ni][nj]!=0:
            horses_board[up_board[ni][nj]][4]=idx
        horses_board[idx] = [ni, nj, horses_board[idx][2], up_board[ni][nj], nx]
        up_board[ni][nj]=idx


def blue(idx,pi,pj,d,pre,nx):
    if d==1 or d==3:
        d+=1
    else:
        d-=1
    horses_board[idx][2]=d
    ni, nj = pi + dx[d], pj + dy[d]
    if (not (0 <= ni < N and 0 <= nj < N)) or color_board[ni][nj] == 2:
        return
    elif color_board[ni][nj] == 1:
        red(idx, pi, pj, ni, nj, d, pre, nx)
    elif color_board[ni][nj] == 0:
        white(idx, pi, pj, ni, nj, d, pre, nx)

def count(c_num):
    count_num=0
    while c_num!=0:
        count_num+=1
        c_num=horses_board[c_num][3]
    return count_num
# white(1,1,0,1,1,1,0,0)
# white(2,2,1,1,1,3,0,0)
# red(3,1,1,1,2,1,0,1)
#
#
# print(horses_board)
# print(up_board)
def answer():
    for turn in range(1,1002):
        if turn==1001:
            print(-1)
            return
        for idx in range(1,K+1):
            pi,pj,d,pre,nx=horses_board[idx]
            ni,nj=pi+dx[d],pj+dy[d]
            # 범위 밖일 때
            if (not (0<=ni<N and 0<=nj<N)) or color_board[ni][nj]==2:
                blue(idx,pi,pj,d,pre,nx)
                c_num=up_board[horses_board[idx][0]][horses_board[idx][1]]
                if count(c_num)>=4:
                    print(turn)
                    return
            elif color_board[ni][nj]==1:
                red(idx,pi,pj,ni,nj,d,pre,nx)
                c_num = up_board[horses_board[idx][0]][horses_board[idx][1]]
                if count(c_num) >= 4:
                    print(turn)
                    return
            elif color_board[ni][nj]==0:
                white(idx,pi,pj,ni,nj,d,pre,nx)
                c_num = up_board[horses_board[idx][0]][horses_board[idx][1]]
                if count(c_num) >= 4:
                    print(turn)
                    return
        # print(f"turn : {turn}")
        # print(f"horses_board : {horses_board}")
        # print(f"up_board : ")
        # for ar in up_board:
        #     print(*ar)
        # print('==================================')
answer()

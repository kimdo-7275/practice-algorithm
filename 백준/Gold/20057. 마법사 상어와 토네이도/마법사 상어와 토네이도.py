N=int(input())
graph=[list(map(int, input().split())) for _ in range(N)]
def in_range(x,y):
    return 0<=x<N and 0<=y<N
def rotate_90(proportion):
    return list(map(list,zip(*proportion)))[::-1]

p=[[0,0,0.02,0,0],
   [0,0.1,0.07,0.01,0],
   [0.05,0,0,0,0],
   [0,0.1,0.07,0.01,0],
   [0,0,0.02,0,0]]
p1=rotate_90(p)
p2=rotate_90(p1)
p3=rotate_90(p2)
proportions=[p,p1,p2,p3]

directions=[[0,-1],[1,0],[0,1],[-1,0]] # 토네이도의 방향 : 좌->하->우->상
tr=tc=N//2 # 처음 토네이도 위치

out_sand=0 # 버리는 모래
cur_direction=0 #현재방향
turn=2 # 회전변수(2씩 늘어난다) 1+1,2+2,3+3
now_lenght=0 # 한칸씩 이동한 수
proportion=proportions[0] # 초기방향(왼쪽)
alpha=[(2,1),(3,2),(2,3),(1,2)]

while not (tr==0 and tc==0):

    # 토네이도 이동
    tr+=directions[cur_direction][0]
    tc+=directions[cur_direction][1]
    now_lenght+=1 # 토네이도 길이 갱신
    sand = graph[tr][tc]
    graph[tr][tc]=0
    left=sand

    # 비율에 맞게 모래정보 갱신
    for r in range(5):
        for c in range(5):
            now_sand=int(proportion[r][c]*sand)
            left-=now_sand
            if in_range(tr+r-2, tc+c-2):
                graph[tr+r-2][tc+c-2]+=now_sand
            else:
                out_sand+=now_sand

    # 남은거 알파에 두기
    if in_range(tr+alpha[cur_direction][0]-2,tc+alpha[cur_direction][1]-2):
        graph[tr+alpha[cur_direction][0]-2][tc+alpha[cur_direction][1]-2]+=left
    else:
        out_sand+=left

    # 방향 돌리기
    if now_lenght==turn or now_lenght==turn//2:
        cur_direction=(cur_direction+1) % 4 # 방향바꿔주고
        proportion=proportions[cur_direction] # 비율 그래프도 바꿔주고
        if now_lenght==turn:
            now_lenght=0
            turn+=2
print(out_sand)



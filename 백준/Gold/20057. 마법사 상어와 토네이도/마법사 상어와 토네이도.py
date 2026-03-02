N=int(input())
remain=0
arr=[list(map(int,input().split())) for _ in range(N)]
si,sj=N//2,N//2
dx=[0,1,0,-1]
dy=[-1,0,1,0]

p=[[0,0,0.02,0,0],
     [0,0.1,0.07,0.01,0],
     [0.05,0,0,0,0],
     [0,0.1,0.07,0.01,0],
     [0,0,0.02,0,0]]

def rotate_90(lst):
    return [list(y) for y in zip(*[x[::-1] for x in lst])]
p1=rotate_90(p)
p2=rotate_90(p1)
p3=rotate_90(p2)
ps=[p,p1,p2,p3]

answer=0
d=0
cg_l=0
cnt=0
goal=1
while not (si==0 and sj==0):
    if cnt<goal:
        ni,nj=si+dx[d],sj+dy[d]
        cnt+=1
    elif cnt==goal:
        d=(d+1)%4
        if cg_l==0:
            cg_l+=1
            cnt=1
            ni, nj = si + dx[d], sj + dy[d]
        elif cg_l==1:
            cg_l-=1
            cnt=1
            goal+=1
            ni, nj = si + dx[d], sj + dy[d]
    # 여기에 할 거 하고
    total=arr[ni][nj]
    move_sand=0
    for i in range(5):
        for j in range(5):
            if ps[d][i][j]==0:
                continue
            pi,pj=ni-2+i,nj-2+j
            if not (0<=pi<N and 0<=pj<N):
                answer+=int(total*ps[d][i][j])
                move_sand+=int(total*ps[d][i][j])
            else:
                move_sand+=int(total*ps[d][i][j])
                arr[pi][pj]+=int(total*ps[d][i][j])
    remain=total-move_sand
    if 0<=ni+dx[d]<N and 0<=nj+dy[d]<N:
        arr[ni+dx[d]][nj+dy[d]]+=remain
    else:
        answer+=remain
    si,sj=ni,nj
print(answer)




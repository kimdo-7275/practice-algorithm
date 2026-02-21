R,C,M=map(int,input().split())
arr=[[[] for _ in range(C)] for _ in range(R)]
dx=[0,-1,1,0,0]
dy=[0,0,0,1,-1]
# 1,2,3,4 = 위,아래,오른쪽,왼쪽
for _ in range(M):
    r,c,s,d,z=map(int,input().split())
    arr[r-1][c-1].append((s,d,z))   # s는 속력, d는 이동방향, z는 크기

answer=0
man_idx=-1
while man_idx<C-1:
    man_idx+=1
    # 해당 열에 있는 가장 가까운 상어 잡기
    for i in range(R):
        if arr[i][man_idx]:
            answer+=arr[i][man_idx][0][2]
            arr[i][man_idx].pop()
            break
    # 상어 이동하기
    new_arr=[[[] for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if arr[i][j]:
                pi,pj=i,j
                ps,pd,pz=arr[i][j][0]
                if pd==1 or pd==2:
                    tps=ps%(2*R-2)
                else:
                    tps=ps%(2*C-2)
                for _ in range(tps):
                    if 0<=pi+dx[pd]<R and 0<=pj+dy[pd]<C:
                        pi,pj=pi+dx[pd],pj+dy[pd]
                    else:
                        if pd%2==0: # 짝수
                            pd-=1
                        else:
                            pd+=1
                        pi, pj = pi + dx[pd], pj + dy[pd]
                if new_arr[pi][pj]:
                    if new_arr[pi][pj][0][2]>pz:
                        continue
                    else:
                        new_arr[pi][pj]=[(ps,pd,pz)]
                else:
                    new_arr[pi][pj].append((ps,pd,pz))
    arr=new_arr

print(answer)
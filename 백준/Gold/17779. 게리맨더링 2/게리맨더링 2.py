
N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)]

def make_area(x,y,d1,d2):
    new_arr = [[0] * N for _ in range(N)]
    if not (x+d1+d2<N) or not (y-d1>=0) or not (y+d2<N):
        return new_arr , False

    # 5 채우기
    for i in range(d1):
        new_arr[x+i][y-i]=5
        new_arr[x+d1+d2-i][y-d1+d2+i]=5
    for i in range(d2):
        new_arr[x+d1+i][y-d1+i]=5
        new_arr[x+d2-i][y+d2-i]=5
    visit=[[0]*N for _ in range(N)]
    visit[x+d1][y-d1]=1
    visit[x+d2][y+d2]=1
    for i in range(N):
        for j in range(N):
            if new_arr[i][j]==5 and not visit[i][j]:
                visit[i][j]=1
                for di in range(1,N):
                    ni=i+di
                    if 0<=ni<N:
                        if not visit[ni][j] and new_arr[ni][j]==0:
                            visit[ni][j]=1
                            new_arr[ni][j]=5
                        elif not visit[ni][j] and new_arr[ni][j]==5:
                            visit[ni][j]=1
                            break
                    else:
                        break


    # 1 채우기
    for i in range(x+d1):
        for j in range(y+1):
            if new_arr[i][j]==5:
                break
            elif new_arr[i][j]==0:
                new_arr[i][j]=1
    # 2 채우기
    for i in range(x+d2+1):
        for j in range(-1,-N+y,-1):
            if new_arr[i][j]==5:
                break
            elif new_arr[i][j]==0:
                new_arr[i][j]=2
    # 3 채우기
    for i in range(x+d1,N):
        for j in range(y+-d1+d2):
            if new_arr[i][j]==5:
                break
            elif new_arr[i][j]==0:
                new_arr[i][j]=3
    # 4 채우기
    for i in range(x+d2+1,N):
        for j in range(-1,-N+(y-d1+d2)-1,-1):
            if new_arr[i][j]==5:
                break
            elif new_arr[i][j]==0:
                new_arr[i][j]=4
    return new_arr,True

def cal_area(new_arr):
    d={}
    for i in range(N):
        for j in range(N):
            if new_arr[i][j] not in d:
                d[new_arr[i][j]]=arr[i][j]
            else:
                d[new_arr[i][j]]+=arr[i][j]
    lst=[]
    for i in d:
        lst.append(d[i])
    return max(lst)-min(lst)
answer=N*N*100
for i in range(N):
    for j in range(N):
        for d1 in range(1,N):
            for d2 in range(1,N):
                new_arr, possible=make_area(i, j, d1, d2)
                if not possible:
                    continue
                else:
                    local=cal_area(new_arr)
                    answer=min(answer,cal_area(new_arr))
                    if local==15:
                        for ar in new_arr:
                            print(*ar)

print(answer)
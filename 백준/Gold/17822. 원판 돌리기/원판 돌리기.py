from collections import deque
N,M,T=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]

def rotate(x,d,k,arr):
    if d==0:    # 시계방향
        for i in range(x,N+1,x):
            new_arr=[0]*M
            for j in range(M):
                new_arr[(j+k)%M]=arr[i-1][j]
            arr[i-1]=new_arr[:] # 이거 테스트 해보기!!!
    elif d==1:  # 반시계방향
        for i in range(x,N+1,x):
            new_arr=[0]*M
            for j in range(M):
                new_arr[(j-k)%M]=arr[i-1][j]
            arr[i-1]=new_arr[:] # 이거 테스트 해보기!!!
    return arr
def plate_empty(arr):
    for i in range(N):
        for j in range(M):
            if arr[i][j]!=0:
                return False
    return True

def find_del_num(arr):
    is_change=False
    visit=[[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if not visit[i][j]:
                visit[i][j] = 1
                if arr[i][j] == 0:
                    continue
                del_lst=[(i,j)]
                for dx,dy in ((-1,0),(1,0),(0,1),(0,-1)):
                    ni,nj=i+dx,(j+dy)%M
                    if 0<=ni<N:
                        if arr[ni][nj]==arr[i][j]:
                            del_lst.append((ni,nj))
                            break
                if len(del_lst)==1:
                    continue
                is_change=True
                q=deque()
                del_num=arr[i][j]
                q.append((i,j))
                arr[i][j]=0
                while q:
                    pi,pj=q.popleft()
                    for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                        ni, nj = pi + dx, (pj + dy) % M
                        if 0<=ni<N:
                            if arr[ni][nj]==del_num:
                                visit[ni][nj]=1
                                arr[ni][nj]=0
                                q.append((ni,nj))
    return is_change,arr
def sum_plate(arr):
    su=0
    nu=0
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                nu+=1
                su+=arr[i][j]
    avg=su/nu
    for i in range(N):
        for j in range(M):
            if arr[i][j]!=0:
                if arr[i][j]>avg:
                    arr[i][j]-=1
                elif arr[i][j]<avg:
                    arr[i][j]+=1
    return arr


for _ in range(T):
    xi,di,ki=map(int,input().split())
    arr=rotate(xi,di,ki,arr)
    if plate_empty(arr):
        break
    is_change,arr=find_del_num(arr)
    if is_change:
        pass
    else:
        arr=sum_plate(arr)

answer=0
for ar in arr:
    answer+=sum(ar)
print(answer)



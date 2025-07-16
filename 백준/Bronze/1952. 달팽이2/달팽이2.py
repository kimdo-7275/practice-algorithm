m,n = map(int,input().split())
arr = [[0]*n for _ in range(m)]
arr[0][0]=1
si,sj=0,0
di=[0,1,0,-1]
dj=[1,0,-1,0]
d=0
answer=0
while True:
    ni,nj = si+di[d], sj+dj[d]
    if 0<=ni<m and 0<=nj<n and arr[ni][nj]==0:
        si,sj=ni,nj
        arr[ni][nj]=1
    elif arr[si+di[(d+1)%4]][sj+dj[(d+1)%4]]==0:
        answer+=1
        d=(d+1)%4
        ni, nj = si + di[d], sj + dj[d]
        arr[ni][nj] = 1
        si, sj = ni, nj
    else:
        break


print(answer)
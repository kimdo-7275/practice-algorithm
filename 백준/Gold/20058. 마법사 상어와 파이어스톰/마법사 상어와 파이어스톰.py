from collections import deque
N, Q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(2 ** N)]
L = list(map(int, input().split()))


def my_print_2d(arr):
    for ar in arr:
        print(*ar)


def all_rotate(l, arr):
    new_arr = [[0] * 2 ** N for _ in range(2 ** N)]
    length = 2 ** l
    for i in range(0, 2 ** N, length):
        for j in range(0, 2 ** N, length):
            for ii in range(length):
                for jj in range(length):
                    new_arr[i + ii][j + jj] = arr[i + length - 1 - jj][j + ii]
    return new_arr


def melt_ice(arr):
    new_arr = [x[:] for x in arr]
    for i in range(2 ** N):
        for j in range(2 ** N):
            if arr[i][j] == 0:
                continue
            cnt = 0
            for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                ni, nj = i + di, j + dj
                if not (0 <= ni < 2 ** N and 0 <= nj < 2 ** N):
                    continue
                elif arr[ni][nj] == 0:
                    continue
                else:
                    cnt += 1
            if cnt < 3:
                new_arr[i][j] = arr[i][j] - 1
            else:
                new_arr[i][j] = arr[i][j]
    return new_arr

for l in L:
    arr=all_rotate(l,arr)
    arr=melt_ice(arr)

answer_1=0
answer_2=0

#
# for i in range(2**N):
#     for j in range(2**N):
#         answer_1+=arr[i][j]

visit=[[0]*2**N for _ in range(2**N)]
check=0
for i in range(2**N):
    for j in range(2**N):
        if arr[i][j]>0 and not visit[i][j]:
            q=deque()
            q.append((i,j))
            visit[i][j]=1
            tmp=arr[i][j]
            cnt=1
            check+=1
            while q:
                pi,pj=q.popleft()
                for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                    ni, nj = pi + di, pj + dj
                    if 0<=ni<2**N and 0<=nj<2**N and not visit[ni][nj] and arr[ni][nj]>0:
                        q.append((ni,nj))
                        cnt+=1
                        visit[ni][nj]=1
                        tmp+=arr[ni][nj]
            answer_1+=tmp
            answer_2=max(answer_2,cnt)

print(answer_1)
print(answer_2)

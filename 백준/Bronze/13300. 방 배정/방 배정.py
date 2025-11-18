n,k = map(int,input().split())
lst = [[0]*2 for _ in range(6)]
for _ in range(n):
    s,g = map(int,input().split())
    lst[g-1][s]+=1
answer = 0
for i in range(6):
    for j in range(2):
        if lst[i][j]==0:
            continue
        answer+=((lst[i][j]+k-1)//k)

print(answer)
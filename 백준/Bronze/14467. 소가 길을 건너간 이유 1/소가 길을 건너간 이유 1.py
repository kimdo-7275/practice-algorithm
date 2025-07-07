num = int(input())

lst=[-1]*11
answer=0
for _ in range(num):
    n, d = map(int, input().split())
    if lst[n]==-1:
        lst[n]=d
    elif lst[n]==0 and d==1:
        lst[n]=1
        answer+=1
    elif lst[n]==1 and d==0:
        lst[n]=0
        answer+=1
print(answer)



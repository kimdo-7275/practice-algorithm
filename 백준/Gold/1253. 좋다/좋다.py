n=int(input())
lst=list(map(int,input().split()))
lst.sort()
answer=0
for i in range(n):
    target=lst[i]
    s,e=0,n-1
    while s<e:
        if s==i:
            s+=1
            continue
        if e==i:
            e-=1
            continue
        if lst[s]+lst[e]>target:
            e-=1
        elif lst[s]+lst[e]<target:
            s+=1
        else:
            answer+=1
            break
print(answer)
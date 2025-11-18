n=int(input())
lst = list(map(int,input().split()))
m=int(input())

s = 0
e = max(lst)
answer = 0
while s<=e:
    total = 0
    h = (s+e) // 2
    for i in lst:
        total+=min(i,h)

    if total > m:
        e=h-1
    else:
        answer=h
        s=h+1
print(answer)

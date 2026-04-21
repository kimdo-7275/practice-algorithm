N=int(input())
numbers=list(map(int,input().split()))
total=int(input())
s=0
e=max(numbers)
answer=0

while s<=e:
    h=(s+e)//2
    tmp_total=0
    for number in numbers:
        tmp_total+=min(number,h)
    if tmp_total>total:
        e=h-1
        continue
    else:
        answer=h
        s=h+1
        continue
print(answer)
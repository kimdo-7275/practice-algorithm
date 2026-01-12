T=int(input())
for t in range(T):
    n=int(input())
    lst=list(map(int,input().split()))
    answer=0
    max_price=0
    for i in range(-1,-(n+1),-1):
        if lst[i] < max_price:
            answer+=(max_price-lst[i])
        else:
            max_price=lst[i]
    print(answer)
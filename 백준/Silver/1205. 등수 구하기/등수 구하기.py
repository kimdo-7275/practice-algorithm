n,new,p=map(int,input().split())
def fun():
    if n==0:
        return 1
    lst=list(map(int,input().split()))
    lst.sort(reverse=True)
    # -1을 출력하는 경우!
    if len(lst)==p and lst[-1]>=new:
        return -1
    # 그 이외 모든 케이스

    if lst[0]<=new:
        return 1

    dup = 0
    rank = 1
    for i in range(1,len(lst)):
        pre=lst[i-1]
        if pre==lst[i]:
            dup+=1
            continue
        else:
            rank+=dup
            dup=0
        if lst[i] > new:
            rank+=(dup+1)
        elif lst[i]<=new:
            return rank+1
    return rank+dup+1
print(fun())


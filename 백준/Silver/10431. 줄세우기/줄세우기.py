p = int(input())

for _ in range(p):
    lst = list(map(int,input().split()))
    t=lst[0]
    lst=lst[1:]
    answer = 0
    for i in range(1,20):
        if lst[i-1] < lst[i]:
            continue
        mn = lst[i-1] - lst[i]
        mn_idx = i-1
        for j in range(i):
            if mn>lst[j]-lst[i]>0:
                mn=lst[j]-lst[i]
                mn_idx = j
        answer+=(i-mn_idx)
        while i!=mn_idx:
            lst[i], lst[i-1] = lst[i-1], lst[i]
            i-=1
    print(t,answer)
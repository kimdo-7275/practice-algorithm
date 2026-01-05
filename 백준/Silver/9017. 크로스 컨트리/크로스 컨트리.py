T=int(input())

for t in range(T):
    n=int(input())
    lst=list(map(int,input().split()))
    d={}
    for i in range(len(lst)):
        if lst[i] not in d:
            d[lst[i]]=[i]
        else:
            d[lst[i]].append(i)
    # 6개 이하인 거 지우는 작업
    remain=[]
    for i in d:
        if len(d[i])==6:
            remain.append(i)
    d={}
    cnt=1
    for i in lst:
        if i in remain:
            if i not in d:
                d[i]=[cnt]
                cnt+=1
            else:
                d[i].append(cnt)
                cnt+=1
    max_score=float('inf')
    team=0
    for key in d:
        if len(d[key])<6:
            continue
        if max_score > sum(d[key][:4]):
            max_score=sum(d[key][:4])
            team=key
        elif max_score == sum(d[key][:4]) and d[team][4] > d[key][4]:
            max_score = sum(d[key][:4])
            team = key
    print(team)
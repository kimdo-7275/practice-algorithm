T=int(input())
for _ in range(T):
    s=input()
    k=int(input())
    d = {}
    for i in range(len(s)):
        if s[i] not in d:
            d[s[i]] = [i]
        else:
            d[s[i]].append(i)
    answer1=len(s)+1
    # 1번 문제!
    for key in d:
        if len(d[key])<k:
            continue
        for i in range(k-1,len(d[key])):
            answer1=min(answer1,d[key][i]-d[key][i-(k-1)]+1)
    answer1 = -1 if answer1==len(s)+1 else answer1
    # 2번 문제!
    answer2=-1
    for key in d:
        if len(d[key])<k:
            continue
        for i in range(k-1,len(d[key])):
            answer2=max(answer2,d[key][i]-d[key][i-(k-1)]+1)
    answer2= -1 if answer2==-1 else answer2
    if answer1==-1:
        print(answer1)
    else:
        print(answer1, answer2)

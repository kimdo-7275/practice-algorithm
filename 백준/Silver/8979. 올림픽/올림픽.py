n,k = map(int,input().split())
lst=[list(map(int,input().split())) for _ in range(n)]
lst.sort(key=lambda x:(-x[1],-x[2],-x[3]))
rank=0
pre_g, pre_s, pre_b = -1,-1,-1
answer=0
dup=0

for ls in lst:
    if ls[1]!=pre_g or ls[2]!=pre_s or ls[3]!=pre_b:
        if dup!=0:
            rank+=dup
            dup=0
            pre_g, pre_s, pre_b = ls[1],ls[2],ls[3]
        else:
            rank+=1
            pre_g, pre_s, pre_b = ls[1], ls[2], ls[3]
    elif ls[1]==pre_g and ls[2]==pre_s and ls[2]==pre_b:
        dup+=1

    if ls[0]==k:
        print(rank)
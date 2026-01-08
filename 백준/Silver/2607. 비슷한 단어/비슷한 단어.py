n=int(input())
lst=[input() for _ in range(n)]

answer=list(lst[0])
d1={}
for i in answer:
    if i not in d1:
        d1[i]=1
    else:
        d1[i]+=1

lst=lst[1:]
count=0

for s in lst:
    d2={}
    for i in s:
        if i not in d2:
            d2[i]=1
        else:
            d2[i]+=1
    plus=0
    minus=0
    for k in d1.keys():
        if k in d2:
            if d1[k]>d2[k]:
                plus+=d1[k]-d2[k]
            elif d1[k]<d2[k]:
                minus+=d2[k]-d1[k]
        else:
            plus+=d1[k]
    for k in d2.keys():
        if k not in d1:
            minus+=d2[k]
    if plus>1 or minus>1:
        continue
    else:
        count+=1
print(count)

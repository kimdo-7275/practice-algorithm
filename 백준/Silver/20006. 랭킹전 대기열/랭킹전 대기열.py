p,m=map(int,input().split())
lst=[]
for _ in range(p):
    i,n=map(str,input().split())
    find=False
    i=int(i)
    for l in lst:
        if len(l)<m and l[0][0]-10<=i<=l[0][0]+10:
            l.append((i,n))
            find=True
            break
    if not find:
        lst.append([(i,n)])

for l in lst:
    if len(l)==m:
        print("Started!")
    else:
        print("Waiting!")
    l.sort(key=lambda x:(x[1]))
    for i in l:
        print(f"{i[0]} {i[1]}")


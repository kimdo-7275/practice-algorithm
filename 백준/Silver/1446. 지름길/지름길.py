N,D=map(int,input().split())
roads=[]
for _ in range(N):
    s,e,l=map(int,input().split())
    if e>D:
        continue
    roads.append([s,e,l])
roads.sort()
arr=[float('inf')]*(D+1)
arr[0]=0
for i in range(D+1):
    if i!=0:
        arr[i]=min(arr[i],arr[i-1]+1)
    for idx in range(len(roads)):
        s,e,l=roads[idx]
        if s>i:
            break
        if s==i:
            arr[e]=min(arr[e],arr[s]+l)
print(arr[-1])
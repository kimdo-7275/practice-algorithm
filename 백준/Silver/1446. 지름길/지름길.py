n,d=map(int,input().split())
short=[list(map(int,input().split())) for _ in range(n)]
short.sort(key=lambda x:x[1])
arr=[10001]*(d+1)
arr[0]=0
for i in range(1,d+1):
    for s in short:
        if s[1]>i:
            break
        if s[1]==i:
            arr[i]=min(min(arr[i-1]+1,arr[s[0]]+s[2]),arr[i])
    arr[i]=min(arr[i-1]+1,arr[i])
print(arr[-1])
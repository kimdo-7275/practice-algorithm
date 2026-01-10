import sys
n,m=map(int,input().split())
lst=[list(map(str,sys.stdin.readline().strip().split()))for _ in range(n)]
for l in lst:
    l[1]=int(l[1])
for _ in range(m):
    a=int(sys.stdin.readline().strip())
    s=0
    e=n-1
    while s<=e:
        half=(s+e)//2
        if a > lst[half][1]:
            s=half+1
        else:
            e=half-1
    print(lst[s][0])
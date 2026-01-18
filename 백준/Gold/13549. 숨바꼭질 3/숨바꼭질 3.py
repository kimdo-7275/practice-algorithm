from collections import deque
n,k=map(int,input().split())
arr=[-1]*200004
q=deque()
q.append(n)
arr[n]=0
while q:
    p=q.popleft()
    if p==k:
        print(arr[p])
        break
    if 0<=p*2<200004 and arr[p*2]==-1:
        arr[p*2]=arr[p]
        q.append(p*2)
    elif 0<=p*2<200004 and arr[p]<arr[p*2]:
        arr[p*2]=arr[p]
        q.append(p*2)
    for i in ((p+1),(p-1)):
        if 0<=i<200004 and arr[i]==-1:
            arr[i]=arr[p]+1
            q.append(i)
        elif 0<=i<200004 and arr[p]+1 < arr[i]:
            arr[i]=arr[p]+1
            q.append(i)


n=int(input())
m=int(input())
arr=[[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    i,j = map(int,input().split())
    arr[i][j]=1
    arr[j][i]=1
visited=[0]*(n+1)
q=[1]
while q:
    t=q.pop(0)
    if visited[t]==0:
        visited[t]=1
    for i in range(n+1):
        if arr[t][i]==1 and visited[i]==0:
            q.append(i)
print(sum(visited)-1)
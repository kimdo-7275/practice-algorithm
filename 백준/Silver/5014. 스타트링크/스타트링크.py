from collections import deque
F,S,G,U,D=map(int,input().split())
visit=[-1]*(F+1)
visit[S]=0
q=deque()
q.append(S)
while q:
    p=q.popleft()
    for n in ((p+U),(p-D)):
        if 1<=n<(F+1) and visit[n]==-1:
            visit[n]=visit[p]+1
            q.append(n)
if visit[G]==-1:
    print('use the stairs')
else:
    print(visit[G])


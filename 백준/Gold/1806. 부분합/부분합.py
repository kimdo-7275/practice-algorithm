N,S=map(int,input().split())
lst=list(map(int,input().split()))
answer=N+1
s=0
sm=0
for e in range(N):
    sm+=lst[e]
    if sm<S:
        continue
    while sm>=S:
        answer=min(answer,e-s+1)
        sm-=lst[s]
        s+=1
if answer==N+1:
    print(0)
else:
    print(answer)
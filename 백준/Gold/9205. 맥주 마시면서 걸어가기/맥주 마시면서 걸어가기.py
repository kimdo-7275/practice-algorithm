from collections import deque
T=int(input())
for _ in range(T):
    n=int(input())
    home=list(map(int,input().split()))
    store=[list(map(int,input().split())) for _ in range(n)]
    visit_store=[0]*n
    festival=list(map(int,input().split()))
    q=deque()
    q.append(home)
    answer=False
    while q:
        pi,pj=q.popleft()
        for i in range(n):
            if not visit_store[i] and abs(pi-store[i][0])+abs(pj-store[i][1])<=1000:
                q.append([store[i][0],store[i][1]])
                visit_store[i]=1
        if abs(pi-festival[0])+abs(pj-festival[1])<=1000:
            answer=True
            print('happy')
            break
    if not answer:
        print('sad')





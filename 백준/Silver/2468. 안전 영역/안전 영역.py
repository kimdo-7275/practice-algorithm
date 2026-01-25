from collections import deque
n=int(input())
s=set()
arr=[list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        s.add(arr[i][j])
s=list(s)
s.append(0)
s.sort()
def bfs(k):
    answer=0
    visit=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j]>k and not visit[i][j]:
                answer+=1
                q=deque()
                q.append((i,j))
                visit[i][j]=1
                while q:
                    pi,pj=q.popleft()
                    for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                        ni,nj=pi+di,pj+dj
                        if 0<=ni<n and 0<=nj<n and not visit[ni][nj] and arr[ni][nj]>k:
                            visit[ni][nj]=1
                            q.append((ni,nj))
    return answer
mx_answer=0
for i in s:
    mx_answer=max(mx_answer,bfs(i))
print(mx_answer)



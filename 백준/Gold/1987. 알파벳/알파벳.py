import sys
r,c=map(int,sys.stdin.readline().strip().split())
arr=[list(sys.stdin.readline().strip()) for _ in range(r)]
answer=0
visit=set()

def dfs(pi,pj):
    global answer
    answer=max(answer,len(visit))
    for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
        ni,nj=pi+di,pj+dj
        if 0<=ni<r and 0<=nj<c and arr[ni][nj] not in visit:
            visit.add(arr[ni][nj])
            dfs(ni,nj)
            visit.remove(arr[ni][nj])
visit.add(arr[0][0])
dfs(0,0)
print(answer)
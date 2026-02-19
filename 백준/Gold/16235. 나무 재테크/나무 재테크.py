from collections import deque
n,m,k=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(n)]
ground=[[5]*n for _ in range(n)]
trees=[[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x,y,z=map(int,input().split())
    trees[x-1][y-1].append(z)
for i in range(n):
    for j in range(n):
        if trees[i][j]:
            trees[i][j].sort()
        trees[i][j]=deque(trees[i][j])

def spring_summer():
    for i in range(n):
        for j in range(n):
            if not trees[i][j]: # 나무 없으면 굳이?
                continue
            t=deque()
            bin=0
            for tree_age in trees[i][j]:
                if ground[i][j]>=tree_age:
                    t.append(tree_age+1)
                    ground[i][j]-=tree_age
                else:
                    bin+=(tree_age//2)
            trees[i][j]=t
            ground[i][j]+=bin
def fall():
    for i in range(n):
        for j in range(n):
            if not trees[i][j]:
                continue
            for tree_age in trees[i][j]:
                if tree_age%5==0:
                    for ii,jj in ((0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)):
                        ni,nj=i+ii,j+jj
                        if 0<=ni<n and 0<=nj<n:
                            trees[ni][nj].appendleft(1)

def winter():
    for i in range(n):
        for j in range(n):
            if A[i][j]:
                ground[i][j]+=A[i][j]

for _ in range(k):
    spring_summer()
    fall()
    winter()
answer=0
for i in range(n):
    for j in range(n):
        answer+=len(trees[i][j])
print(answer)

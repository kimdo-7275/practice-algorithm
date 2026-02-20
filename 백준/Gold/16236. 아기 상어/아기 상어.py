from collections import deque
n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if arr[i][j]==9:
            si,sj=i,j
arr[si][sj]=0
s_size=2
def find_fish(si,sj,s_size):
    visit=[[-1]*n for _ in range(n)]
    visit[si][sj]=0
    q=deque()
    q.append((si,sj))
    while q:
        lst = []
        for _ in range(len(q)):
            pi,pj=q.popleft()
            for di,dj in ((-1,0),(0,-1),(0,1),(1,0)):
                ni,nj=pi+di,pj+dj
                if 0<=ni<n and 0<=nj<n and visit[ni][nj]==-1:
                    if arr[ni][nj]>s_size:
                        continue
                    elif arr[ni][nj]==s_size or arr[ni][nj]==0:
                        visit[ni][nj]=visit[pi][pj]+1
                        q.append((ni,nj))
                    else:
                        lst.append((ni,nj,visit[pi][pj]+1))
        if lst:
            lst.sort(key=lambda x : (x[0],x[1]))
            return lst[0][0],lst[0][1],lst[0][2]
    return False

def main(si,sj,s_size):
    answer = 0
    eat=0
    while True:
        for _ in range(s_size):
            if not find_fish(si,sj,s_size):
                print(answer)
                return
            si, sj, sec = find_fish(si, sj,s_size)
            eat+=1
            answer += sec
            arr[si][sj]=0
            if eat==s_size:
                s_size+=1
                eat=0

main(si,sj,s_size)


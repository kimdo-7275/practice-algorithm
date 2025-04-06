N = int(input())

stat = [list(map(int,input().split())) for _ in range(N)]

visited = [False] * N

differ = float("inf") # 팀 star, link의 능력치 차이

def dfs(half, idx): # a는 팀원이 반틈으로 나워졌는지?(a= 팀star의 팀원 수)
    global differ
    if half == N // 2:
        team_star = 0
        team_link = 0

        for i in range(N):
            for j in range(N):

                if visited[i] and visited[j]:
                    team_star += stat[i][j]
                elif not visited[i] and not visited[j]:
                    team_link += stat[i][j]
        differ = min(differ, abs(team_star-team_link))
        return
    else: # 팀 나누기 (재귀 사용)
        for a in range(idx, N):
            if not visited[a]:
                visited[a]=True
                dfs(half+1, a+1)
                visited[a]=False
dfs(0,0)
print(differ)



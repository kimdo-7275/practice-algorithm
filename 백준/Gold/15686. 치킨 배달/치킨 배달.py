N, M = map(int, input().split())
graph =[list(map(int, input().split())) for _ in range(N)]

# 집이랑 치킨 배열
house, chicken = [], []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            house.append((i,j))
        if graph[i][j] == 2:
            chicken.append((i,j))

answer = float("inf") # 전체 치킨집중에서 M개치킨집에서 최소거리
chicken_idx = []

def dfs(idx,cnt):
    global answer
    # 치킨집 인덱스 넘어가면 return
    if idx > len(chicken):
        return

    if cnt == M: # 치킨집 인덱스가 다 채워졌다. house랑 거리계산해야지
        cnt_chicken_dist = 0 # 지금 고른 치킨집에서 최소거리
        for hx, hy in house: # 집을 기준으로 하기
            nearest_dist = float("inf") # 선택한 집에서 가장 가까운 치킨집거리
            for i in chicken_idx:
                nearest_dist = min(nearest_dist, abs(hx-chicken[i][0])+abs(hy-chicken[i][1]))
            cnt_chicken_dist+=nearest_dist
        answer=min(answer,cnt_chicken_dist)

    chicken_idx.append(idx)
    dfs(idx+1, cnt+1) # 지금 치킨집 넣고 다음 인덱스 치킨집으로 넘어가자
    chicken_idx.pop()
    dfs(idx+1, cnt) # 지금 치킨집 안넣고 다음 인덱스 치킨집으로 넘어가자

    return answer

print(dfs(0,0))





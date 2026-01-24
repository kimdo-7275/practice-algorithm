import heapq
n,m=map(int,input().split())
arr=[[] for _ in range(n+1)]
dist=[float('inf') for _ in range(n+1)]
dist[1]=0
for _ in range(m):
    a,b,c=map(int,input().split())
    arr[a].append([b,c])
    arr[b].append([a,c])
# arr에는 [노드, 비용]으로 저장
hq=[[0,1]]  # 힙은 [비용,노드]로 저장 -> 비용이 제일 작은 거부터 보려고
while hq:
    cnt_dist,cnt_node = heapq.heappop(hq)

    if cnt_dist>dist[cnt_node]: # 이미 더 짧게 방문 넘어가주세요
        continue

    for nd,d in arr[cnt_node]:
        dis=cnt_dist+d
        if dist[nd]>dis:
            dist[nd]=dis
            heapq.heappush(hq,[dis,nd])
print(dist[n])
import heapq
N,M=map(int,input().split())
roads=[[] for _ in range(N+1)]
distance=[float('inf') for _ in range(N+1)]

for _ in range(M):
    a,b,d=map(int,input().split())
    roads[a].append([b,d])
    roads[b].append([a,d])
distance[1]=0
heap=[[0,1]]    # [거리,노드] 이렇게 저장하기
while heap:
    c_dis,c_nd=heapq.heappop(heap)
    if distance[c_nd]<c_dis:
        continue
    for nd,dis in roads[c_nd]:
        n_dis=c_dis+dis
        if distance[nd]>n_dis:
            distance[nd]=n_dis
            heapq.heappush(heap,[n_dis,nd])
print(distance[N])
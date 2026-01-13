import heapq
n=int(input())
heap=[]
for _ in range(n):
    lst=list(map(int,input().split()))
    if not heap:
        heap=lst
        heapq.heapify(heap)
    for i in lst:
        if heap[0] < i:
            heapq.heappop(heap)
            heapq.heappush(heap,i)
print(heap[0])
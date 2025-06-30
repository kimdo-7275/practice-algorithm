import heapq

def solution(n, works):
    if sum(works)<=n:
        return 0
    works = [-w for w in works]
    heapq.heapify(works)
    while n!=0:
        val = heapq.heappop(works)
        val+=1
        heapq.heappush(works,val)
        n-=1
    answer = 0
    
    for i in works:
        answer+=(i**2)
    return answer
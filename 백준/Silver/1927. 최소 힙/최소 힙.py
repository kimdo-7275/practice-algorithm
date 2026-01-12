import heapq
import sys
q=[]
heapq.heapify(q)
n=int(input())
for _ in range(n):
    x=int(sys.stdin.readline().strip())
    if x==0:
        if len(q)==0:
            print(0)
        else:
            print(heapq.heappop(q))
    else:
        heapq.heappush(q,x)

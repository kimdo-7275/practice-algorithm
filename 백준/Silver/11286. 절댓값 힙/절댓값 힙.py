import heapq
import sys

n = int(input())
plus = []
minus = []
answer = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(plus) != 0 and len(minus) != 0:
            p = heapq.heappop(plus)
            m = heapq.heappop(minus)
            if p >= m:
                answer.append(-m)
                heapq.heappush(plus, p)
            elif p < m:
                answer.append(p)
                heapq.heappush(minus, m)
        elif len(plus) != 0:
            p = heapq.heappop(plus)
            answer.append(p)
        elif len(minus) != 0:
            m = heapq.heappop(minus)
            answer.append(-m)
        else:
            answer.append(0)
    if x > 0:
        heapq.heappush(plus, x)
    if x < 0:
        heapq.heappush(minus, -x)
for i in answer:
    print(i)
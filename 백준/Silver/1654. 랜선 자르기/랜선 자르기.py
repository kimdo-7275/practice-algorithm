N, K = map(int,input().split())
import sys
lines = [int(sys.stdin.readline().strip()) for _ in range(N)]
low = 1
high = max(lines)

while low <= high:
    can_make = 0
    mid = (low+high)//2
    for i in lines:
        can_make += i//mid
    if can_make >= K:
        low = mid + 1
    else:
        high = mid - 1
print(high)
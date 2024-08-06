import sys

n = int(input())
lst = list(map(int, sys.stdin.readline().split()))

lst.sort()

answer = 0
cnt = 0
for i in range(n):
    cnt += lst[i]
    answer += cnt
print(answer)
import sys

n, m = map(int, input().split())

c = {}

answer=[]

for _ in range(n):
    cant_l = sys.stdin.readline().strip()
    c[cant_l] = 1

for _ in range(m):
    cant_s = sys.stdin.readline().strip()
    if cant_s in c:
        answer.append(cant_s)

answer.sort()

print(len(answer))
for i in answer:
    print(i)
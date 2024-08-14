n, m = map(int, input().split())
visit = [101 for _ in range(101)]
visit[1] = 0
d1 = {}
d2 = {}

for _ in range(n):
    x, y = map(int, input().split())
    d1[x] = y
for _ in range(m):
    u, v = map(int, input().split())
    d2[u] = v
for _ in range(2):
    for i in range(1, 101):
        for j in range(1, 7):
            n = i + j
            if n > 100:
                break
            if n in d2:
                visit[d2[n]]=min(visit[d2[n]],visit[i]+1)
                continue
            else:
                visit[n] = min(visit[i] + 1, visit[n])
            if n in d1:
                visit[d1[n]] = min(visit[n], visit[d1[n]])
print(visit[100])

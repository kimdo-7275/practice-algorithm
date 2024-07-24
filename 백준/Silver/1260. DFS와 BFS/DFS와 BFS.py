import sys
from collections import deque

N, M, V = map(int, input().split())
gp = list([] for i in range(N + 1))
for _ in range(M):
    lst = list(map(int, sys.stdin.readline().split()))
    gp[lst[0]].append(lst[1])
    gp[lst[1]].append(lst[0])
for i in gp:
    i.sort()


def dfs(gp, start, visited=[]):
    visited.append(start)
    for i in gp[start]:
        if i not in visited:
            dfs(gp, i, visited)
    return visited


def bfs():
    visited = [0] * (N + 1)
    q = deque()
    visited[V] = 1
    print(V, end=" ")
    q.append(gp[V])
    while q:
        lst1 = q.popleft()
        for i in lst1:
            if visited[i] == 0:
                visited[i] = 1
                print(i, end=" ")
                q.append(gp[i])


answer_dfs = dfs(gp, V)
for i in answer_dfs:
    print(i,end=" ")
print()
bfs()
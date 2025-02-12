import sys

T = int(input())

lst = [[int(sys.stdin.readline().strip()) for _ in range(2)] for __ in range(T)]

floor = max(lst, key = lambda x : x[0])[0]
ho = max(lst, key = lambda x : x[1])[1]

graph = [[0] * ho for i in range(floor+1)]

for i in range(floor+1):
    for j in range(ho):
        if (i > 0) and (j > 0):
            graph[i][j] = graph[i][j-1]+graph[i-1][j]
        elif (i > 0):
            graph[i][j] = graph[i-1][j]
        else:
            graph[i][j] = graph[i][j-1] + 1

for f,h in lst:
    print(graph[f][h-1])
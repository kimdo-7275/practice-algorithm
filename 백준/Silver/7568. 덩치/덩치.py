N=int(input())
lst = [list(map(int,input().split())) for _ in range(N)]
answer = []

for i in range(N):
    rank=0
    for j in range(N):
        if i == j:
            continue
        if (lst[i][0] < lst[j][0]) and (lst[i][1] < lst[j][1]):
            rank += 1
    answer.append(str(rank+1))

print(' '.join(answer))

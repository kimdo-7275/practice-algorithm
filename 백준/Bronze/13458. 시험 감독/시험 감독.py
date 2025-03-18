N = int(input())
lst = list(map(int, input().split()))
B, C = map(int, input().split())

answer = 0
for i in lst:
    if i<B:
        answer+=1
        continue
    tmp = 1 + (i-B)//C
    if (i-B)%C != 0:
        tmp+=1
    answer+=tmp
print(answer)

n = int(input())
lst = list(map(int,input().split()))
lst.sort()
start = 0
end = len(lst)-1
total = lst[start] + lst[end]
answer = [start,end]

while start != end:
    tmp = lst[start] + lst[end]
    if abs(tmp) < abs(total):
        total = tmp
        answer = [start,end]
    if tmp > 0:
        end -= 1
        continue
    elif tmp < 0:
        start += 1
        continue
    elif tmp == 0:
        answer = [start, end]
        break
print(lst[answer[0]], lst[answer[1]])
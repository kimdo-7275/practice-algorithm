# [1,2,3,4,5,6,7]
N,K = map(int,input().split())

lst=[i for i in range(N)]
answer=[]
i=K-1
while lst:
    temp = lst.pop(i)
    answer.append(temp+1)
    if lst:
        i=(i+K-1)%len(lst)

print("<", end='')
for i in answer[:-1]:
    print(i,end=', ')
print(answer[-1],end='>')

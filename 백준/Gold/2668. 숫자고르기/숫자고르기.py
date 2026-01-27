n=int(input())
arr=[0]+[int(input()) for _ in range(n)]
visit=[0]*(n+1)
for i in range(1,n+1):
    if visit[i]==1:
        continue
    s=set()
    s.add(i)
    start=i
    while True:
        i=arr[i]
        if visit[i]==1: # 기존에 방문했다면 컷!
            break
        if i==start:
            for j in s:
                visit[j]=1
            break
        elif i not in s:
            s.add(i)
        else:
            break
answer=[]
for i in range(n+1):
    if visit[i]==1:
        answer.append(i)
print(len(answer))
for i in answer:
    print(i)







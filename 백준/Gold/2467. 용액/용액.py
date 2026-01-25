n=int(input())
lst=list(map(int,input().split()))
start,end=0,n-1
answer=[lst[start],lst[end]]

while start<end:
    tmp=lst[start]+lst[end]
    if abs(tmp) < abs(sum(answer)):
        answer[0]=lst[start]
        answer[1]=lst[end]
    if tmp>0:
        end-=1
        continue
    elif tmp<0:
        start+=1
        continue
    else:
        break
print(*answer)
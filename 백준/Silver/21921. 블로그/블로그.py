n,x=map(int,input().split())
lst=list(map(int,input().split()))

visit=sum(lst[:x])
mx=visit
count=1 if visit else 0

for i in range(x,n):
    visit += (lst[i] - lst[i - x])
    if visit==mx:
        count+=1
    elif visit>mx:
        mx=visit
        count=1

if mx==0:
    print('SAD')
else:
    print(mx)
    print(count)
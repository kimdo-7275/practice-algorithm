h,w=map(int,input().split())
arr=[[0]*w for _ in range(h)]
lst=list(map(int,input().split()))
for i in range(w):
    b_h=lst[i]
    for j in range(-1,-(b_h+1),-1):
        arr[j][i]=1
answer=0
for i in range(-1,-(h+1),-1):
    zero_count=0
    can=False
    for j in range(w):
        if arr[i][j]==1:
            if zero_count and can:
                answer+=zero_count
                zero_count=0
                continue
            else:
                can = True
                zero_count=0
        elif arr[i][j]==0 and can:
            zero_count+=1
print(answer)

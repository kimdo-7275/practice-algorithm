n=int(input())
lst=[list(map(int,input().split())) for _ in range(n)]
lst.sort(key=lambda x:x[0])
f_max=max(lst,key=lambda x:x[1])
max_loc,max_length=f_max[0],f_max[1]

answer=0
now_length=lst[0][1]
if now_length!=max_length:
    for i in range(1,n):
        answer += now_length * (lst[i][0] - lst[i - 1][0])
        if lst[i][1] > now_length:
            now_length=lst[i][1]
            if now_length==max_length:
                break
now_length=lst[-1][1]
for i in range(-2,-(n+1),-1):
    answer += now_length * (lst[i+1][0] - lst[i][0])
    if lst[i][1]>now_length:
        now_length = lst[i][1]
    if now_length==max_length:
        answer+=max_length*(lst[i][0]-max_loc+1)
        break
if n==1:
    answer=max_length*1
print(answer)
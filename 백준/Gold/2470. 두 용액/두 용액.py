N=int(input())
lst=list(map(int,input().split()))
lst.sort()
s,e=0,N-1
total=2*(10**9)
answer=[]
while s<e:
    tmp_total=lst[s]+lst[e]
    if tmp_total>0:
        if abs(tmp_total) < abs(total):
            answer=[lst[s],lst[e]]
            total=tmp_total
        e-=1

    elif tmp_total<0:
        if abs(tmp_total) < abs(total):
            answer=[lst[s],lst[e]]
            total = tmp_total
        s+=1
    else:
        answer=[lst[s],lst[e]]
        break
print(*answer)

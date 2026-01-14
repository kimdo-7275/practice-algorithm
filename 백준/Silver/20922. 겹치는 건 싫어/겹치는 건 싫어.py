n,k=map(int,input().split())
arr=list(map(int,input().split()))
s,e=0,0
d={}
answer=0
length=0
for _ in range(n):
    if arr[e] not in d:
        d[arr[e]]=1
        length+=1
        answer=max(answer,length)
        e += 1
        continue
    elif d[arr[e]]<k:
        d[arr[e]]+=1
        length+=1
        answer=max(answer,length)
        e += 1
        continue
    elif d[arr[e]]==k:
        for _ in range(s,e):
            if arr[s]!=arr[e]:
                d[arr[s]]-=1
                s += 1
                length-=1
            else:
                s+=1
                e+=1
                answer=max(answer,length)
                break
print(answer)




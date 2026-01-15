n,d,k,c=map(int,input().split())
lst=[int(input()) for _ in range(n)]
dic={}
for i in range(k):
    if lst[i] not in dic:
        dic[lst[i]]=1
    else:
        dic[lst[i]]+=1
if c not in dic:
    dic[c]=1
else:
    dic[c]+=1
answer=len(dic)
length=len(dic)
for s in range(n):
    e=(s+k)%n   # e넣고 s뺄거에요
    if lst[e] not in dic:
        dic[lst[e]]=1
        length+=1
    elif dic[lst[e]]==0:
        dic[lst[e]]+=1
        length+=1
    else:
        dic[lst[e]] += 1
    if dic[lst[s]]==1:
        dic[lst[s]]-=1
        length-=1
    else:
        dic[lst[s]]-=1
    answer=max(answer,length)
print(answer)



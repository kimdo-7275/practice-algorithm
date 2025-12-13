word=input()
d={}
for s in word:
    s=s.upper()
    if s not in d:
        d[s]=1
    else:
        d[s]+=1
lst=list(d.items())
lst.sort(key=lambda x : -x[1])
if len(lst)==1:
    print(lst[0][0])
elif lst[0][1]==lst[1][1]:
    print("?")
else:
    print(lst[0][0])

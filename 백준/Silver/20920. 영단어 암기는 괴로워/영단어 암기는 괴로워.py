import sys
n,m=map(int,input().split())
d={}
for _ in range(n):
    word = sys.stdin.readline().strip()
    if len(word) < m:
        continue
    if word not in d:
        d[word]=1
    else:
        d[word]+=1
lst=list(d.items())
lst.sort(key=lambda x:(-x[1],-len(x[0]),x[0]))
for i in lst:
    print(i[0])

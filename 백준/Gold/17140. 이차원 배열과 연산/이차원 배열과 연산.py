r,c,k=map(int,input().split())

arr=[[0]*100 for _ in range(100)]
for i in range(3):
    aa,bb,cc=map(int,input().split())
    arr[i][0]=aa
    arr[i][1]=bb
    arr[i][2]=cc
answer=0
max_raw=3
max_col=3
def check():
    if arr[r-1][c-1]==k:
        return True
    return False
def raw_align(i):
    lst=[]
    d={}
    for j in range(100):
        if arr[i][j]==0:
            continue
        if arr[i][j] not in d:
            d[arr[i][j]]=1
        else:
            d[arr[i][j]]+=1
    for key in d:
        lst.append((key,d[key]))
    lst.sort(key=lambda x: (x[1],x[0]))
    tmp=[]
    for tu in lst:
        tmp.append(tu[0])
        tmp.append(tu[1])
    arr[i]=tmp+[0]*(100-len(lst)*2)
    return len(tmp)
def col_align(j):
    lst=[]
    d={}
    for i in range(100):
        if arr[i][j]==0:
            continue
        if arr[i][j] not in d:
            d[arr[i][j]]=1
        else:
            d[arr[i][j]]+=1
    for key in d:
        lst.append((key,d[key]))
    lst.sort(key=lambda x: (x[1],x[0]))
    tmp = []
    for tu in lst:
        tmp.append(tu[0])
        tmp.append(tu[1])
    for i in range(len(tmp)):
        arr[i][j]=tmp[i]
    for i in range(len(tmp),100):
        arr[i][j]=0
    return len(tmp)

while True:
    if answer==100 and not check():
        print(-1)
        break
    if check():
        print(answer)
        break
    if max_col>=max_raw:
        for i in range(100):
            max_raw=max(max_raw,raw_align(i))
    else:
        for j in range(100):
            max_col=max(max_col,col_align(j))
    answer+=1
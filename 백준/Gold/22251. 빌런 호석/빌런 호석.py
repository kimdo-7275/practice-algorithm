def cnt(a,b):
     count=0
     lst0=num[a]
     lst1=num[b]
     for i in range(7):
          if lst0[i]!=lst1[i]:
               count+=1
     return count
num=[[1,1,1,0,1,1,1],
     [0,0,1,0,0,1,0],
     [1,0,1,1,1,0,1],
     [1,0,1,1,0,1,1],
     [0,1,1,1,0,1,0],
     [1,1,0,1,0,1,1],
     [1,1,0,1,1,1,1],
     [1,0,1,0,0,1,0],
     [1,1,1,1,1,1,1],
     [1,1,1,1,0,1,1]]
arr=[[0]*10 for _ in range(10)]
for i in range(10):
     for j in range(i,10):
          count=cnt(i,j)
          arr[i][j]=count
          arr[j][i]=count
n,k,p,x=map(int,input().split())
answer=0
for i in range(1,n+1): # i랑 x랑 비교 할겁니다
    count=0
    for j in range(k):
        a=i//(10**j)%10
        b=x//(10**j)%10
        count+=arr[a][b]
    if count<=p:
        answer+=1
print(answer-1)
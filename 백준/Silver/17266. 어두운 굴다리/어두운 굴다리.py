N=int(input())
M=int(input())
lst=list(map(int,input().split()))

length=lst[0]
for i in range(1,len(lst)):
    if lst[i]-2*length > lst[i-1]:
        length=(lst[i]-lst[i-1]+1)//2
if lst[-1]+length < N:
    length=N-lst[-1]
print(length)
n,m = map(int,input().split())
lst = [0]*(n+1)
lst[0]=1
mod = 1000000007
for i in range(1,(n+1)):
    if 0<=(i-m):
        lst[i]=(lst[i-1]+lst[i-m])%mod
    else:
        lst[i] = lst[i - 1]%mod
print(lst[-1])

n=int(input())
dis=list(map(int,input().split()))
pri=list(map(int,input().split()))

total_price=dis[0]*pri[0]
now_pri=pri[0]
for i in range(1,n-1):
    if now_pri < pri[i]:
        total_price+=now_pri*dis[i]
    else:
        now_pri=pri[i]
        total_price+=now_pri*dis[i]
print(total_price)

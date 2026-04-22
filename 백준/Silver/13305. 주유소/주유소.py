N=int(input())
distance=list(map(int,input().split()))
gas_price=list(map(int,input().split()))
answer=distance[0]*gas_price[0]
now_price=gas_price[0]

for idx in range(1,N-1):
    if gas_price[idx] < now_price:
        now_price=gas_price[idx]
        answer+=now_price*distance[idx]
    else:
        answer+=now_price*distance[idx]
print(answer)
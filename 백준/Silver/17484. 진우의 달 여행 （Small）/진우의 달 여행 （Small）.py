n,m=map(int,input().split())
lst=[list(map(int,input().split())) for _ in range(n)]

dp=[[[float('inf')]*3 for _ in range(m)] for _ in range(n)]
# 0번 행 초기화 하기
for i in range(m):
    for d in range(3):
        dp[0][i][d]=lst[0][i]

for i in range(1,n):
    for j in range(m):
        dp[i][j][0]=min(dp[i-1][j][1],dp[i-1][j][-1])+lst[i][j]
        if 0<=j-1:
            dp[i][j][-1]=min(dp[i-1][j-1][0],dp[i-1][j-1][1])+lst[i][j]
        if m>j+1:
            dp[i][j][1]=min(dp[i-1][j+1][-1],dp[i-1][j+1][0])+lst[i][j]
answer=float('inf')
# print(dp[-1])
for i in dp[-1]:
    answer=min(answer,min(i))
print(answer)
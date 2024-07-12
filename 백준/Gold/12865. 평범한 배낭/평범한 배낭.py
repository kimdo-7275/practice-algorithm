N, K = map(int,input().split()) # N이 물건의 개수, K가 가방에 담을 수 있는 최대 무게
lst=[]
for _ in range(N):
    w,v=map(int,input().split())
    lst.append([w,v])
def solution(weight,items):
    dp=[[0]*(weight+1) for _ in range(len(items)+1)]
    for i in range(1,len(items)+1):
        for j in range(1, weight+1):
            if j>=items[i-1][0]:
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-items[i-1][0]]+items[i-1][1])
            else:
                dp[i][j]=dp[i-1][j]
    return dp[-1][-1]
print(solution(K,lst))
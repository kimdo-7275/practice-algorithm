N=int(input())
numbers = list(map(int,input().split()))
operation = list(map(int,input().split())) # +-*/

maxi = float("-inf")
mini = float("inf")

def dfs(n,value):
    global maxi, mini

    if n==N-1:
        maxi = max(maxi, value)
        mini = min(mini, value)
        return

    if operation[0]!=0:
        operation[0]-=1
        dfs(n+1, value+numbers[n+1])
        operation[0]+=1

    if operation[1]!=0:
        operation[1]-=1
        dfs(n+1, value-numbers[n+1])
        operation[1]+=1

    if operation[2]!=0:
        operation[2]-=1
        dfs(n+1, value*numbers[n+1])
        operation[2]+=1

    if operation[3]!=0:
        operation[3]-=1
        dfs(n+1, int(value/numbers[n+1]))
        operation[3]+=1
dfs(0,numbers[0])
print(maxi)
print(mini)


import sys

sys.setrecursionlimit(10 ** 6)

N = int(input())
S = list(map(int, input().split()))
num=[0]*10

def sol(start,end,max_num,kind):
    if end>=N:
        return max_num
    
    num[S[end]]+=1
    if num[S[end]]==1:
        kind+=1
    if kind>2:
        num[S[start]]-=1
        if num[S[start]]==0:
            kind-=1
        start+=1
    
    max_num=max(max_num, end-start+1)
    return sol(start,end+1,max_num,kind)

print(sol(0,0,0,0))
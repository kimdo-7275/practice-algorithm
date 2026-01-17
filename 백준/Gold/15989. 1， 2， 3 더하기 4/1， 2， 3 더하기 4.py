T=int(input())
test_case=[int(input()) for _ in range(T)]
mx=max(test_case)
lst=[1]*(mx+1)
for i in range(2,mx+1):
    lst[i]+=lst[i-2]
for i in range(3,mx+1):
    lst[i]+=lst[i-3]
for i in test_case:
    print(lst[i])
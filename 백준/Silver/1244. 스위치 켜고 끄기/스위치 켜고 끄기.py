n1=int(input())  # 스위치 수
lst=list(map(int,input().split()))
n2=int(input())
for _ in range(n2):
    gen, num = map(int,input().split())
    num-=1
    if gen==1:
        lst[num]=(lst[num]+1)%2
        ad=num+1
        while True:
            num+=ad
            if num < n1:
                lst[num]=(lst[num]+1)%2
            else: break
    elif gen==2:
        lst[num]=(lst[num]+1)%2
        pr, nt = num, num
        while True:
            pr-=1
            nt+=1
            if pr >= 0 and nt < n1 and lst[pr]==lst[nt]:
                lst[pr]=(lst[pr]+1)%2
                lst[nt]=(lst[nt]+1)%2
            else:
                break
for i in range(len(lst)):
    if i%20==19:
        print(lst[i])
    else:
        print(lst[i],end=' ')
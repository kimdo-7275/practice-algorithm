T=int(input())

def dfs(s,n,total,cal):
    if cal == ' ':
        num=0
        space=0
        n_cal='+'
        for i in range(len(s)-1,-1,-1):
            if s[i]=='+' or s[i]=='-':
                n_cal=s[i]
                break
            elif s[i]==' ':
                space+=1
            else:   # 숫자일 때
                num=num+int(s[i])*(10**space)
        s += ' '
        s += str(n)
        if n_cal=='+':
            total=total+(num*9)+n
        elif n_cal=='-':
            total=total-(num*9)-n
    elif cal=='+':
        s+='+'
        s+=str(n)
        total+=n
    elif cal=='-':
        s+='-'
        s+=str(n)
        total-=n
    if n!=number:
        dfs(s,n+1,total,' ')
        dfs(s, n + 1, total, '+')
        dfs(s, n + 1, total, '-')
    if n==number and total==0:
        print(s)


for _ in range(T):
    number=int(input())
    dfs('1',2,1,' ')
    dfs('1',2,1,'+')
    dfs('1',2,1,'-')
    print()


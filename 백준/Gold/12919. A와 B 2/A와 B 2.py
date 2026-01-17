S=input()
T=input()

def dfs(s,t):
    if len(s)==len(t):
        if s==t:
            return 1
        else:
            return 0
    if s not in t and ''.join(reversed(s)) not in t:
        return 0
    case1=dfs(s+'A',t)
    case2=dfs(''.join(reversed(s+'B')),t)
    return case1 or case2
print(dfs(S,T))

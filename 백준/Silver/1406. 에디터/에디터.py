import sys
s1=list(input())
s2=[]
m=int(input())
for _ in range(m):
    command=list(sys.stdin.readline().strip().split())
    if command[0]=='L':
        if s1:
            s2.append(s1.pop())
    elif command[0]=='D':
        if s2:
            s1.append(s2.pop())
    elif command[0]=='B':
        if s1:
            s1.pop()
    elif command[0]=='P':
        s1.append(command[1])
s2.reverse()
s1.extend(s2)
print(''.join(s1))

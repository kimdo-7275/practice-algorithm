N=int(input())
buildings=[]
for _ in range(N):
    _,b = map(int,input().split())
    buildings.append(b)
answer=0
stack=[0]
for i in buildings:
    if stack[-1]<i:
        stack.append(i)
    else:
        while True:
            if stack[-1]>i:
                stack.pop()
                answer+=1
            elif stack[-1]<i:
                stack.append(i)
                break
            else:
                break
answer+=(len(stack)-1)
print(answer)
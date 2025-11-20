n = int(input())
stack = [0]
answer = 0
buildings = []
for i in range(n):
    buildings.append(int(input().split()[1]))
buildings.append(0)

for a in buildings:
    while stack[-1] > a:
        answer+=1

        b = stack.pop()
        while b == stack[-1]:
            stack.pop()

    stack.append(a)

print(answer)
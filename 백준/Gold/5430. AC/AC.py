from collections import deque

t = int(input())
answer = []


def func():
    global answer
    p = input()  # RDD
    n = int(input())  # 4
    x = input()  # [1,2,3,4]
    if x == '[]':
        lst = []
    else:
        lst = list(map(int, x[1:-1].split(',')))
    lst = deque(lst)
    reverse = 1  # 1일때 정방향, -1일때 역방향
    for s in p:
        if s == 'R':
            reverse *= -1
        elif s == 'D':
            if len(lst) == 0:
                answer.append('error')
                return
            if reverse == 1:
                lst.popleft()
            else:
                lst.pop()
    if len(lst) == 0:
        answer.append('[]')
        return
    if reverse == 1:
        answer.append(list(lst))
    else:
        lst = list(lst)
        lst = list(reversed(lst))
        answer.append(lst)


for _ in range(t):
    func()

for i in answer:
    if i == 'error':
        print(i)
    elif i=='[]':
        print('[]')
    else:
        s = '['
        for j in i:
            s += str(j)
            s += ','
        s = s[:-1]
        s += ']'
        print(s)

import sys
# sys.stdin.readline().strip()
n,m=map(int,input().split())
words = [sys.stdin.readline().strip() for _ in range(n)]
words=set(words)
s=set()

for _ in range(m):
    lst=sys.stdin.readline().strip().split(',')
    for i in lst:
        if i in words:
            words.remove(i)

    print(len(words))
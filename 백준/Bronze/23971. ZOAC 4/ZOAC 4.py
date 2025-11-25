h,w,n,m = map(int,input().split())

a = 0
b = 0
a += (h//(n+1))
if h % (n+1) != 0:
    a += 1

b += (w//(m+1))
if w % (m+1) != 0:
    b += 1

print(a*b)
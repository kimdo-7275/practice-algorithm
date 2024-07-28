n, r, c = map(int, input().split())
count = 0
while n != 1:
    if (2 ** (n - 1)) <= r:
        if (2 ** (n - 1)) <= c:
            count += 3 * (2 ** (n - 1))**2
            r -= (2 ** (n - 1))
            c -= (2 ** (n - 1))
            n -= 1
        else:
            count += 2 * (2 ** (n - 1))**2
            r -= (2 ** (n - 1))
            n -= 1
    elif (2 ** (n - 1)) <= c:
        count += (2 ** (n - 1))**2
        c -= (2 ** (n - 1))
        n -= 1
    else:
        n -= 1
if r == 0:
    if c == 0:
        pass
    else:
        count += 1
elif c == 0:
    count += 2
else:
    count += 3
print(count)
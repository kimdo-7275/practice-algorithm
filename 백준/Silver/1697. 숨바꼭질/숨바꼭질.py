import math

N, M = map(int, input().split())


# math.inf
def sol(n, m):
    lst = [math.inf] * (m + 2)
    lst[n] = 0
    # n 이전에 채우기
    for i in range(n):
        if n - 1 - i >= 0:
            lst[n - 1 - i] = i + 1
    # n부터 m까지 채우기
    for _ in range(2):
        for i in range(n + 1, m + 2):
            # 짝수 일때
            if i % 2 == 0:
                if i // 2 >= 0 and i + 1 < m + 2:
                    lst[i] = min(min(lst[i // 2], lst[i - 1], lst[i + 1]) + 1, lst[i])
                elif i // 2 >= 0:
                    lst[i] = min(min(lst[i // 2], lst[i - 1]) + 1, lst[i])
                elif i + 1 < m + 2:
                    lst[i] = min(min(lst[i - 1], lst[i + 1]) + 1, lst[i])
                else:
                    lst[i] = min(lst[i - 1] + 1, lst[i])
            else:  # 홀 수 있때
                if i + 1 < m + 2:
                    lst[i] = min(min(lst[i - 1], lst[i + 1]) + 1, lst[i])
                else:
                    lst[i] = min(lst[i - 1] + 1, lst[i])
    print(lst[m])


if N <= M:
    sol(N, M)
else:
    print(N - M)
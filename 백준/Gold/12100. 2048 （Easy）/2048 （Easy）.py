n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0


def rotate(arr):
    return list(map(list, zip(*arr[::-1])))


def move_down(arr):
    narr = []
    for j in range(n):
        lst = []
        pre = arr[-1][j]
        for i in range(-2, -(n + 1), -1):
            if arr[i][j] == 0:
                continue
            elif arr[i][j] == pre:
                lst.append(2 * pre)
                pre = 0
            else:
                if pre != 0:
                    lst.append(pre)
                pre = arr[i][j]
        if pre != 0:
            lst.append(pre)
        narr.append(lst + [0] * (n - len(lst)))
    for _ in range(3):
        narr = rotate(narr)
    return narr


def cal_max(arr, score):
    for ar in arr:
        score = max(score, max(ar))
    return score


def dfs(arr, cnt):
    global answer
    if cnt > 5:
        return
    answer = cal_max(arr, answer)
    # 아래
    n1arr = [x[:] for x in arr]
    dfs(move_down(n1arr), cnt + 1)
    # 오른쪽
    n2arr = [x[:] for x in arr]
    for _ in range(1):
        n2arr=rotate(n2arr)
    dfs(move_down(n2arr), cnt + 1)
    # 위쪽
    n3arr = [x[:] for x in arr]
    for _ in range(2):
        n3arr = rotate(n3arr)
    dfs(move_down(n3arr), cnt + 1)
    # 왼쪽
    n4arr = [x[:] for x in arr]
    for _ in range(3):
        n4arr = rotate(n4arr)
    dfs(move_down(n4arr), cnt + 1)

dfs(arr, 0)
print(answer)

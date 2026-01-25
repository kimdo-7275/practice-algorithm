def find_win(arr):
    # 1. 가로 체크
    x_win,o_win=False,False
    for i in range(3):
        if arr[i][0]==arr[i][1]==arr[i][2]:
            if arr[i][0]=='X':
                x_win=True
            elif arr[i][0]=='O':
                o_win=True
    # 2. 새로 체크
    for i in range(3):
        if arr[0][i]==arr[1][i]==arr[2][i]:
            if arr[0][i]=='X':
                x_win=True
            elif arr[0][i]=='O':
                o_win=True
    # 3. 대각선 체크
    if arr[0][0]==arr[1][1]==arr[2][2]:
        if arr[1][1]=='X':
            x_win=True
        elif arr[1][1]=='O':
            o_win=True
    elif arr[0][2]==arr[1][1]==arr[2][0]:
        if arr[1][1]=='X':
            x_win=True
        elif arr[1][1]=='O':
            o_win=True
    return x_win, o_win

while True:
    s=input()
    if s=='end':
        break
    s=list(s)
    arr=[s[i:i+3] for i in range(0,len(s),3)]
    x_count, o_count = 0,0
    x_win, o_win = find_win(arr)
    # 1. X,O 개수 카운트 하기
    for i in range(3):
        for j in range(3):
            if arr[i][j]=='X':
                x_count+=1
            elif arr[i][j]=='O':
                o_count+=1
    if o_count>x_count or x_count > o_count+1:
        print('invalid')
        continue
    # 2. O랑 X가 같은데 O가 이긴 경우
    if x_count==o_count+1 and o_win:
        print('invalid')
        continue
    # 3. 아무도 이기지 않았는 데 모든 칸이 다 차지 않은 경우!
    if not x_win and not o_win and x_count+o_count!=9:
        print('invalid')
        continue
    # 4. X,O 둘 다 모두 이긴 경우
    if x_win and o_win:
        print('invalid')
        continue
    # 5. X가 이길 때 X가 O보다 1개 더 많아야함:
    if x_win and not o_win and x_count!=o_count+1:
        print('invalid')
        continue
    # 이 외는 다 가능
    print('valid')
# invalid인 경우 찾아보기!
# 1. O가 X보다 더 많은 경우!
#   X가 O보다 2개이상 더 많은 경우도 포함!
# 2. O랑 X가 같은데 O가 이긴 경우!
# 3. 아무도 이기지 않았는 데 모든 칸이 다 차지 않은 경우!
# 4. X,O 둘 다 모두 이긴 경우
# 5. X가 이길 때 X가 O보다 1개 더 많아야함

state=True

while state:
    num=input()
    if num == '0':
        state = False
        break

    answer = 'yes'

    for i in range(len(num)//2):
        if num[i] != num[-(i+1)]:
            answer = 'no'
            break

    print(answer)
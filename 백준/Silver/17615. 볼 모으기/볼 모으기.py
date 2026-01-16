n=int(input())
lst=list(input())
blue_count=0
red_count=0
for i in lst:
    if i=='B':
        blue_count+=1
    else:
        red_count+=1
answer=n
# 1. 빨강 모두 왼쪽
count=0
for i in lst:
    if i=='B':
        break
    else:
        count+=1
answer=min(answer,red_count-count)

# 2. 빨강 모두 오른쪽
count=0
for i in range(-1,-(n+1),-1):
    if lst[i]=='B':
        break
    else:
        count+=1
answer=min(answer,red_count-count)

# 3. 파랑 모두 왼쪽
count=0
for i in lst:
    if i=='R':
        break
    else:
        count+=1
answer=min(answer,blue_count-count)

# 4. 파랑 모두 오른쪽
count=0
for i in range(-1,-(n+1),-1):
    if lst[i]=='R':
        break
    else:
        count+=1
answer=min(answer,blue_count-count)
print(answer)
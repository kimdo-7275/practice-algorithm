S=input()
S=list(S)
count_0=0
count_1=0
for s in S:
    if s=='0':
        count_0+=1
    elif s=='1':
        count_1+=1
count_0//=2
count_1//=2
answer=[]
# 뒤에서부터 볼건데
while S:
    t=S.pop()
    if t=='1':
        if count_1!=0:
            answer.append(t)
            count_1-=1
    elif t=='0':
        if count_0!=0:
            count_0-=1
        else:
            answer.append(t)
answer.reverse()
print(''.join(answer))
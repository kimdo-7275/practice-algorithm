lst=list(input())
a_count=0
for i in lst:
    if i=='a':
        a_count+=1
change=0    # a개수의 길이만큼의 윈도우에서 b의 개수!(바꿀 개수)

for i in range(a_count):
    if lst[i]=='b':
        change+=1
answer=change
for s in range(len(lst)):
    e=(s+a_count)%len(lst) # e넣고 s빼고
    if lst[e]=='b':
        change+=1
    if lst[s]=='b':
        change-=1
    answer=min(answer,change)
print(answer)

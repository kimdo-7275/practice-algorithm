n=int(input())
start=list(input())
end=list(input())
answer=n+1
# case1 : 첫번째 스위치를 눌렀을 때
switch=[0]*n
switch[0]=1
state=[0]*n
state[0],state[1]=1,1
for i in range(1,n):
    if start[i-1]==end[i-1]:
        if state[i-1]%2==0:
            continue
        else:
            switch[i]=1
            state[i-1]+=1
            state[i]+=1
            if i!=n-1:
                state[i+1]+=1
    else:
        if state[i-1]%2==1:
            continue
        else:
            switch[i]=1
            state[i-1]+=1
            state[i]+=1
            if i!=n-1:
                state[i+1]+=1
if (start[-1]!=end[-1] and state[-1]%2==1) or\
    (start[-1]==end[-1] and state[-1]%2==0):
    answer=sum(switch)
# case2 : 첫번째 스위치를 누르지 않았을 때
switch=[0]*n
state=[0]*n
for i in range(1,n):
    if start[i-1]==end[i-1]:
        if state[i-1]%2==0:
            continue
        else:
            switch[i]=1
            state[i-1]+=1
            state[i]+=1
            if i!=n-1:
                state[i+1]+=1
    else:
        if state[i-1]%2==1:
            continue
        else:
            switch[i]=1
            state[i-1]+=1
            state[i]+=1
            if i!=n-1:
                state[i+1]+=1
if (start[-1]!=end[-1] and state[-1]%2==1) or\
    (start[-1]==end[-1] and state[-1]%2==0):
    answer=min(answer,sum(switch))
if answer==n+1:
    print(-1)
else:
    print(answer)
T=int(input())
for _ in range(T):
    n,k,t,m=map(int,input().split())
    # 팀별 : [팀,점수, 제출 횟수, 마지막 제출 순서]
    team = [[i]+[0]*3 for i in range(n+1)]
    # 점수 넣기 : 리스트 : [팀][문제]
    score = [[0]*(k+1) for _ in range(n+1)]
    for idx in range(m):
        i,j,s = map(int,input().split())
        team[i][2]+=1 # 제출횟수+=1
        team[i][3]=idx # 마지막 제출 순서
        score[i][j]=max(score[i][j],s)# 점수입력
    for i in range(n+1):
        team[i][1]=sum(score[i])
    team.sort(key=lambda x:(-x[1],x[2],x[3]))
    for i in range(n+1):
        if team[i][0]==t:
            print(i+1)
            break

